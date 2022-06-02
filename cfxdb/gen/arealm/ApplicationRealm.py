# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# WAMP application realms defined.
class ApplicationRealm(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ApplicationRealm()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsApplicationRealm(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ApplicationRealm
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this object.
    # ApplicationRealm
    def Oid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Time when the object was created.
    # ApplicationRealm
    def Created(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Owner organization of this object.
    # ApplicationRealm
    def Owner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Name of this application realm (must be unique within the management realm at any given point in time).
    # ApplicationRealm
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # When dispatching events to receivers, batch sending in chunks of this many events (not all at once).
    # ApplicationRealm
    def EventDispatchingChunkSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # URI check level to enforce by the router.
    # ApplicationRealm
    def UriCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Enable the WAMP meta API on the application realm.
    # ApplicationRealm
    def EnableMetaApi(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Bridge the WAMP meta API from the application realm to the management realm, so that it can be tapped into.
    # ApplicationRealm
    def BridgeMetaApi(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def ApplicationRealmStart(builder): builder.StartObject(8)
def Start(builder):
    return ApplicationRealmStart(builder)
def ApplicationRealmAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def AddOid(builder, oid):
    return ApplicationRealmAddOid(builder, oid)
def ApplicationRealmAddCreated(builder, created): builder.PrependUint64Slot(1, created, 0)
def AddCreated(builder, created):
    return ApplicationRealmAddCreated(builder, created)
def ApplicationRealmAddOwner(builder, owner): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(owner), 0)
def AddOwner(builder, owner):
    return ApplicationRealmAddOwner(builder, owner)
def ApplicationRealmAddName(builder, name): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return ApplicationRealmAddName(builder, name)
def ApplicationRealmAddEventDispatchingChunkSize(builder, eventDispatchingChunkSize): builder.PrependUint32Slot(4, eventDispatchingChunkSize, 0)
def AddEventDispatchingChunkSize(builder, eventDispatchingChunkSize):
    return ApplicationRealmAddEventDispatchingChunkSize(builder, eventDispatchingChunkSize)
def ApplicationRealmAddUriCheck(builder, uriCheck): builder.PrependInt8Slot(5, uriCheck, 0)
def AddUriCheck(builder, uriCheck):
    return ApplicationRealmAddUriCheck(builder, uriCheck)
def ApplicationRealmAddEnableMetaApi(builder, enableMetaApi): builder.PrependBoolSlot(6, enableMetaApi, 0)
def AddEnableMetaApi(builder, enableMetaApi):
    return ApplicationRealmAddEnableMetaApi(builder, enableMetaApi)
def ApplicationRealmAddBridgeMetaApi(builder, bridgeMetaApi): builder.PrependBoolSlot(7, bridgeMetaApi, 0)
def AddBridgeMetaApi(builder, bridgeMetaApi):
    return ApplicationRealmAddBridgeMetaApi(builder, bridgeMetaApi)
def ApplicationRealmEnd(builder): return builder.EndObject()
def End(builder):
    return ApplicationRealmEnd(builder)