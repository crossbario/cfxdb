# automatically generated by the FlatBuffers compiler, do not modify

# namespace: realmstore

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# This table store WAMP events dispatched to receivers, under WAMP subscriptions on URIs (or patterns).
class Event(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Event()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEvent(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Event
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Timestamp when the event was sent to the receiver. Epoch time in ns.
    # Event
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # The subscription ID this event is dispatched under.
    # Event
    def Subscription(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # The publication ID of the dispatched event.
    # Event
    def Publication(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # The WAMP session ID of the receiver.
    # Event
    def Receiver(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Whether the message was retained by the broker on the topic, rather than just published.
    # Event
    def Retained(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Whether this Event was to be acknowledged by the receiver.
    # Event
    def AcknowledgedDelivery(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def EventStart(builder):
    builder.StartObject(6)

def Start(builder):
    EventStart(builder)

def EventAddTimestamp(builder, timestamp):
    builder.PrependUint64Slot(0, timestamp, 0)

def AddTimestamp(builder, timestamp):
    EventAddTimestamp(builder, timestamp)

def EventAddSubscription(builder, subscription):
    builder.PrependUint64Slot(1, subscription, 0)

def AddSubscription(builder, subscription):
    EventAddSubscription(builder, subscription)

def EventAddPublication(builder, publication):
    builder.PrependUint64Slot(2, publication, 0)

def AddPublication(builder, publication):
    EventAddPublication(builder, publication)

def EventAddReceiver(builder, receiver):
    builder.PrependUint64Slot(3, receiver, 0)

def AddReceiver(builder, receiver):
    EventAddReceiver(builder, receiver)

def EventAddRetained(builder, retained):
    builder.PrependBoolSlot(4, retained, 0)

def AddRetained(builder, retained):
    EventAddRetained(builder, retained)

def EventAddAcknowledgedDelivery(builder, acknowledgedDelivery):
    builder.PrependBoolSlot(5, acknowledgedDelivery, 0)

def AddAcknowledgedDelivery(builder, acknowledgedDelivery):
    EventAddAcknowledgedDelivery(builder, acknowledgedDelivery)

def EventEnd(builder):
    return builder.EndObject()

def End(builder):
    return EventEnd(builder)
