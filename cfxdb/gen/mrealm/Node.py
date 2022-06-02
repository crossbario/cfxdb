# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mrealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Node(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Node()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsNode(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Node
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this object.
    # Node
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
    # Node
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Description for this object (not interpreted by CFC).
    # Node
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Tags on this object.
    # Node
    def Tags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Node
    def TagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Node
    def TagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Name of this object (must be globally unique within CFC at any given point in time).
    # Also used for WAMP authid under which the node is authenticated on the management realm.
    # Node
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP-cryptosign node public key (32 bytes as HEX encoded string).
    # Node
    def Pubkey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP ``realm`` the node will be joined on.
    # Node
    def Realm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP-cryptosign ``authid`` the node will be authenticated as.
    # Node
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Optional WAMP authextra to be sent to the node when authenticating. CBOR serialized binary.
    # Node
    def Authextra(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Node
    def AuthextraAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Node
    def AuthextraLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Node
    def AuthextraIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

def NodeStart(builder): builder.StartObject(9)
def Start(builder):
    return NodeStart(builder)
def NodeAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def AddOid(builder, oid):
    return NodeAddOid(builder, oid)
def NodeAddLabel(builder, label): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0)
def AddLabel(builder, label):
    return NodeAddLabel(builder, label)
def NodeAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def AddDescription(builder, description):
    return NodeAddDescription(builder, description)
def NodeAddTags(builder, tags): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(tags), 0)
def AddTags(builder, tags):
    return NodeAddTags(builder, tags)
def NodeStartTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartTagsVector(builder, numElems):
    return NodeStartTagsVector(builder, numElems)
def NodeAddName(builder, name): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return NodeAddName(builder, name)
def NodeAddPubkey(builder, pubkey): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(pubkey), 0)
def AddPubkey(builder, pubkey):
    return NodeAddPubkey(builder, pubkey)
def NodeAddRealm(builder, realm): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(realm), 0)
def AddRealm(builder, realm):
    return NodeAddRealm(builder, realm)
def NodeAddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def AddAuthid(builder, authid):
    return NodeAddAuthid(builder, authid)
def NodeAddAuthextra(builder, authextra): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(authextra), 0)
def AddAuthextra(builder, authextra):
    return NodeAddAuthextra(builder, authextra)
def NodeStartAuthextraVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartAuthextraVector(builder, numElems):
    return NodeStartAuthextraVector(builder, numElems)
def NodeEnd(builder): return builder.EndObject()
def End(builder):
    return NodeEnd(builder)