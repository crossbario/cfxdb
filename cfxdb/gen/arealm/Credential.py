# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# WAMP client authentication credentials, used for mapping ``(authmethod, realm, authid) -> principal``.
class Credential(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Credential()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCredential(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Credential
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this credential.
    # Credential
    def Oid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WAMP authentication method offered by the authenticating client.
    # Credential
    def Authmethod(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # WAMP realm requested by the authenticating client.
    # Credential
    def Realm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WAMP authid announced by the authenticating client.
    # Credential
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Authentication method specific configuration (CBOR serialized).
    # Credential
    def Authconfig(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Credential
    def AuthconfigAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Credential
    def AuthconfigLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Credential
    def AuthconfigIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # ID of the principal this credential resolves to upon successful authentication.
    # Credential
    def PrincipalOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def CredentialStart(builder): builder.StartObject(6)
def Start(builder):
    return CredentialStart(builder)
def CredentialAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def AddOid(builder, oid):
    return CredentialAddOid(builder, oid)
def CredentialAddAuthmethod(builder, authmethod): builder.PrependInt8Slot(1, authmethod, 0)
def AddAuthmethod(builder, authmethod):
    return CredentialAddAuthmethod(builder, authmethod)
def CredentialAddRealm(builder, realm): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(realm), 0)
def AddRealm(builder, realm):
    return CredentialAddRealm(builder, realm)
def CredentialAddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def AddAuthid(builder, authid):
    return CredentialAddAuthid(builder, authid)
def CredentialAddAuthconfig(builder, authconfig): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(authconfig), 0)
def AddAuthconfig(builder, authconfig):
    return CredentialAddAuthconfig(builder, authconfig)
def CredentialStartAuthconfigVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartAuthconfigVector(builder, numElems):
    return CredentialStartAuthconfigVector(builder, numElems)
def CredentialAddPrincipalOid(builder, principalOid): builder.PrependStructSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(principalOid), 0)
def AddPrincipalOid(builder, principalOid):
    return CredentialAddPrincipalOid(builder, principalOid)
def CredentialEnd(builder): return builder.EndObject()
def End(builder):
    return CredentialEnd(builder)