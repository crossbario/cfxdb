# automatically generated by the FlatBuffers compiler, do not modify

# namespace: reflection

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Service(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Service()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsService(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def ServiceBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x42\x46\x42\x53", size_prefixed=size_prefixed)

    # Service
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Service
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Service
    def Calls(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from reflection.RPCCall import RPCCall
            obj = RPCCall()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Service
    def CallsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Service
    def CallsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Service
    def Attributes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from reflection.KeyValue import KeyValue
            obj = KeyValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Service
    def AttributesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Service
    def AttributesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Service
    def Documentation(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Service
    def DocumentationLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Service
    def DocumentationIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def Start(builder): builder.StartObject(4)
def ServiceStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def ServiceAddName(builder, name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, name)
def AddCalls(builder, calls): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(calls), 0)
def ServiceAddCalls(builder, calls):
    """This method is deprecated. Please switch to AddCalls."""
    return AddCalls(builder, calls)
def StartCallsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ServiceStartCallsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartCallsVector(builder, numElems)
def AddAttributes(builder, attributes): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(attributes), 0)
def ServiceAddAttributes(builder, attributes):
    """This method is deprecated. Please switch to AddAttributes."""
    return AddAttributes(builder, attributes)
def StartAttributesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ServiceStartAttributesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartAttributesVector(builder, numElems)
def AddDocumentation(builder, documentation): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(documentation), 0)
def ServiceAddDocumentation(builder, documentation):
    """This method is deprecated. Please switch to AddDocumentation."""
    return AddDocumentation(builder, documentation)
def StartDocumentationVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ServiceStartDocumentationVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartDocumentationVector(builder, numElems)
def End(builder): return builder.EndObject()
def ServiceEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)