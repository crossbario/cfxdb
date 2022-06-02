# automatically generated by the FlatBuffers compiler, do not modify

# namespace: xbr

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# XBR Markets.
class Market(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Market()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMarket(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Market
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # The unique ID of the market.
    # Market
    def Market(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def MarketAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def MarketLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def MarketIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Database transaction time (epoch time in ns) of insert or last update.
    # Market
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Block number (on the blockchain) when the actor (originally) joined the market.
    # Market
    def Created(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def CreatedAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def CreatedLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def CreatedIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Global market sequence number.
    # Market
    def Seq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Market owner.
    # Market
    def Owner(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def OwnerAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def OwnerLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def OwnerIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # Market coin used as means of payment.
    # Market
    def Coin(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def CoinAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def CoinLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def CoinIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # The XBR market terms set by the market owner. IPFS Multihash pointing to a ZIP archive file with market documents.
    # Market
    def Terms(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The XBR market metadata published by the market owner. IPFS Multihash pointing to a RDF/Turtle file with market metadata.
    # Market
    def Meta(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The address of the XBR market maker that will run this market. The delegate of the market owner.
    # Market
    def Maker(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def MakerAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def MakerLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def MakerIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # The amount of XBR tokens a XBR provider joining the market must deposit.
    # Market
    def ProviderSecurity(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def ProviderSecurityAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def ProviderSecurityLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def ProviderSecurityIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # The amount of XBR tokens a XBR consumer joining the market must deposit.
    # Market
    def ConsumerSecurity(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def ConsumerSecurityAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def ConsumerSecurityLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def ConsumerSecurityIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # The fee taken by the market (beneficiary is the market owner). The fee is a percentage of the revenue of the XBR Provider that receives XBR Token paid for transactions. The fee must be between 0% (inclusive) and 99% (inclusive), and is expressed as a fraction of the total supply of XBR tokens.
    # Market
    def MarketFee(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def MarketFeeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def MarketFeeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def MarketFeeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # Transaction hash of the transaction this change was committed to the blockchain under.
    # Market
    def Tid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def TidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def TidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def TidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # When signed off-chain and submitted via ``XBRMarket.createMarketFor``.
    # Market
    def Signature(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Market
    def SignatureAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Market
    def SignatureLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Market
    def SignatureIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

def MarketStart(builder): builder.StartObject(14)
def Start(builder):
    return MarketStart(builder)
def MarketAddMarket(builder, market): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(market), 0)
def AddMarket(builder, market):
    return MarketAddMarket(builder, market)
def MarketStartMarketVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartMarketVector(builder, numElems):
    return MarketStartMarketVector(builder, numElems)
def MarketAddTimestamp(builder, timestamp): builder.PrependUint64Slot(1, timestamp, 0)
def AddTimestamp(builder, timestamp):
    return MarketAddTimestamp(builder, timestamp)
def MarketAddCreated(builder, created): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(created), 0)
def AddCreated(builder, created):
    return MarketAddCreated(builder, created)
def MarketStartCreatedVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartCreatedVector(builder, numElems):
    return MarketStartCreatedVector(builder, numElems)
def MarketAddSeq(builder, seq): builder.PrependUint32Slot(3, seq, 0)
def AddSeq(builder, seq):
    return MarketAddSeq(builder, seq)
def MarketAddOwner(builder, owner): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(owner), 0)
def AddOwner(builder, owner):
    return MarketAddOwner(builder, owner)
def MarketStartOwnerVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartOwnerVector(builder, numElems):
    return MarketStartOwnerVector(builder, numElems)
def MarketAddCoin(builder, coin): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(coin), 0)
def AddCoin(builder, coin):
    return MarketAddCoin(builder, coin)
def MarketStartCoinVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartCoinVector(builder, numElems):
    return MarketStartCoinVector(builder, numElems)
def MarketAddTerms(builder, terms): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(terms), 0)
def AddTerms(builder, terms):
    return MarketAddTerms(builder, terms)
def MarketAddMeta(builder, meta): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(meta), 0)
def AddMeta(builder, meta):
    return MarketAddMeta(builder, meta)
def MarketAddMaker(builder, maker): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(maker), 0)
def AddMaker(builder, maker):
    return MarketAddMaker(builder, maker)
def MarketStartMakerVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartMakerVector(builder, numElems):
    return MarketStartMakerVector(builder, numElems)
def MarketAddProviderSecurity(builder, providerSecurity): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(providerSecurity), 0)
def AddProviderSecurity(builder, providerSecurity):
    return MarketAddProviderSecurity(builder, providerSecurity)
def MarketStartProviderSecurityVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartProviderSecurityVector(builder, numElems):
    return MarketStartProviderSecurityVector(builder, numElems)
def MarketAddConsumerSecurity(builder, consumerSecurity): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(consumerSecurity), 0)
def AddConsumerSecurity(builder, consumerSecurity):
    return MarketAddConsumerSecurity(builder, consumerSecurity)
def MarketStartConsumerSecurityVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartConsumerSecurityVector(builder, numElems):
    return MarketStartConsumerSecurityVector(builder, numElems)
def MarketAddMarketFee(builder, marketFee): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(marketFee), 0)
def AddMarketFee(builder, marketFee):
    return MarketAddMarketFee(builder, marketFee)
def MarketStartMarketFeeVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartMarketFeeVector(builder, numElems):
    return MarketStartMarketFeeVector(builder, numElems)
def MarketAddTid(builder, tid): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(tid), 0)
def AddTid(builder, tid):
    return MarketAddTid(builder, tid)
def MarketStartTidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartTidVector(builder, numElems):
    return MarketStartTidVector(builder, numElems)
def MarketAddSignature(builder, signature): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(signature), 0)
def AddSignature(builder, signature):
    return MarketAddSignature(builder, signature)
def MarketStartSignatureVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartSignatureVector(builder, numElems):
    return MarketStartSignatureVector(builder, numElems)
def MarketEnd(builder): return builder.EndObject()
def End(builder):
    return MarketEnd(builder)