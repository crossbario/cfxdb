##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint

import flatbuffers
from cfxdb import unpack_uint256, pack_uint256
from cfxdb.gen.xbr import ChannelType as ChannelTypeGen, ChannelState as ChannelStateGen, \
    Channel as ChannelGen, ChannelBalance as ChannelBalanceGen
from zlmdb import table, MapBytes20FlatBuffers, MapBytes20TimestampBytes20

ChannelType = ChannelTypeGen.ChannelType
ChannelState = ChannelStateGen.ChannelState


class _ChannelGen(ChannelGen.Channel):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsChannel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _ChannelGen()
        x.Init(buf, n + offset)
        return x

    def ChannelAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def MarketAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def SenderAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def DelegateAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def RecipientAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def AmountAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def OpenAtAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def ClosingAtAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def ClosedAtAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def CloseMmSigAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def CloseDelSigAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def CloseBalanceAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def ClosedTxAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class Channel(object):
    """
    ``XBRChannel`` record/event database object.

    XBR payment channel (from XBR consumer to XBR market maker) and XBR paying channels (from XBR market maker to XBR provider).
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        self._type = None
        self._channel = None
        self._market = None
        self._sender = None
        self._delegate = None
        self._recipient = None
        self._amount = None
        self._timeout = None
        self._state = None
        self._open_at = None
        self._closing_at = None
        self._closed_at = None

        self._close_mm_sig = None
        self._close_del_sig = None
        self._close_channel_seq = None
        self._close_balance = None
        self._close_is_final = None

        self._closed_tx = None

    def marshal(self) -> dict:
        obj = {
            'type': self.type,
            'channel': bytes(self.channel) if self.channel else None,
            'market': bytes(self.market) if self.market else None,
            'sender': bytes(self.sender) if self.sender else None,
            'delegate': bytes(self.delegate) if self.delegate else None,
            'recipient': bytes(self.recipient) if self.recipient else None,
            'amount': pack_uint256(self.amount) if self.amount else 0,
            'timeout': self.timeout,
            'state': self.state,
            'open_at': self.open_at,
            'closing_at': self.closing_at,
            'closed_at': self.closed_at,
            'close_mm_sig': bytes(self.close_mm_sig) if self.close_mm_sig else None,
            'close_del_sig': bytes(self.close_del_sig) if self.close_del_sig else None,
            'close_channel_seq': self.close_channel_seq,
            'close_is_final': self.close_is_final,
            'close_balance': self.close_balance,
            'closed_tx': bytes(self.closed_tx) if self.closed_tx else None,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def type(self) -> int:
        """
        Channel type: payment channel (from XBR consumer to XBR market maker) or paying channel (from XBR market maker to XBR provider).
        """
        if self._type is None and self._from_fbs:
            self._type = self._from_fbs.Type()
        return self._type

    @type.setter
    def type(self, value: int):
        assert type(value) == int
        self._type = value

    @property
    def channel(self) -> bytes:
        """
        ID of the payment channel.
        """
        if self._channel is None and self._from_fbs:
            if self._from_fbs.ChannelLength():
                self._channel = self._from_fbs.ChannelAsBytes()
        return self._channel

    @channel.setter
    def channel(self, value: bytes):
        assert value is None or type(value) == bytes
        self._channel = value

    @property
    def market(self) -> bytes:
        """
        ID of the market this payment channel is associated with.
        """
        if self._market is None and self._from_fbs:
            if self._from_fbs.MarketLength():
                self._market = self._from_fbs.MarketAsBytes()
        return self._market

    @market.setter
    def market(self, value: bytes):
        assert value is None or type(value) == bytes
        self._market = value

    @property
    def sender(self) -> bytes:
        """
        Ethereum address of the sender (either XBR Consumer or XBR Market).
        """
        if self._sender is None and self._from_fbs:
            if self._from_fbs.SenderLength():
                self._sender = self._from_fbs.SenderAsBytes()
        return self._sender

    @sender.setter
    def sender(self, value: bytes):
        assert value is None or type(value) == bytes
        self._sender = value

    @property
    def delegate(self) -> bytes:
        """
        Ethereum address of the sender delegate (either XBR Consumer delegate or XBR Market delegate == market maker)
        """
        if self._delegate is None and self._from_fbs:
            if self._from_fbs.DelegateLength():
                self._delegate = self._from_fbs.DelegateAsBytes()
        return self._delegate

    @delegate.setter
    def delegate(self, value: bytes):
        assert value is None or type(value) == bytes
        self._delegate = value

    @property
    def recipient(self) -> bytes:
        """
        Ethereum address of the recipient (either XBR Market or XBR Provider)
        """
        if self._recipient is None and self._from_fbs:
            if self._from_fbs.RecipientLength():
                self._recipient = self._from_fbs.RecipientAsBytes()
        return self._recipient

    @recipient.setter
    def recipient(self, value: bytes):
        assert value is None or type(value) == bytes
        self._recipient = value

    @property
    def amount(self) -> int:
        """
        Amount of XBR tokens initially deposited into the payment channel.
        """
        if self._amount is None and self._from_fbs:
            if self._from_fbs.AmountLength():
                _amount = self._from_fbs.AmountAsBytes()
                self._amount = unpack_uint256(bytes(_amount))
            else:
                self._amount = 0
        return self._amount

    @amount.setter
    def amount(self, value: int):
        assert value is None or type(value) == int
        self._amount = value

    @property
    def timeout(self) -> int:
        """
        Payment channel (non-cooperative) closed timeout in blocks (on the blockchain).
        """
        if self._timeout is None and self._from_fbs:
            self._timeout = self._from_fbs.Timeout()
        return self._timeout

    @timeout.setter
    def timeout(self, value: int):
        assert type(value) == int
        self._timeout = value

    @property
    def state(self) -> int:
        """
        Current state of payment channel.
        """
        if self._state is None and self._from_fbs:
            self._state = self._from_fbs.State()
        return self._state

    @state.setter
    def state(self, value: int):
        assert type(value) == int
        self._state = value

    @property
    def open_at(self) -> int:
        """
        Block number (on the blockchain) when the payment channel was opened.
        """
        if self._open_at is None and self._from_fbs:
            if self._from_fbs.OpenAtLength():
                _open_at = self._from_fbs.OpenAtAsBytes()
                self._open_at = unpack_uint256(bytes(_open_at))
            else:
                self._open_at = 0
        return self._open_at

    @open_at.setter
    def open_at(self, value: int):
        assert value is None or type(value) == int
        self._open_at = value

    @property
    def closing_at(self) -> int:
        """
        Block number (on the blockchain) when the payment channel will close (at the latest).
        """
        if self._closing_at is None and self._from_fbs:
            if self._from_fbs.ClosingAtLength():
                _closing_at = self._from_fbs.ClosingAtAsBytes()
                self._closing_at = unpack_uint256(bytes(_closing_at))
            else:
                self._closed_at = 0
        return self._closing_at

    @closing_at.setter
    def closing_at(self, value: int):
        assert value is None or type(value) == int
        self._closing_at = value

    @property
    def closed_at(self) -> int:
        """
        Block number (on the blockchain) when the payment channel was finally closed.
        """
        if self._closed_at is None and self._from_fbs:
            if self._from_fbs.ClosedAtLength():
                _closed_at = self._from_fbs.ClosedAtAsBytes()
                self._closed_at = unpack_uint256(bytes(_closed_at))
            else:
                self._closed_at = 0
        return self._closed_at

    @closed_at.setter
    def closed_at(self, value: int):
        assert value is None or type(value) == int
        self._closed_at = value

    @property
    def close_mm_sig(self) -> int:
        """
        Closing signature by market maker.
        """
        if self._close_mm_sig is None and self._from_fbs:
            if self._from_fbs.CloseMmSigLength():
                self._close_mm_sig = self._from_fbs.CloseMmSigAsBytes()
        return self._close_mm_sig

    @close_mm_sig.setter
    def close_mm_sig(self, value: int):
        assert value is None or type(value) == bytes
        self._close_mm_sig = value

    @property
    def close_del_sig(self) -> bytes:
        """
        Closing signature by (seller or buyer) delegate.
        """
        if self._close_del_sig is None and self._from_fbs:
            if self._from_fbs.CloseDelSigLength():
                self._close_del_sig = self._from_fbs.CloseDelSigAsBytes()
        return self._close_del_sig

    @close_del_sig.setter
    def close_del_sig(self, value: bytes):
        assert value is None or type(value) == bytes
        self._close_del_sig = value

    @property
    def close_channel_seq(self) -> int:
        """
        Last off-chain, closing transaction: channel transaction sequence number.
        """
        if self._close_channel_seq is None and self._from_fbs:
            self._close_channel_seq = self._from_fbs.CloseChannelSeq()
        return self._close_channel_seq

    @close_channel_seq.setter
    def close_channel_seq(self, value: int):
        assert type(value) == int
        self._close_channel_seq = value

    @property
    def close_balance(self) -> int:
        """
        Remaining (closing) channel balance (XBR).
        """
        if self._close_balance is None and self._from_fbs:
            if self._from_fbs.CloseBalanceLength():
                _close_balance = self._from_fbs.CloseBalanceAsBytes()
                if _close_balance is not None:
                    self._close_balance = unpack_uint256(bytes(_close_balance))
                else:
                    self._close_balance = 0
            else:
                self._close_balance = 0
        return self._close_balance

    @close_balance.setter
    def close_balance(self, value: int):
        assert value is None or type(value) == int
        self._close_balance = value

    @property
    def close_is_final(self) -> bool:
        """
        Flag indication if close is final (happens immediately without a channel timeout).
        """
        if self._close_is_final is None and self._from_fbs:
            self._close_is_final = (self._from_fbs.CloseIsFinal() is True)
        return self._close_is_final

    @close_is_final.setter
    def close_is_final(self, value: bool):
        assert value is None or type(value) == bool
        self._close_is_final = value

    @property
    def closed_tx(self) -> bytes:
        """
        When channel was finally closed on-chain, the Ethereum transaction ID.
        """
        if self._closed_tx is None and self._from_fbs:
            if self._from_fbs.ClosedTxLength():
                self._closed_tx = self._from_fbs.ClosedTxAsBytes()
        return self._closed_tx

    @closed_tx.setter
    def closed_tx(self, value: bytes):
        assert value is None or type(value) == bytes
        self._closed_tx = value

    @staticmethod
    def cast(buf):
        return Channel(_ChannelGen.GetRootAsChannel(buf, 0))

    def build(self, builder):

        channel = self.channel
        if channel:
            channel = builder.CreateString(bytes(channel))

        market = self.market
        if market:
            market = builder.CreateString(bytes(market))

        sender = self.sender
        if sender:
            sender = builder.CreateString(bytes(sender))

        delegate = self.delegate
        if delegate:
            delegate = builder.CreateString(bytes(delegate))

        recipient = self.recipient
        if recipient:
            recipient = builder.CreateString(bytes(recipient))

        amount = self.amount
        if amount:
            amount = builder.CreateString(pack_uint256(amount))

        open_at = self.open_at
        if open_at:
            open_at = builder.CreateString(pack_uint256(open_at))

        closing_at = self.closing_at
        if closing_at:
            closing_at = builder.CreateString(pack_uint256(closing_at))

        closed_at = self.closed_at
        if closed_at:
            closed_at = builder.CreateString(pack_uint256(closed_at))

        close_mm_sig = self.close_mm_sig
        if close_mm_sig:
            close_mm_sig = builder.CreateString(bytes(close_mm_sig))

        close_del_sig = self.close_del_sig
        if close_del_sig:
            close_del_sig = builder.CreateString(bytes(close_del_sig))

        close_balance = self.close_balance
        if close_balance:
            close_balance = builder.CreateString(pack_uint256(close_balance))

        closed_tx = self.closed_tx
        if closed_tx:
            closed_tx = builder.CreateString(bytes(closed_tx))

        ChannelGen.ChannelStart(builder)

        if self.type:
            ChannelGen.ChannelAddType(builder, int(self.type))

        if channel:
            ChannelGen.ChannelAddChannel(builder, channel)

        if market:
            ChannelGen.ChannelAddMarket(builder, market)

        if sender:
            ChannelGen.ChannelAddSender(builder, sender)

        if delegate:
            ChannelGen.ChannelAddDelegate(builder, delegate)

        if recipient:
            ChannelGen.ChannelAddRecipient(builder, recipient)

        if amount:
            ChannelGen.ChannelAddAmount(builder, amount)

        ChannelGen.ChannelAddTimeout(builder, self.timeout)

        if self.state:
            ChannelGen.ChannelAddState(builder, int(self.state))

        if open_at:
            ChannelGen.ChannelAddOpenAt(builder, open_at)

        if closing_at:
            ChannelGen.ChannelAddClosingAt(builder, closing_at)

        if closed_at:
            ChannelGen.ChannelAddClosedAt(builder, closed_at)

        if close_mm_sig:
            ChannelGen.ChannelAddCloseMmSig(builder, close_mm_sig)

        if close_del_sig:
            ChannelGen.ChannelAddCloseDelSig(builder, close_del_sig)

        if self.close_channel_seq:
            ChannelGen.ChannelAddCloseChannelSeq(builder, self.close_channel_seq)

        if close_balance:
            ChannelGen.ChannelAddCloseBalance(builder, close_balance)

        if self.close_is_final:
            ChannelGen.ChannelAddCloseIsFinal(builder, self.close_is_final)

        if closed_tx:
            ChannelGen.ChannelAddClosedTx(builder, closed_tx)

        final = ChannelGen.ChannelEnd(builder)

        return final


@table('b3d01946-85ae-49f3-ad96-b78194eb82fe', build=Channel.build, cast=Channel.cast)
class PaymentChannels(MapBytes20FlatBuffers):
    """
    XBR payment channels by ``payment_channel_adr``.

    Map :class:`zlmdb.MapBytes20FlatBuffers` from ``payment_channel_adr`` to :class:`cfxdb.xbr.Channel`
    """


@table('cffd5253-72f8-41a9-8b76-5e6ff3654e67')
class IndexPaymentChannelByDelegate(MapBytes20TimestampBytes20):
    """
    Index: ``(delegate_adr, created_timestamp) -> payment_channel_adr``
    """


@table('4e7e7c8d-db0d-4dea-8409-ac8f21ce1e10', build=Channel.build, cast=Channel.cast)
class PayingChannels(MapBytes20FlatBuffers):
    """
    XBR paying channels by ``paying_channel_adr``.

    Map :class:`zlmdb.MapBytes32FlatBuffers` from ``paying_channel_adr`` to :class:`cfxdb.xbr.Channel`
    """


@table('cee954be-fdb2-43cc-8891-529d6c7a0c3b')
class IndexPayingChannelByDelegate(MapBytes20TimestampBytes20):
    """
    Index: ``(delegate_adr, created_timestamp) -> paying_channel_adr``
    """


@table('655a9d5f-0bdf-4c2a-8102-208f6da4a566')
class IndexPayingChannelByRecipient(MapBytes20TimestampBytes20):
    """
    Index: ``(recipient_adr, created_timestamp) -> paying_channel_adr``
    """


class _ChannelBalanceGen(ChannelBalanceGen.ChannelBalance):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsChannelBalance(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _ChannelBalanceGen()
        x.Init(buf, n + offset)
        return x

    def RemainingAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def InflightAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class ChannelBalance(object):
    """
    XBR payment channel current (off-chain) balance. The sum of ``Balance.remaining`` and ``Balance.inflight`` equals ``Channel.amount``.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        self._remaining = None
        self._inflight = None
        self._seq = None

    @staticmethod
    def parse(data: dict):
        assert type(data) == dict

        obj = ChannelBalance()

        if 'remaining' in data:
            remaining = data['remaining']
            assert type(remaining) == bytes and len(remaining) == 32
            obj._remaining = unpack_uint256(remaining)

        if 'inflight' in data:
            inflight = data['inflight']
            assert type(inflight) == bytes and len(inflight) == 32
            obj._inflight = unpack_uint256(inflight)

        if 'seq' in data:
            seq = data['seq']
            assert type(seq) == int
            obj._seq = unpack_uint256(seq)

        return obj

    def marshal(self) -> dict:
        obj = {
            'remaining': pack_uint256(self.remaining) if self.remaining else 0,
            'inflight': pack_uint256(self.inflight) if self.inflight else 0,
            'seq': self.seq or 0
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def remaining(self) -> int:
        """
        Amount of XBR tokens currently remaining in the payment channel.
        """
        if self._remaining is None and self._from_fbs:
            if self._from_fbs.RemainingLength():
                _remaining = self._from_fbs.RemainingAsBytes()
                self._remaining = unpack_uint256(bytes(_remaining))
            else:
                self._remaining = 0
        return self._remaining

    @remaining.setter
    def remaining(self, value: int):
        assert value is None or type(value) == int
        self._remaining = value

    @property
    def inflight(self) -> int:
        """
        Amount of XBR tokens reserved to in-flight purchase transactions.
        """
        if self._inflight is None and self._from_fbs:
            if self._from_fbs.InflightLength():
                _inflight = self._from_fbs.InflightAsBytes()
                self._inflight = unpack_uint256(bytes(_inflight))
            else:
                self._inflight = 0
        return self._inflight

    @inflight.setter
    def inflight(self, value: int):
        assert value is None or type(value) == int
        self._inflight = value

    @property
    def seq(self) -> int:
        """
        Sequence number of transactions on this balance starting from 0 when the payment channel is created.
        """
        if self._seq is None and self._from_fbs:
            self._seq = self._from_fbs.Seq()
        return self._seq or 0

    @seq.setter
    def seq(self, value: int):
        assert value is None or type(value) == int
        self._seq = value

    @staticmethod
    def cast(buf):
        return ChannelBalance(_ChannelBalanceGen.GetRootAsChannelBalance(buf, 0))

    def build(self, builder):

        remaining = self.remaining
        if remaining:
            remaining = builder.CreateString(pack_uint256(remaining))

        inflight = self.inflight
        if inflight:
            inflight = builder.CreateString(pack_uint256(inflight))

        ChannelBalanceGen.ChannelBalanceStart(builder)

        if remaining:
            ChannelBalanceGen.ChannelBalanceAddRemaining(builder, remaining)

        if inflight:
            ChannelBalanceGen.ChannelBalanceAddInflight(builder, inflight)

        if self.seq:
            ChannelBalanceGen.ChannelBalanceAddSeq(builder, self.seq)

        final = ChannelBalanceGen.ChannelBalanceEnd(builder)

        return final


@table('878ac002-a830-488b-bfe9-f06371b8eecb', build=ChannelBalance.build, cast=ChannelBalance.cast)
class PaymentChannelBalances(MapBytes20FlatBuffers):
    """
    XBR payment channels current balances by ``payment_channel_adr``.

    Map :class:`zlmdb.MapBytes20FlatBuffers` from ``payment_channel_adr`` to :class:`cfxdb.xbr.Balance`
    """


@table('c0931d5d-6d5d-4f9c-b2a3-29664a0f4c07', build=ChannelBalance.build, cast=ChannelBalance.cast)
class PayingChannelBalances(MapBytes20FlatBuffers):
    """
    XBR paying channels current balances by ``paying_channel_adr``.

    Map :class:`zlmdb.MapBytes20FlatBuffers` from ``paying_channel_adr`` to :class:`cfxdb.xbr.Balance`
    """
