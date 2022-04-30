##############################################################################
#
#                        Crossbar.io Database
#     Copyright (c) Crossbar.io Technologies GmbH. Licensed under MIT.
#
##############################################################################

import uuid
import cbor2
from typing import Optional, Dict, Any
import pprint

import flatbuffers
import numpy as np

from cfxdb.gen.realmstore import AppSession as AppSessionGen


class _AppSessionGen(AppSessionGen.AppSession):
    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _AppSessionGen()
        x.Init(buf, n + offset)
        return x

    def OidAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def NodeOidAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def TransportAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def AuthextraAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class AppSession(object):
    """
    Persisted session database object.
    """

    __slots__ = (
        '_from_fbs',
        '_oid',
        '_session',
        '_joined_at',
        '_left_at',
        '_node_oid',
        '_node_authid',
        '_worker_name',
        '_transport',
        '_realm',
        '_authid',
        '_authrole',
        '_authmethod',
        '_authprovider',
        '_authextra',
    )

    def __init__(self, from_fbs: Optional[_AppSessionGen] = None):
        self._from_fbs = from_fbs

        # [uint8] (uuid)
        self._oid: Optional[uuid.UUID] = None

        # uint64
        self._session: Optional[int] = None

        # uint64 (timestamp)
        self._joined_at: Optional[np.datetime64] = None

        # uint64 (timestamp)
        self._left_at: Optional[np.datetime64] = None

        # [uint8] (uuid)
        self._node_oid: Optional[uuid.UUID] = None

        # string
        self._node_authid: Optional[str] = None

        # string
        self._worker_name: Optional[str] = None

        # [uint8] (cbor)
        self._transport: Optional[Dict[str, Any]] = None

        # string
        self._realm: Optional[str] = None

        # string
        self._authid: Optional[str] = None

        # string
        self._authrole: Optional[str] = None

        # string
        self._authmethod: Optional[str] = None

        # string
        self._authprovider: Optional[str] = None

        # [uint8] (cbor)
        self._authextra: Optional[Dict[str, Any]] = None

    def marshal(self):
        obj = {
            'oid': self.oid.bytes if self.oid else None,
            'session': self.session,
            'joined_at': int(self.joined_at) if self.joined_at else None,
            'left_at': int(self.left_at) if self.left_at else None,
            'node_oid': self.node_oid.bytes if self.node_oid else None,
            'node_authid': self.node_authid,
            'worker_name': self.worker_name,
            'transport': self.transport,
            'realm': self.realm,
            'authid': self.authid,
            'authrole': self.authrole,
            'authmethod': self.authmethod,
            'authprovider': self.authprovider,
            'authextra': self.authextra,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def oid(self) -> Optional[uuid.UUID]:
        """
        Unlimited time, globally unique, long-term session object ID. The pair ``(session, joined_at)`` maps bidirectionally to ``session_oid``.
        """
        if self._oid is None and self._from_fbs:
            if self._from_fbs.OidLength():
                _oid = self._from_fbs.OidAsBytes()
                self._oid = uuid.UUID(bytes=bytes(_oid))
        return self._oid

    @oid.setter
    def oid(self, value: Optional[uuid.UUID]):
        assert value is None or isinstance(value, uuid.UUID)
        self._oid = value

    @property
    def session(self) -> Optional[int]:
        """
        The WAMP session_id of the session.
        """
        if self._session is None and self._from_fbs:
            self._session = self._from_fbs.Session()
        return self._session

    @session.setter
    def session(self, value: Optional[int]):
        assert value is None or type(value) == int
        self._session = value

    @property
    def joined_at(self) -> Optional[np.datetime64]:
        """
        Timestamp when the session was joined by the router. Epoch time in ns.
        """
        if self._joined_at is None and self._from_fbs:
            self._joined_at = np.datetime64(self._from_fbs.JoinedAt(), 'ns')
        return self._joined_at

    @joined_at.setter
    def joined_at(self, value: Optional[np.datetime64]):
        assert value is None or isinstance(value, np.datetime64)
        self._joined_at = value

    @property
    def left_at(self) -> Optional[np.datetime64]:
        """
        Timestamp when the session left the router. Epoch time in ns.
        """
        if self._left_at is None and self._from_fbs:
            self._left_at = np.datetime64(self._from_fbs.LeftAt(), 'ns')
        return self._left_at

    @left_at.setter
    def left_at(self, value: Optional[np.datetime64]):
        assert value is None or isinstance(value, np.datetime64)
        self._left_at = value

    @property
    def node_oid(self) -> Optional[uuid.UUID]:
        """
        OID of the node of the router worker hosting this session.
        """
        if self._node_oid is None and self._from_fbs:
            if self._from_fbs.NodeOidLength():
                _node_oid = self._from_fbs.NodeOidAsBytes()
                self._node_oid = uuid.UUID(bytes=bytes(_node_oid))
        return self._node_oid

    @node_oid.setter
    def node_oid(self, value: Optional[uuid.UUID]):
        assert value is None or isinstance(value, uuid.UUID)
        self._node_oid = value

    @property
    def node_authid(self) -> Optional[str]:
        """
        Name (management realm WAMP authid) of the node of the router worker hosting this session.
        """
        if self._node_authid is None and self._from_fbs:
            _node_authid = self._from_fbs.NodeAuthid()
            if _node_authid:
                self._node_authid = _node_authid.decode('utf8')
        return self._node_authid

    @node_authid.setter
    def node_authid(self, value: Optional[str]):
        self._node_authid = value

    @property
    def worker_name(self) -> Optional[str]:
        """
        Local worker name of the router worker hosting this session.
        """
        if self._worker_name is None and self._from_fbs:
            _worker_name = self._from_fbs.WorkerName()
            if _worker_name:
                self._worker_name = _worker_name.decode('utf8')
        return self._worker_name

    @worker_name.setter
    def worker_name(self, value: Optional[str]):
        self._worker_name = value

    @property
    def transport(self) -> Optional[Dict[str, Any]]:
        """
        Session transport information.
        """
        if self._transport is None and self._from_fbs:
            _transport = self._from_fbs.TransportAsBytes()
            if _transport:
                self._transport = cbor2.loads(_transport)
            else:
                self._transport = {}
        return self._transport

    @transport.setter
    def transport(self, value: Optional[Dict[str, Any]]):
        assert value is None or type(value) == dict
        self._transport = value

    @property
    def realm(self) -> Optional[str]:
        """
        The WAMP realm the session is/was joined on.
        """
        if self._realm is None and self._from_fbs:
            self._realm = self._from_fbs.Realm().decode('utf8')
        return self._realm

    @realm.setter
    def realm(self, value: Optional[str]):
        assert value is None or type(value) == str
        self._realm = value

    @property
    def authid(self) -> Optional[str]:
        """
        The WAMP authid the session was authenticated under.
        """
        if self._authid is None and self._from_fbs:
            _authid = self._from_fbs.Authid()
            if _authid:
                self._authid = _authid.decode('utf8')
        return self._authid

    @authid.setter
    def authid(self, value: Optional[str]):
        self._authid = value

    @property
    def authrole(self) -> Optional[str]:
        """
        The WAMP authrole the session was authenticated under.
        """
        if self._authrole is None and self._from_fbs:
            _authrole = self._from_fbs.Authrole()
            if _authrole:
                self._authrole = _authrole.decode('utf8')
        return self._authrole

    @authrole.setter
    def authrole(self, value: Optional[str]):
        self._authrole = value

    @property
    def authmethod(self) -> Optional[str]:
        """
        The WAMP authmethod uses to authenticate the session.
        """
        if self._authmethod is None and self._from_fbs:
            _authmethod = self._from_fbs.Authmethod()
            if _authmethod:
                self._authmethod = _authmethod.decode('utf8')
        return self._authmethod

    @authmethod.setter
    def authmethod(self, value: Optional[str]):
        self._authmethod = value

    @property
    def authprovider(self) -> Optional[str]:
        """
        The WAMP authprovider that was handling the session authentication.
        """
        if self._authprovider is None and self._from_fbs:
            _authprovider = self._from_fbs.Authprovider()
            if _authprovider:
                self._authprovider = _authprovider.decode('utf8')
        return self._authprovider

    @authprovider.setter
    def authprovider(self, value: Optional[str]):
        self._authprovider = value

    @property
    def authextra(self) -> Optional[Dict[str, Any]]:
        """
        The WAMP authextra as provided to the authenticated session.
        """
        if self._authextra is None and self._from_fbs:
            _authextra = self._from_fbs.AuthextraAsBytes()
            if _authextra:
                self._authextra = cbor2.loads(_authextra)
            else:
                self._authextra = {}
        return self._authextra

    @authextra.setter
    def authextra(self, value: Optional[Dict[str, Any]]):
        assert value is None or type(value) == dict
        self._authextra = value

    @staticmethod
    def cast(buf) -> 'AppSession':
        return AppSession(_AppSessionGen.GetRootAsAppSession(buf, 0))

    def build(self, builder):

        oid = self.oid.bytes if self.oid else None
        if oid:
            oid = builder.CreateString(oid)

        node_oid = self.node_oid.bytes if self.node_oid else None
        if node_oid:
            node_oid = builder.CreateString(node_oid)

        node_authid = self.node_authid
        if node_authid:
            node_authid = builder.CreateString(node_authid)

        worker_name = self.worker_name
        if worker_name:
            worker_name = builder.CreateString(worker_name)

        transport = self.transport
        if transport:
            transport = builder.CreateString(cbor2.dumps(transport))

        realm = self.realm
        if realm:
            realm = builder.CreateString(realm)

        authid = self.authid
        if authid:
            authid = builder.CreateString(authid)

        authrole = self.authrole
        if authrole:
            authrole = builder.CreateString(authrole)

        authmethod = self.authmethod
        if authmethod:
            authmethod = builder.CreateString(authmethod)

        authprovider = self.authprovider
        if authprovider:
            authprovider = builder.CreateString(authprovider)

        authextra = self.authextra
        if authextra:
            authextra = builder.CreateString(cbor2.dumps(authextra))

        AppSessionGen.AppSessionStart(builder)

        if oid:
            AppSessionGen.AppSessionAddOid(builder, oid)

        if self.session:
            AppSessionGen.AppSessionAddSession(builder, self.session)

        if self.joined_at:
            AppSessionGen.AppSessionAddJoinedAt(builder, int(self.joined_at))

        if self.left_at:
            AppSessionGen.AppSessionAddLeftAt(builder, int(self.left_at))

        if node_oid:
            AppSessionGen.AppSessionAddNodeOid(builder, node_oid)

        if node_authid:
            AppSessionGen.AppSessionAddNodeAuthid(builder, node_authid)

        if worker_name:
            AppSessionGen.AppSessionAddWorkerName(builder, worker_name)

        if transport:
            AppSessionGen.AppSessionAddTransport(builder, transport)

        if realm:
            AppSessionGen.AppSessionAddRealm(builder, realm)

        if authid:
            AppSessionGen.AppSessionAddAuthid(builder, authid)

        if authrole:
            AppSessionGen.AppSessionAddAuthrole(builder, authrole)

        if authmethod:
            AppSessionGen.AppSessionAddAuthmethod(builder, authmethod)

        if authprovider:
            AppSessionGen.AppSessionAddAuthprovider(builder, authprovider)

        if authextra:
            AppSessionGen.AppSessionAddAuthextra(builder, authextra)

        final = AppSessionGen.AppSessionEnd(builder)

        return final
