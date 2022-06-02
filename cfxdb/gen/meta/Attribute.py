# automatically generated by the FlatBuffers compiler, do not modify

# namespace: meta

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Generic **meta data attributes** for objects in other tables. Primary key of this table is ``(table_oid, object_oid, attribute)``.
class Attribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Attribute()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAttribute(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Attribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Table of the object holding the attribute.
    # Attribute
    def TableOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Attribute
    def TableOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Attribute
    def TableOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def TableOidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Object (within the table) holding the attribute.
    # Attribute
    def ObjectOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Attribute
    def ObjectOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Attribute
    def ObjectOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def ObjectOidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Attribute name (part of the key).
    # Attribute
    def Attribute(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Timestamp when the attribute was last modified (or first created).
    # Attribute
    def Modified(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # CBOR-serialized, object-valued attribute.
    # Attribute
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Attribute
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Attribute
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def ValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def AttributeStart(builder): builder.StartObject(5)
def Start(builder):
    return AttributeStart(builder)
def AttributeAddTableOid(builder, tableOid): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(tableOid), 0)
def AddTableOid(builder, tableOid):
    return AttributeAddTableOid(builder, tableOid)
def AttributeStartTableOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartTableOidVector(builder, numElems):
    return AttributeStartTableOidVector(builder, numElems)
def AttributeAddObjectOid(builder, objectOid): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(objectOid), 0)
def AddObjectOid(builder, objectOid):
    return AttributeAddObjectOid(builder, objectOid)
def AttributeStartObjectOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartObjectOidVector(builder, numElems):
    return AttributeStartObjectOidVector(builder, numElems)
def AttributeAddAttribute(builder, attribute): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(attribute), 0)
def AddAttribute(builder, attribute):
    return AttributeAddAttribute(builder, attribute)
def AttributeAddModified(builder, modified): builder.PrependUint64Slot(3, modified, 0)
def AddModified(builder, modified):
    return AttributeAddModified(builder, modified)
def AttributeAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def AddValue(builder, value):
    return AttributeAddValue(builder, value)
def AttributeStartValueVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartValueVector(builder, numElems):
    return AttributeStartValueVector(builder, numElems)
def AttributeEnd(builder): return builder.EndObject()
def End(builder):
    return AttributeEnd(builder)