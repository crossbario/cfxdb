# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# WAMP authentication roles defined, including permissions.
class Role(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Role()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsRole(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Role
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ID of this object.
    # Role
    def Oid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Time when the object was created.
    # Role
    def Created(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Owner organization of this object.
    # Role
    def Owner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Name of this role, must be unique within the management realm at any given point in time.
    # Role
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Set of static permissions on the role.
    # Role
    def Permissions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 9
            from arealm.Permission import Permission
            obj = Permission()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Role
    def PermissionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Role
    def PermissionsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # URIs or URI patterns the permissions must match.
    # Role
    def PermissionUris(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Role
    def PermissionUrisLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Role
    def PermissionUrisIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Alternatively to defining a static set of permissions, the WAMP procedure URI of a dynamic authorizer can be specified.
    # Role
    def Authorizer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def RoleStart(builder): builder.StartObject(7)
def Start(builder):
    return RoleStart(builder)
def RoleAddOid(builder, oid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def AddOid(builder, oid):
    return RoleAddOid(builder, oid)
def RoleAddCreated(builder, created): builder.PrependUint64Slot(1, created, 0)
def AddCreated(builder, created):
    return RoleAddCreated(builder, created)
def RoleAddOwner(builder, owner): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(owner), 0)
def AddOwner(builder, owner):
    return RoleAddOwner(builder, owner)
def RoleAddName(builder, name): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return RoleAddName(builder, name)
def RoleAddPermissions(builder, permissions): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(permissions), 0)
def AddPermissions(builder, permissions):
    return RoleAddPermissions(builder, permissions)
def RoleStartPermissionsVector(builder, numElems): return builder.StartVector(9, numElems, 1)
def StartPermissionsVector(builder, numElems):
    return RoleStartPermissionsVector(builder, numElems)
def RoleAddPermissionUris(builder, permissionUris): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(permissionUris), 0)
def AddPermissionUris(builder, permissionUris):
    return RoleAddPermissionUris(builder, permissionUris)
def RoleStartPermissionUrisVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartPermissionUrisVector(builder, numElems):
    return RoleStartPermissionUrisVector(builder, numElems)
def RoleAddAuthorizer(builder, authorizer): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(authorizer), 0)
def AddAuthorizer(builder, authorizer):
    return RoleAddAuthorizer(builder, authorizer)
def RoleEnd(builder): return builder.EndObject()
def End(builder):
    return RoleEnd(builder)