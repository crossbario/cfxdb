##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint

import cbor2
import flatbuffers

from cfxdb.gen.eventstore import Publication as PublicationGen


class _Publication(PublicationGen.Publication):
    """
    Expand methods on the class code generated by flatc.

    FIXME: comes up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsPublication(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _Publication()
        x.Init(buf, n + offset)
        return x

    def ArgsAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def KwargsAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def PayloadAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def EncKeyAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class Publication(object):
    """
    Persisted publication database object.
    """
    ENC_ALGO_NONE = 0
    ENC_ALGO_CRYPTOBOX = 1
    ENC_ALGO_MQTT = 2
    ENC_ALGO_XBR = 3

    ENC_SER_NONE = 0
    ENC_SER_JSON = 1
    ENC_SER_MSGPACK = 2
    ENC_SER_CBOR = 3
    ENC_SER_UBJSON = 4
    ENC_SER_OPAQUE = 5
    ENC_SER_FLATBUFFERS = 6

    __slots__ = (
        '_from_fbs',
        '_timestamp',
        '_publication',
        '_publisher',
        '_topic',
        '_args',
        '_kwargs',
        '_payload',
        '_acknowledge',
        '_retain',
        '_exclude_me',
        '_exclude',
        '_exclude_authid',
        '_exclude_authrole',
        '_eligible',
        '_eligible_authid',
        '_eligible_authrole',
        '_enc_algo',
        '_enc_key',
        '_enc_serializer',
    )

    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        self._timestamp = None
        self._publication = None
        self._publisher = None
        self._topic = None
        self._args = None
        self._kwargs = None
        self._payload = None
        self._acknowledge = None
        self._retain = None
        self._exclude_me = None
        self._exclude = None
        self._exclude_authid = None
        self._exclude_authrole = None
        self._eligible = None
        self._eligible_authid = None
        self._eligible_authrole = None
        self._enc_algo = None
        self._enc_key = None
        self._enc_serializer = None

    def marshal(self):
        obj = {
            'timestamp': self.timestamp,
            'publication': self.publication,
            'publisher': self.publisher,
            'topic': self.topic,
            'args': self.args,
            'kwargs': self.kwargs,
            'payload': self.payload,
            'acknowledge': self.acknowledge,
            'retain': self.retain,
            'exclude_me': self.exclude_me,
            'exclude': self.exclude,
            'exclude_authid': self.exclude_authid,
            'exclude_authrole': self.exclude_authrole,
            'eligible': self.eligible,
            'eligible_authid': self.eligible_authid,
            'eligible_authrole': self.eligible_authrole,
            'enc_algo': self.enc_algo,
            'enc_key': self.enc_key,
            'enc_serializer': self.enc_serializer,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def timestamp(self):
        """
        Timestamp when the publication was accepted by the broker. Epoch time in ns.

        :returns: epoch time in ns
        :rtype: int
        """
        if self._timestamp is None and self._from_fbs:
            self._timestamp = self._from_fbs.Timestamp()
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        assert value is None or type(value) == int
        self._timestamp = value

    @property
    def publication(self):
        """
        WAMP publication ID that was assigned by the broker.

        :returns: publication ID
        :rtype: int
        """
        if self._publication is None and self._from_fbs:
            self._publication = self._from_fbs.Publication()
        return self._publication

    @publication.setter
    def publication(self, value):
        assert value is None or type(value) == int
        self._publication = value

    @property
    def publisher(self):
        """
        WAMP session ID of the publisher.

        :returns: publisher ID
        :rtype: int
        """
        if self._publisher is None and self._from_fbs:
            self._publisher = self._from_fbs.Publisher()
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        assert value is None or type(value) == int
        self._publisher = value

    @property
    def topic(self):
        """
        The WAMP or application URI of the PubSub topic the event was published to.

        :returns: topic (URI) published to
        :rtype: str
        """
        if self._topic is None and self._from_fbs:
            self._topic = self._from_fbs.Topic().decode('utf8')
        return self._topic

    @topic.setter
    def topic(self, value):
        assert value is None or type(value) == str
        self._topic = value

    #
    # args, kwargs, payload
    #

    @property
    def args(self):
        """
        Positional values for application-defined event payload.

        :returns: positional arguments (app payload) of the event (if any)
        :rtype: None or list
        """
        if self._args is None and self._from_fbs:
            if self._from_fbs.ArgsLength():
                self._args = cbor2.loads(bytes(self._from_fbs.ArgsAsBytes()))
        return self._args

    @args.setter
    def args(self, value):
        assert value is None or type(value) == list
        self._args = value

    @property
    def kwargs(self):
        """
        Keyword values for application-defined event payload.

        :returns: keyword arguments (app payload) of the event (if any)
        :rtype: None or dict
        """
        if self._kwargs is None and self._from_fbs:
            if self._from_fbs.KwargsLength():
                self._kwargs = cbor2.loads(bytes(self._from_fbs.KwargsAsBytes()))
        return self._kwargs

    @kwargs.setter
    def kwargs(self, value):
        assert value is None or type(value) == dict
        self._kwargs = value

    @property
    def payload(self):
        """
        Alternative, transparent payload. If given, ``args`` and ``kwargs`` must be left unset.

        :returns: Transparent binary payload (see ``enc_algo``) if applicable
        :rtype: None or bytes
        """
        if self._payload is None and self._from_fbs:
            if self._from_fbs.PayloadLength():
                self._payload = self._from_fbs.PayloadAsBytes()
        return self._payload

    @payload.setter
    def payload(self, value):
        assert value is None or type(value) == bytes
        self._payload = value

    #
    # acknowledge, retain, exclude_me
    #

    @property
    def acknowledge(self):
        """
        If ``True``, the broker was asked to acknowledge the publication with a success or error response.

        :returns: acknowledge flag
        :rtype: None or bool
        """
        if self._acknowledge is None and self._from_fbs:
            self._acknowledge = self._from_fbs.Acknowledge()
        return self._acknowledge

    @acknowledge.setter
    def acknowledge(self, value):
        assert value is None or type(value) == bool
        self._acknowledge = value

    @property
    def retain(self):
        """
        If ``True``, the broker was requested to retain this event.

        :returns: retain flag
        :rtype: None or bool
        """
        if self._retain is None and self._from_fbs:
            self._retain = self._from_fbs.Retain()
        return self._retain

    @retain.setter
    def retain(self, value):
        assert value is None or type(value) == bool
        self._retain = value

    @property
    def exclude_me(self):
        """
        If ``True``, the broker was asked to exclude the publisher from receiving the event.

        :returns: exclude_me flag
        :rtype: None or bool
        """
        if self._exclude_me is None and self._from_fbs:
            self._exclude_me = self._from_fbs.ExcludeMe()
        return self._exclude_me

    @exclude_me.setter
    def exclude_me(self, value):
        assert value is None or type(value) == bool
        self._exclude_me = value

    #
    # exclude, exclude_authid, exclude_authrole
    #

    @property
    def exclude(self):
        """
        List of WAMP session IDs to exclude from receiving this event.

        :returns: list of excluded session IDs
        :rtype: list[int]
        """
        if self._exclude is None and self._from_fbs:
            if self._from_fbs.ExcludeLength():
                exclude = []
                for j in range(self._from_fbs.ExcludeLength()):
                    exclude.append(self._from_fbs.Exclude(j))
                self._exclude = exclude
        return self._exclude

    @exclude.setter
    def exclude(self, value):
        assert value is None or type(value) == list
        if value:
            for x in value:
                assert type(x) == int
        self._exclude = value

    @property
    def exclude_authid(self):
        """
        List of WAMP authids to exclude from receiving this event.

        :returns: list of excluded authids
        :rtype: list[str]
        """
        if self._exclude_authid is None and self._from_fbs:
            if self._from_fbs.ExcludeAuthidLength():
                exclude_authid = []
                for j in range(self._from_fbs.ExcludeAuthidLength()):
                    exclude_authid.append(self._from_fbs.ExcludeAuthid(j).decode('utf8'))
                self._exclude_authid = exclude_authid
        return self._exclude_authid

    @exclude_authid.setter
    def exclude_authid(self, value):
        assert value is None or type(value) == list
        if value:
            for x in value:
                assert type(x) == str
        self._exclude_authid = value

    @property
    def exclude_authrole(self):
        """
        List of WAMP authroles to exclude from receiving this event.

        :returns: list of excluded authroles
        :rtype: list[str]
        """
        if self._exclude_authrole is None and self._from_fbs:
            if self._from_fbs.ExcludeAuthroleLength():
                exclude_authrole = []
                for j in range(self._from_fbs.ExcludeAuthroleLength()):
                    exclude_authrole.append(self._from_fbs.ExcludeAuthrole(j).decode('utf8'))
                self._exclude_authrole = exclude_authrole
        return self._exclude_authrole

    @exclude_authrole.setter
    def exclude_authrole(self, value):
        assert value is None or type(value) == list
        if value:
            for x in value:
                assert type(x) == str
        self._exclude_authrole = value

    #
    # eligible, eligible_authid, eligible_authrole
    #

    @property
    def eligible(self):
        """
        List of WAMP session IDs eligible to receive this event.

        :returns: list of eligible session IDs
        :rtype: list[int]
        """
        if self._eligible is None and self._from_fbs:
            if self._from_fbs.EligibleLength():
                eligible = []
                for j in range(self._from_fbs.EligibleLength()):
                    eligible.append(self._from_fbs.Eligible(j))
                self._eligible = eligible
        return self._eligible

    @eligible.setter
    def eligible(self, value):
        assert value is None or type(value) == list
        if value:
            for x in value:
                assert type(x) == int
        self._eligible = value

    @property
    def eligible_authid(self):
        """
        List of WAMP authids eligible to receive this event.

        :returns: list of eligible authids
        :rtype: list[str]
        """
        if self._eligible_authid is None and self._from_fbs:
            if self._from_fbs.EligibleAuthidLength():
                eligible_authid = []
                for j in range(self._from_fbs.EligibleAuthidLength()):
                    eligible_authid.append(self._from_fbs.EligibleAuthid(j).decode('utf8'))
                self._eligible_authid = eligible_authid
        return self._eligible_authid

    @eligible_authid.setter
    def eligible_authid(self, value):
        assert value is None or type(value) == list
        if value:
            for x in value:
                assert type(x) == str
        self._eligible_authid = value

    @property
    def eligible_authrole(self):
        """
        List of WAMP authroles eligible to receive this event.

        :returns: list of eligible authroles
        :rtype: list[str]
        """
        if self._eligible_authrole is None and self._from_fbs:
            if self._from_fbs.EligibleAuthroleLength():
                eligible_authrole = []
                for j in range(self._from_fbs.EligibleAuthroleLength()):
                    eligible_authrole.append(self._from_fbs.EligibleAuthrole(j).decode('utf8'))
                self._eligible_authrole = eligible_authrole
        return self._eligible_authrole

    @eligible_authrole.setter
    def eligible_authrole(self, value):
        assert value is None or type(value) == list
        if value:
            for x in value:
                assert type(x) == str
        self._eligible_authrole = value

    #
    # encryption
    #

    @property
    def enc_algo(self):
        """
        When using payload transparency, the encoding algorithm that was used to encode the payload.

        :returns: payload encryption algorithm
        :rtype: int
        """
        if self._enc_algo is None and self._from_fbs:
            self._enc_algo = self._from_fbs.EncAlgo()
        return self._enc_algo

    @enc_algo.setter
    def enc_algo(self, value):
        assert value is None or value in [self.ENC_ALGO_CRYPTOBOX, self.ENC_ALGO_MQTT, self.ENC_ALGO_XBR]
        self._enc_algo = value

    @property
    def enc_key(self):
        """
        When using payload transparency with an encryption algorithm, the payload encryption key.

        :returns: payload key
        :rtype: None or bytes
        """
        if self._enc_key is None and self._from_fbs:
            if self._from_fbs.EncKeyLength():
                self._enc_key = self._from_fbs.EncKeyAsBytes()
        return self._enc_key

    @enc_key.setter
    def enc_key(self, value):
        assert value is None or type(value) == bytes
        self._enc_key = value

    @property
    def enc_serializer(self):
        """
        When using payload transparency, the payload object serializer that was used encoding the payload.

        :returns: payload serializer
        :rtype: int
        """
        if self._enc_serializer is None and self._from_fbs:
            self._enc_serializer = self._from_fbs.EncSerializer()
        return self._enc_serializer

    @enc_serializer.setter
    def enc_serializer(self, value):
        assert value is None or value in [
            self.ENC_SER_JSON, self.ENC_SER_MSGPACK, self.ENC_SER_CBOR, self.ENC_SER_UBJSON
        ]
        self._enc_serializer = value

    @staticmethod
    def cast(buf):
        return Publication(_Publication.GetRootAsPublication(buf, 0))

    def build(self, builder):

        args = self.args
        if args:
            args = builder.CreateString(cbor2.dumps(args))

        kwargs = self.kwargs
        if kwargs:
            kwargs = builder.CreateString(cbor2.dumps(kwargs))

        payload = self.payload
        if payload:
            payload = builder.CreateString(payload)

        topic = self.topic
        if topic:
            topic = builder.CreateString(topic)

        enc_key = self.enc_key
        if enc_key:
            enc_key = builder.CreateString(enc_key)

        # exclude: [int]
        exclude = self.exclude
        if exclude:
            PublicationGen.PublicationStartExcludeAuthidVector(builder, len(exclude))
            for session in reversed(exclude):
                builder.PrependUint64(session)
            exclude = builder.EndVector(len(exclude))

        # exclude_authid: [string]
        exclude_authid = self.exclude_authid
        if exclude_authid:
            _exclude_authid = []
            for authid in exclude_authid:
                _exclude_authid.append(builder.CreateString(authid))
            PublicationGen.PublicationStartExcludeAuthidVector(builder, len(_exclude_authid))
            for o in reversed(_exclude_authid):
                builder.PrependUOffsetTRelative(o)
            exclude_authid = builder.EndVector(len(_exclude_authid))

        # exclude_authrole: [string]
        exclude_authrole = self.exclude_authrole
        if exclude_authid:
            _exclude_authrole = []
            for authrole in exclude_authrole:
                _exclude_authrole.append(builder.CreateString(authrole))
            PublicationGen.PublicationStartExcludeAuthroleVector(builder, len(_exclude_authrole))
            for o in reversed(_exclude_authrole):
                builder.PrependUOffsetTRelative(o)
            exclude_authrole = builder.EndVector(len(_exclude_authrole))

        # eligible: [int]
        eligible = self.eligible
        if eligible:
            PublicationGen.PublicationStartEligibleAuthidVector(builder, len(eligible))
            for session in reversed(eligible):
                builder.PrependUint64(session)
            eligible = builder.EndVector(len(eligible))

        # eligible_authid: [string]
        eligible_authid = self.eligible_authid
        if eligible_authid:
            _eligible_authid = []
            for authid in eligible_authid:
                _eligible_authid.append(builder.CreateString(authid))
            PublicationGen.PublicationStartEligibleAuthidVector(builder, len(_eligible_authid))
            for o in reversed(_eligible_authid):
                builder.PrependUOffsetTRelative(o)
            eligible_authid = builder.EndVector(len(_eligible_authid))

        # eligible_authrole: [string]
        eligible_authrole = self.eligible_authrole
        if eligible_authrole:
            _eligible_authrole = []
            for authrole in eligible_authrole:
                _eligible_authrole.append(builder.CreateString(authrole))
            PublicationGen.PublicationStartEligibleAuthroleVector(builder, len(_eligible_authrole))
            for o in reversed(_eligible_authrole):
                builder.PrependUOffsetTRelative(o)
            eligible_authrole = builder.EndVector(len(_eligible_authrole))

        # now start and build a new object ..
        PublicationGen.PublicationStart(builder)

        if self.timestamp:
            PublicationGen.PublicationAddTimestamp(builder, self.timestamp)
        if self.publication:
            PublicationGen.PublicationAddPublication(builder, self.publication)
        if self.publisher:
            PublicationGen.PublicationAddPublisher(builder, self.publisher)

        if topic:
            PublicationGen.PublicationAddTopic(builder, topic)

        if args:
            PublicationGen.PublicationAddArgs(builder, args)
        if kwargs:
            PublicationGen.PublicationAddKwargs(builder, kwargs)
        if payload is not None:
            PublicationGen.PublicationAddPayload(builder, payload)

        if self.acknowledge is not None:
            PublicationGen.PublicationAddAcknowledge(builder, self.acknowledge)
        if self.retain is not None:
            PublicationGen.PublicationAddRetain(builder, self.retain)
        if self.exclude_me is not None:
            PublicationGen.PublicationAddExcludeMe(builder, self.exclude_me)

        if exclude:
            PublicationGen.PublicationAddExclude(builder, exclude)
        if exclude_authid:
            PublicationGen.PublicationAddExcludeAuthid(builder, exclude_authid)
        if exclude_authrole:
            PublicationGen.PublicationAddExcludeAuthrole(builder, exclude_authrole)

        if eligible:
            PublicationGen.PublicationAddEligible(builder, eligible)
        if eligible_authid:
            PublicationGen.PublicationAddEligibleAuthid(builder, eligible_authid)
        if eligible_authrole:
            PublicationGen.PublicationAddEligibleAuthrole(builder, eligible_authrole)

        if self.enc_algo:
            PublicationGen.PublicationAddEncAlgo(builder, self.enc_algo)
        if enc_key:
            PublicationGen.PublicationAddEncKey(builder, enc_key)
        if self.enc_serializer:
            PublicationGen.PublicationAddEncSerializer(builder, self.enc_serializer)

        # finish the object.
        final = PublicationGen.PublicationEnd(builder)

        return final
