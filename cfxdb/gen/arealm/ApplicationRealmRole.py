# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers

# /// Association (N:M) between roles and application realms, both defined independently at the management realm level.
class ApplicationRealmRole(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsApplicationRealmRole(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ApplicationRealmRole()
        x.Init(buf, n + offset)
        return x

    # ApplicationRealmRole
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// ID of the role being associated with an application realm.
    # ApplicationRealmRole
    def RoleOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

# /// ID of the application realm this role is associated with.
    # ApplicationRealmRole
    def ArealmOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ApplicationRealmRoleStart(builder): builder.StartObject(2)
def ApplicationRealmRoleAddRoleOid(builder, roleOid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(roleOid), 0)
def ApplicationRealmRoleAddArealmOid(builder, arealmOid): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(arealmOid), 0)
def ApplicationRealmRoleEnd(builder): return builder.EndObject()
