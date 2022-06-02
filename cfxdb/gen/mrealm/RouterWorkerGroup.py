# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mrealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RouterWorkerGroup(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RouterWorkerGroup()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsRouterWorkerGroup(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # RouterWorkerGroup
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this object.
    # RouterWorkerGroup
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
    # RouterWorkerGroup
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Description for this object (not interpreted by CFC).
    # RouterWorkerGroup
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Tags on this object.
    # RouterWorkerGroup
    def Tags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # RouterWorkerGroup
    def TagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # RouterWorkerGroup
    def TagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Unique user assigned name.
    # RouterWorkerGroup
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Current status of worker group.
    # RouterWorkerGroup
    def Status(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def RouterWorkerGroupStart(builder): builder.StartObject(6)
def Start(builder):
    return RouterWorkerGroupStart(builder)
def RouterWorkerGroupAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def AddOid(builder, oid):
    return RouterWorkerGroupAddOid(builder, oid)
def RouterWorkerGroupAddLabel(builder, label): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0)
def AddLabel(builder, label):
    return RouterWorkerGroupAddLabel(builder, label)
def RouterWorkerGroupAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def AddDescription(builder, description):
    return RouterWorkerGroupAddDescription(builder, description)
def RouterWorkerGroupAddTags(builder, tags): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(tags), 0)
def AddTags(builder, tags):
    return RouterWorkerGroupAddTags(builder, tags)
def RouterWorkerGroupStartTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartTagsVector(builder, numElems):
    return RouterWorkerGroupStartTagsVector(builder, numElems)
def RouterWorkerGroupAddName(builder, name): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return RouterWorkerGroupAddName(builder, name)
def RouterWorkerGroupAddStatus(builder, status): builder.PrependUint8Slot(5, status, 0)
def AddStatus(builder, status):
    return RouterWorkerGroupAddStatus(builder, status)
def RouterWorkerGroupEnd(builder): return builder.EndObject()
def End(builder):
    return RouterWorkerGroupEnd(builder)