# automatically generated by the FlatBuffers compiler, do not modify

# namespace: xbr

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# This table stores XBRToken._balances state.
class TokenBalance(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TokenBalance()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTokenBalance(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TokenBalance
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Primary key: XBR token owner address.
    # TokenBalance
    def OwnerAddress(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # TokenBalance
    def OwnerAddressAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # TokenBalance
    def OwnerAddressLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TokenBalance
    def OwnerAddressIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # XBR token owned.
    # TokenBalance
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # TokenBalance
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # TokenBalance
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TokenBalance
    def ValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def TokenBalanceStart(builder):
    builder.StartObject(2)

def Start(builder):
    TokenBalanceStart(builder)

def TokenBalanceAddOwnerAddress(builder, ownerAddress):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(ownerAddress), 0)

def AddOwnerAddress(builder, ownerAddress):
    TokenBalanceAddOwnerAddress(builder, ownerAddress)

def TokenBalanceStartOwnerAddressVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartOwnerAddressVector(builder, numElems: int) -> int:
    return TokenBalanceStartOwnerAddressVector(builder, numElems)

def TokenBalanceAddValue(builder, value):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)

def AddValue(builder, value):
    TokenBalanceAddValue(builder, value)

def TokenBalanceStartValueVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartValueVector(builder, numElems: int) -> int:
    return TokenBalanceStartValueVector(builder, numElems)

def TokenBalanceEnd(builder):
    return builder.EndObject()

def End(builder):
    return TokenBalanceEnd(builder)
