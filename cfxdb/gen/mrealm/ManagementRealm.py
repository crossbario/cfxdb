# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mrealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ManagementRealm(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ManagementRealm()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsManagementRealm(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ManagementRealm
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this object.
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

    # Label for this object (not interpreted by CFC).
    # ManagementRealm
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Description for this object (not interpreted by CFC).
    # ManagementRealm
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Tags on this object.
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

    # ManagementRealm
    def TagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Name of this management realm (must be globally unique within CFC at any given point in time).
    # ManagementRealm
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Time when the management realm was created.
    # ManagementRealm
    def Created(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Owner organization of this management realm.
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

    # CFC hosting node for this management realm.
    # ManagementRealm
    def CfNode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CFC hosting router worker for this management realm.
    # ManagementRealm
    def CfRouterWorker(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CFC hosting container worker for this management realm.
    # ManagementRealm
    def CfContainerWorker(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ManagementRealmStart(builder): builder.StartObject(10)
def Start(builder):
    return ManagementRealmStart(builder)
def ManagementRealmAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def AddOid(builder, oid):
    return ManagementRealmAddOid(builder, oid)
def ManagementRealmAddLabel(builder, label): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0)
def AddLabel(builder, label):
    return ManagementRealmAddLabel(builder, label)
def ManagementRealmAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def AddDescription(builder, description):
    return ManagementRealmAddDescription(builder, description)
def ManagementRealmAddTags(builder, tags): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(tags), 0)
def AddTags(builder, tags):
    return ManagementRealmAddTags(builder, tags)
def ManagementRealmStartTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartTagsVector(builder, numElems):
    return ManagementRealmStartTagsVector(builder, numElems)
def ManagementRealmAddName(builder, name): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return ManagementRealmAddName(builder, name)
def ManagementRealmAddCreated(builder, created): builder.PrependUint64Slot(5, created, 0)
def AddCreated(builder, created):
    return ManagementRealmAddCreated(builder, created)
def ManagementRealmAddOwner(builder, owner): builder.PrependStructSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(owner), 0)
def AddOwner(builder, owner):
    return ManagementRealmAddOwner(builder, owner)
def ManagementRealmAddCfNode(builder, cfNode): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(cfNode), 0)
def AddCfNode(builder, cfNode):
    return ManagementRealmAddCfNode(builder, cfNode)
def ManagementRealmAddCfRouterWorker(builder, cfRouterWorker): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(cfRouterWorker), 0)
def AddCfRouterWorker(builder, cfRouterWorker):
    return ManagementRealmAddCfRouterWorker(builder, cfRouterWorker)
def ManagementRealmAddCfContainerWorker(builder, cfContainerWorker): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(cfContainerWorker), 0)
def AddCfContainerWorker(builder, cfContainerWorker):
    return ManagementRealmAddCfContainerWorker(builder, cfContainerWorker)
def ManagementRealmEnd(builder): return builder.EndObject()
def End(builder):
    return ManagementRealmEnd(builder)