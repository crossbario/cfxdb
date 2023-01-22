##############################################################################
#
#                        Crossbar.io Database
#     Copyright (c) typedef int GmbH. Licensed under MIT.
#
##############################################################################

import pprint
import uuid

import flatbuffers
import numpy as np
from cfxdb.gen.xbrnetwork import UserKey as UserKeyGen
from zlmdb import table, MapBytes32FlatBuffers, MapUuidTimestampBytes32


class _UserKeyGen(UserKeyGen.UserKey):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsUserKey(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _UserKeyGen()
        x.Init(buf, n + offset)
        return x

    def PubkeyAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def OwnerAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class UserKey(object):
    """
    User client (public) keys.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        # User key - a Ed25519 public key - for authenticating using WAMP-cryptosign.
        # [uint8] (uint256)
        self._pubkey = None

        # Timestamp (epoch time in ns) of initial creation of this record.
        # uint64 (timestamp)
        self._created = None

        # ID of user account this user key is owned by.
        # [uint8] (uuid)
        self._owner = None

    def marshal(self):
        obj = {
            'pubkey': bytes(self.pubkey),
            'created': int(self.created),
            'owner': self.owner.bytes,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def pubkey(self) -> bytes:
        """
        User key - a Ed25519 public key - for authenticating using WAMP-cryptosign.
        """
        if self._pubkey is None and self._from_fbs:
            if self._from_fbs.PubkeyLength():
                self._pubkey = self._from_fbs.PubkeyAsBytes()
        return self._pubkey

    @pubkey.setter
    def pubkey(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 32)
        self._pubkey = value

    @property
    def created(self) -> np.datetime64:
        """
        Timestamp (epoch time in ns) of initial creation of this record.
        """
        if self._created is None and self._from_fbs:
            self._created = np.datetime64(self._from_fbs.Created(), 'ns')
        return self._created

    @created.setter
    def created(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._created = value

    @property
    def owner(self) -> uuid.UUID:
        """
        ID of user account this user key is owned by.
        """
        if self._owner is None and self._from_fbs:
            if self._from_fbs.OwnerLength():
                _owner = self._from_fbs.OwnerAsBytes()
                self._owner = uuid.UUID(bytes=bytes(_owner))
            else:
                self._owner = uuid.UUID(bytes=b'\x00' * 20)
        return self._owner

    @owner.setter
    def owner(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._owner = value

    @staticmethod
    def cast(buf):
        return UserKey(_UserKeyGen.GetRootAsUserKey(buf, 0))

    def build(self, builder):

        owner = self.owner.bytes if self.owner else None
        if owner:
            owner = builder.CreateString(owner)

        pubkey = self.pubkey
        if pubkey:
            pubkey = builder.CreateString(pubkey)

        UserKeyGen.UserKeyStart(builder)

        if pubkey:
            UserKeyGen.UserKeyAddPubkey(builder, pubkey)

        if self.created:
            UserKeyGen.UserKeyAddCreated(builder, int(self.created))

        if owner:
            UserKeyGen.UserKeyAddOwner(builder, owner)

        final = UserKeyGen.UserKeyEnd(builder)

        return final


@table('5b5d0ce7-33f4-4421-a6ab-ed77cafc763a', build=UserKey.build, cast=UserKey.cast)
class UserKeys(MapBytes32FlatBuffers):
    """
    Database table for user client keys.
    """
    @staticmethod
    def parse(data):
        """

        :param data:
        :return:
        """
        pubkey = None
        if 'pubkey' in data:
            assert type(data['pubkey']) == bytes and len(data['pubkey']) == 32
            pubkey = data['pubkey']

        created = None
        if 'created' in data:
            assert type(data['created'] == int)
            created = np.datetime64(data['created'], 'ns')

        owner = None
        if 'owner' in data:
            assert type(data['owner'] == bytes and len(data['owner']) == 16)
            owner = uuid.UUID(bytes=data['owner'])

        obj = UserKey()
        obj.pubkey = pubkey
        obj.created = created
        obj.owner = owner

        return obj


@table('68b736f8-27df-4e3e-b80f-1b855ae5596f')
class IndexUserKeyByAccount(MapUuidTimestampBytes32):
    """
    Database (index) table for (member_oid, created) -> userkey mapping.
    """
