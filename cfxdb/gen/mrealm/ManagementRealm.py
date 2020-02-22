# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mrealm

import flatbuffers

class ManagementRealm(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsManagementRealm(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ManagementRealm()
        x.Init(buf, n + offset)
        return x

    # ManagementRealm
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// ID of this object.
    # ManagementRealm
    def Oid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

# /// Label for this object (not interpreted by CFC).
    # ManagementRealm
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

# /// Description for this object (not interpreted by CFC).
    # ManagementRealm
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

# /// Tags on this object.
    # ManagementRealm
    def Tags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # ManagementRealm
    def TagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Name of this management realm (must be globally unique within CFC at any given point in time).
    # ManagementRealm
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

# /// Time when the management realm was created.
    # ManagementRealm
    def Created(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

# /// Owner organization of this management realm.
    # ManagementRealm
    def Owner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

# /// CFC hosting node for this management realm.
    # ManagementRealm
    def CfNode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

# /// CFC hosting router worker for this management realm.
    # ManagementRealm
    def CfRouterWorker(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

# /// CFC hosting container worker for this management realm.
    # ManagementRealm
    def CfContainerWorker(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ManagementRealmStart(builder): builder.StartObject(10)
def ManagementRealmAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def ManagementRealmAddLabel(builder, label): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0)
def ManagementRealmAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def ManagementRealmAddTags(builder, tags): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(tags), 0)
def ManagementRealmStartTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ManagementRealmAddName(builder, name): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def ManagementRealmAddCreated(builder, created): builder.PrependUint64Slot(5, created, 0)
def ManagementRealmAddOwner(builder, owner): builder.PrependStructSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(owner), 0)
def ManagementRealmAddCfNode(builder, cfNode): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(cfNode), 0)
def ManagementRealmAddCfRouterWorker(builder, cfRouterWorker): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(cfRouterWorker), 0)
def ManagementRealmAddCfContainerWorker(builder, cfContainerWorker): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(cfContainerWorker), 0)
def ManagementRealmEnd(builder): return builder.EndObject()
