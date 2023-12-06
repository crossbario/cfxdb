# automatically generated by the FlatBuffers compiler, do not modify

# namespace: log

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Heartbeat log record of managed nodes. Primary key: (timestamp, node_id).
class MNodeLog(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MNodeLog()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMNodeLog(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MNodeLog
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Primary key: Unix time in ns when this log record was received (from CFC node clock).
    # MNodeLog
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Primary key: CF node ID.
    # MNodeLog
    def NodeId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # MNodeLog
    def NodeIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # MNodeLog
    def NodeIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MNodeLog
    def NodeIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Heartbeat period in seconds encompassed by this record.
    # MNodeLog
    def Period(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Management realm ID.
    # MNodeLog
    def MrealmId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # MNodeLog
    def MrealmIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # MNodeLog
    def MrealmIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MNodeLog
    def MrealmIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Current state of CF node.
    # MNodeLog
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # WAMP session ID of the CF node uplink management session to this CFC instance.
    # MNodeLog
    def Session(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Unix time in ns. This timestamp is from the original received event payload (from CF node clock).
    # MNodeLog
    def Sent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Sequence number as sent in the log record by the CF node (started at 0 for CF start and incremented by one on each heartbeat).
    # MNodeLog
    def Seq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Number of controllers running in the CF node (this is always 1).
    # MNodeLog
    def Controllers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of router workers currently running in the CF node.
    # MNodeLog
    def Routers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of container workers currently running in the CF node.
    # MNodeLog
    def Containers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of guest workers currently running in the CF node.
    # MNodeLog
    def Guests(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of proxy workers currently running in the CF node.
    # MNodeLog
    def Proxies(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of XBR market maker workers currently running in the CF node.
    # MNodeLog
    def Marketmakers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of hostmonitor workers currently running in the CF node (this is usually either 0 or 1).
    # MNodeLog
    def Hostmonitors(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # CF node system statistics.
    # MNodeLog
    def CpuCtxSwitches(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def CpuFreq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuGuest(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuGuestNice(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuIdle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuInterrupts(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def CpuIowait(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuIrq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuNice(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuSoftInterrupts(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def CpuSoftirq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuSteal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuSystem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuUser(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def DiskBusyTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskReadBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskReadCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskReadMergedCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskReadTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskWriteBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskWriteCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskWriteMergedCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskWriteTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryActive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryAvailable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryBuffers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryCached(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryFree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryInactive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryPercent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def MemoryShared(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemorySlab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryTotal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryUsed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkBytesRecv(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkBytesSent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkConnectionAfInet(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkConnectionAfInet6(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkConnectionAfUnix(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkDropin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkDropout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkErrin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkErrout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkPacketsRecv(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkPacketsSent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

def MNodeLogStart(builder):
    builder.StartObject(60)

def Start(builder):
    MNodeLogStart(builder)

def MNodeLogAddTimestamp(builder, timestamp):
    builder.PrependUint64Slot(0, timestamp, 0)

def AddTimestamp(builder, timestamp):
    MNodeLogAddTimestamp(builder, timestamp)

def MNodeLogAddNodeId(builder, nodeId):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(nodeId), 0)

def AddNodeId(builder, nodeId):
    MNodeLogAddNodeId(builder, nodeId)

def MNodeLogStartNodeIdVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartNodeIdVector(builder, numElems: int) -> int:
    return MNodeLogStartNodeIdVector(builder, numElems)

def MNodeLogAddPeriod(builder, period):
    builder.PrependUint32Slot(2, period, 0)

def AddPeriod(builder, period):
    MNodeLogAddPeriod(builder, period)

def MNodeLogAddMrealmId(builder, mrealmId):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(mrealmId), 0)

def AddMrealmId(builder, mrealmId):
    MNodeLogAddMrealmId(builder, mrealmId)

def MNodeLogStartMrealmIdVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartMrealmIdVector(builder, numElems: int) -> int:
    return MNodeLogStartMrealmIdVector(builder, numElems)

def MNodeLogAddState(builder, state):
    builder.PrependUint8Slot(4, state, 0)

def AddState(builder, state):
    MNodeLogAddState(builder, state)

def MNodeLogAddSession(builder, session):
    builder.PrependUint64Slot(5, session, 0)

def AddSession(builder, session):
    MNodeLogAddSession(builder, session)

def MNodeLogAddSent(builder, sent):
    builder.PrependUint64Slot(6, sent, 0)

def AddSent(builder, sent):
    MNodeLogAddSent(builder, sent)

def MNodeLogAddSeq(builder, seq):
    builder.PrependUint64Slot(7, seq, 0)

def AddSeq(builder, seq):
    MNodeLogAddSeq(builder, seq)

def MNodeLogAddControllers(builder, controllers):
    builder.PrependUint16Slot(8, controllers, 0)

def AddControllers(builder, controllers):
    MNodeLogAddControllers(builder, controllers)

def MNodeLogAddRouters(builder, routers):
    builder.PrependUint16Slot(9, routers, 0)

def AddRouters(builder, routers):
    MNodeLogAddRouters(builder, routers)

def MNodeLogAddContainers(builder, containers):
    builder.PrependUint16Slot(10, containers, 0)

def AddContainers(builder, containers):
    MNodeLogAddContainers(builder, containers)

def MNodeLogAddGuests(builder, guests):
    builder.PrependUint16Slot(11, guests, 0)

def AddGuests(builder, guests):
    MNodeLogAddGuests(builder, guests)

def MNodeLogAddProxies(builder, proxies):
    builder.PrependUint16Slot(12, proxies, 0)

def AddProxies(builder, proxies):
    MNodeLogAddProxies(builder, proxies)

def MNodeLogAddMarketmakers(builder, marketmakers):
    builder.PrependUint16Slot(13, marketmakers, 0)

def AddMarketmakers(builder, marketmakers):
    MNodeLogAddMarketmakers(builder, marketmakers)

def MNodeLogAddHostmonitors(builder, hostmonitors):
    builder.PrependUint16Slot(14, hostmonitors, 0)

def AddHostmonitors(builder, hostmonitors):
    MNodeLogAddHostmonitors(builder, hostmonitors)

def MNodeLogAddCpuCtxSwitches(builder, cpuCtxSwitches):
    builder.PrependUint64Slot(15, cpuCtxSwitches, 0)

def AddCpuCtxSwitches(builder, cpuCtxSwitches):
    MNodeLogAddCpuCtxSwitches(builder, cpuCtxSwitches)

def MNodeLogAddCpuFreq(builder, cpuFreq):
    builder.PrependFloat32Slot(16, cpuFreq, 0.0)

def AddCpuFreq(builder, cpuFreq):
    MNodeLogAddCpuFreq(builder, cpuFreq)

def MNodeLogAddCpuGuest(builder, cpuGuest):
    builder.PrependFloat32Slot(17, cpuGuest, 0.0)

def AddCpuGuest(builder, cpuGuest):
    MNodeLogAddCpuGuest(builder, cpuGuest)

def MNodeLogAddCpuGuestNice(builder, cpuGuestNice):
    builder.PrependFloat32Slot(18, cpuGuestNice, 0.0)

def AddCpuGuestNice(builder, cpuGuestNice):
    MNodeLogAddCpuGuestNice(builder, cpuGuestNice)

def MNodeLogAddCpuIdle(builder, cpuIdle):
    builder.PrependFloat32Slot(19, cpuIdle, 0.0)

def AddCpuIdle(builder, cpuIdle):
    MNodeLogAddCpuIdle(builder, cpuIdle)

def MNodeLogAddCpuInterrupts(builder, cpuInterrupts):
    builder.PrependUint64Slot(20, cpuInterrupts, 0)

def AddCpuInterrupts(builder, cpuInterrupts):
    MNodeLogAddCpuInterrupts(builder, cpuInterrupts)

def MNodeLogAddCpuIowait(builder, cpuIowait):
    builder.PrependFloat32Slot(21, cpuIowait, 0.0)

def AddCpuIowait(builder, cpuIowait):
    MNodeLogAddCpuIowait(builder, cpuIowait)

def MNodeLogAddCpuIrq(builder, cpuIrq):
    builder.PrependFloat32Slot(22, cpuIrq, 0.0)

def AddCpuIrq(builder, cpuIrq):
    MNodeLogAddCpuIrq(builder, cpuIrq)

def MNodeLogAddCpuNice(builder, cpuNice):
    builder.PrependFloat32Slot(23, cpuNice, 0.0)

def AddCpuNice(builder, cpuNice):
    MNodeLogAddCpuNice(builder, cpuNice)

def MNodeLogAddCpuSoftInterrupts(builder, cpuSoftInterrupts):
    builder.PrependUint64Slot(24, cpuSoftInterrupts, 0)

def AddCpuSoftInterrupts(builder, cpuSoftInterrupts):
    MNodeLogAddCpuSoftInterrupts(builder, cpuSoftInterrupts)

def MNodeLogAddCpuSoftirq(builder, cpuSoftirq):
    builder.PrependFloat32Slot(25, cpuSoftirq, 0.0)

def AddCpuSoftirq(builder, cpuSoftirq):
    MNodeLogAddCpuSoftirq(builder, cpuSoftirq)

def MNodeLogAddCpuSteal(builder, cpuSteal):
    builder.PrependFloat32Slot(26, cpuSteal, 0.0)

def AddCpuSteal(builder, cpuSteal):
    MNodeLogAddCpuSteal(builder, cpuSteal)

def MNodeLogAddCpuSystem(builder, cpuSystem):
    builder.PrependFloat32Slot(27, cpuSystem, 0.0)

def AddCpuSystem(builder, cpuSystem):
    MNodeLogAddCpuSystem(builder, cpuSystem)

def MNodeLogAddCpuUser(builder, cpuUser):
    builder.PrependFloat32Slot(28, cpuUser, 0.0)

def AddCpuUser(builder, cpuUser):
    MNodeLogAddCpuUser(builder, cpuUser)

def MNodeLogAddDiskBusyTime(builder, diskBusyTime):
    builder.PrependUint64Slot(29, diskBusyTime, 0)

def AddDiskBusyTime(builder, diskBusyTime):
    MNodeLogAddDiskBusyTime(builder, diskBusyTime)

def MNodeLogAddDiskReadBytes(builder, diskReadBytes):
    builder.PrependUint64Slot(30, diskReadBytes, 0)

def AddDiskReadBytes(builder, diskReadBytes):
    MNodeLogAddDiskReadBytes(builder, diskReadBytes)

def MNodeLogAddDiskReadCount(builder, diskReadCount):
    builder.PrependUint64Slot(31, diskReadCount, 0)

def AddDiskReadCount(builder, diskReadCount):
    MNodeLogAddDiskReadCount(builder, diskReadCount)

def MNodeLogAddDiskReadMergedCount(builder, diskReadMergedCount):
    builder.PrependUint64Slot(32, diskReadMergedCount, 0)

def AddDiskReadMergedCount(builder, diskReadMergedCount):
    MNodeLogAddDiskReadMergedCount(builder, diskReadMergedCount)

def MNodeLogAddDiskReadTime(builder, diskReadTime):
    builder.PrependUint64Slot(33, diskReadTime, 0)

def AddDiskReadTime(builder, diskReadTime):
    MNodeLogAddDiskReadTime(builder, diskReadTime)

def MNodeLogAddDiskWriteBytes(builder, diskWriteBytes):
    builder.PrependUint64Slot(34, diskWriteBytes, 0)

def AddDiskWriteBytes(builder, diskWriteBytes):
    MNodeLogAddDiskWriteBytes(builder, diskWriteBytes)

def MNodeLogAddDiskWriteCount(builder, diskWriteCount):
    builder.PrependUint64Slot(35, diskWriteCount, 0)

def AddDiskWriteCount(builder, diskWriteCount):
    MNodeLogAddDiskWriteCount(builder, diskWriteCount)

def MNodeLogAddDiskWriteMergedCount(builder, diskWriteMergedCount):
    builder.PrependUint64Slot(36, diskWriteMergedCount, 0)

def AddDiskWriteMergedCount(builder, diskWriteMergedCount):
    MNodeLogAddDiskWriteMergedCount(builder, diskWriteMergedCount)

def MNodeLogAddDiskWriteTime(builder, diskWriteTime):
    builder.PrependUint64Slot(37, diskWriteTime, 0)

def AddDiskWriteTime(builder, diskWriteTime):
    MNodeLogAddDiskWriteTime(builder, diskWriteTime)

def MNodeLogAddMemoryActive(builder, memoryActive):
    builder.PrependUint64Slot(38, memoryActive, 0)

def AddMemoryActive(builder, memoryActive):
    MNodeLogAddMemoryActive(builder, memoryActive)

def MNodeLogAddMemoryAvailable(builder, memoryAvailable):
    builder.PrependUint64Slot(39, memoryAvailable, 0)

def AddMemoryAvailable(builder, memoryAvailable):
    MNodeLogAddMemoryAvailable(builder, memoryAvailable)

def MNodeLogAddMemoryBuffers(builder, memoryBuffers):
    builder.PrependUint64Slot(40, memoryBuffers, 0)

def AddMemoryBuffers(builder, memoryBuffers):
    MNodeLogAddMemoryBuffers(builder, memoryBuffers)

def MNodeLogAddMemoryCached(builder, memoryCached):
    builder.PrependUint64Slot(41, memoryCached, 0)

def AddMemoryCached(builder, memoryCached):
    MNodeLogAddMemoryCached(builder, memoryCached)

def MNodeLogAddMemoryFree(builder, memoryFree):
    builder.PrependUint64Slot(42, memoryFree, 0)

def AddMemoryFree(builder, memoryFree):
    MNodeLogAddMemoryFree(builder, memoryFree)

def MNodeLogAddMemoryInactive(builder, memoryInactive):
    builder.PrependUint64Slot(43, memoryInactive, 0)

def AddMemoryInactive(builder, memoryInactive):
    MNodeLogAddMemoryInactive(builder, memoryInactive)

def MNodeLogAddMemoryPercent(builder, memoryPercent):
    builder.PrependFloat32Slot(44, memoryPercent, 0.0)

def AddMemoryPercent(builder, memoryPercent):
    MNodeLogAddMemoryPercent(builder, memoryPercent)

def MNodeLogAddMemoryShared(builder, memoryShared):
    builder.PrependUint64Slot(45, memoryShared, 0)

def AddMemoryShared(builder, memoryShared):
    MNodeLogAddMemoryShared(builder, memoryShared)

def MNodeLogAddMemorySlab(builder, memorySlab):
    builder.PrependUint64Slot(46, memorySlab, 0)

def AddMemorySlab(builder, memorySlab):
    MNodeLogAddMemorySlab(builder, memorySlab)

def MNodeLogAddMemoryTotal(builder, memoryTotal):
    builder.PrependUint64Slot(47, memoryTotal, 0)

def AddMemoryTotal(builder, memoryTotal):
    MNodeLogAddMemoryTotal(builder, memoryTotal)

def MNodeLogAddMemoryUsed(builder, memoryUsed):
    builder.PrependUint64Slot(48, memoryUsed, 0)

def AddMemoryUsed(builder, memoryUsed):
    MNodeLogAddMemoryUsed(builder, memoryUsed)

def MNodeLogAddNetworkBytesRecv(builder, networkBytesRecv):
    builder.PrependUint64Slot(49, networkBytesRecv, 0)

def AddNetworkBytesRecv(builder, networkBytesRecv):
    MNodeLogAddNetworkBytesRecv(builder, networkBytesRecv)

def MNodeLogAddNetworkBytesSent(builder, networkBytesSent):
    builder.PrependUint64Slot(50, networkBytesSent, 0)

def AddNetworkBytesSent(builder, networkBytesSent):
    MNodeLogAddNetworkBytesSent(builder, networkBytesSent)

def MNodeLogAddNetworkConnectionAfInet(builder, networkConnectionAfInet):
    builder.PrependUint32Slot(51, networkConnectionAfInet, 0)

def AddNetworkConnectionAfInet(builder, networkConnectionAfInet):
    MNodeLogAddNetworkConnectionAfInet(builder, networkConnectionAfInet)

def MNodeLogAddNetworkConnectionAfInet6(builder, networkConnectionAfInet6):
    builder.PrependUint32Slot(52, networkConnectionAfInet6, 0)

def AddNetworkConnectionAfInet6(builder, networkConnectionAfInet6):
    MNodeLogAddNetworkConnectionAfInet6(builder, networkConnectionAfInet6)

def MNodeLogAddNetworkConnectionAfUnix(builder, networkConnectionAfUnix):
    builder.PrependUint32Slot(53, networkConnectionAfUnix, 0)

def AddNetworkConnectionAfUnix(builder, networkConnectionAfUnix):
    MNodeLogAddNetworkConnectionAfUnix(builder, networkConnectionAfUnix)

def MNodeLogAddNetworkDropin(builder, networkDropin):
    builder.PrependUint32Slot(54, networkDropin, 0)

def AddNetworkDropin(builder, networkDropin):
    MNodeLogAddNetworkDropin(builder, networkDropin)

def MNodeLogAddNetworkDropout(builder, networkDropout):
    builder.PrependUint32Slot(55, networkDropout, 0)

def AddNetworkDropout(builder, networkDropout):
    MNodeLogAddNetworkDropout(builder, networkDropout)

def MNodeLogAddNetworkErrin(builder, networkErrin):
    builder.PrependUint32Slot(56, networkErrin, 0)

def AddNetworkErrin(builder, networkErrin):
    MNodeLogAddNetworkErrin(builder, networkErrin)

def MNodeLogAddNetworkErrout(builder, networkErrout):
    builder.PrependUint32Slot(57, networkErrout, 0)

def AddNetworkErrout(builder, networkErrout):
    MNodeLogAddNetworkErrout(builder, networkErrout)

def MNodeLogAddNetworkPacketsRecv(builder, networkPacketsRecv):
    builder.PrependUint64Slot(58, networkPacketsRecv, 0)

def AddNetworkPacketsRecv(builder, networkPacketsRecv):
    MNodeLogAddNetworkPacketsRecv(builder, networkPacketsRecv)

def MNodeLogAddNetworkPacketsSent(builder, networkPacketsSent):
    builder.PrependUint64Slot(59, networkPacketsSent, 0)

def AddNetworkPacketsSent(builder, networkPacketsSent):
    MNodeLogAddNetworkPacketsSent(builder, networkPacketsSent)

def MNodeLogEnd(builder):
    return builder.EndObject()

def End(builder):
    return MNodeLogEnd(builder)
