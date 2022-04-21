# automatically generated by the FlatBuffers compiler, do not modify

# namespace: cookiestore

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# This table stores persistent cookies, as used in WAMP-Cookie authentication by router and proxy workers.
class Cookie(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Cookie()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCookie(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Cookie
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Database ID of this cookie record.
    # Cookie
    def Oid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Cookie
    def OidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Cookie
    def OidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Cookie
    def OidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Timestamp when the cookie was created. Epoch time in ns.
    # Cookie
    def Created(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Cookie maximum age (lifetime of the cookie in seconds, see http://tools.ietf.org/html/rfc6265#page-20), e.g. ``604800"``.
    # Cookie
    def MaxAge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Cookie name, as set in HTTP header, e.g. ``"cbtid"``.
    # Cookie
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Cookie value, as set in HTTP header, e.g. ``"gn2ri8fuAYQse50/L6N7jnt2"``.
    # Cookie
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Timestamp when the cookie was authenticated (if any). Epoch time in ns.
    # Cookie
    def Authenticated(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # The Crossbar.io node (within the management domain) the cookie was authenticated on (if any).
    # Cookie
    def AuthenticatedOnNode(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Cookie
    def AuthenticatedOnNodeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Cookie
    def AuthenticatedOnNodeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Cookie
    def AuthenticatedOnNodeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # The WAMP session ID of the original authenticating session.
    # Cookie
    def AuthenticatedSession(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Timestamp when the original authenticating session was welcome by the router. Epoch time in ns.
    # Cookie
    def AuthenticatedJoinedAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # The (original) WAMP authentication method, after which the client was authenticated before setting this cookie.
    # Cookie
    def AuthenticatedAuthmethod(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP authid a cookie-authenticating session is to be assigned.
    # Cookie
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP authrole a cookie-authenticating session is to join under.
    # Cookie
    def Authrole(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP realm a cookie-authenticating session is to join.
    # Cookie
    def Authrealm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP authentication extra data to be returned to the client performing cookie-based authentication.
    # Cookie
    def Authextra(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Cookie
    def AuthextraAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Cookie
    def AuthextraLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Cookie
    def AuthextraIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

def Start(builder): builder.StartObject(14)
def CookieStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddOid(builder, oid): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def CookieAddOid(builder, oid):
    """This method is deprecated. Please switch to AddOid."""
    return AddOid(builder, oid)
def StartOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def CookieStartOidVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartOidVector(builder, numElems)
def AddCreated(builder, created): builder.PrependUint64Slot(1, created, 0)
def CookieAddCreated(builder, created):
    """This method is deprecated. Please switch to AddCreated."""
    return AddCreated(builder, created)
def AddMaxAge(builder, maxAge): builder.PrependUint64Slot(2, maxAge, 0)
def CookieAddMaxAge(builder, maxAge):
    """This method is deprecated. Please switch to AddMaxAge."""
    return AddMaxAge(builder, maxAge)
def AddName(builder, name): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def CookieAddName(builder, name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, name)
def AddValue(builder, value): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def CookieAddValue(builder, value):
    """This method is deprecated. Please switch to AddValue."""
    return AddValue(builder, value)
def AddAuthenticated(builder, authenticated): builder.PrependUint64Slot(5, authenticated, 0)
def CookieAddAuthenticated(builder, authenticated):
    """This method is deprecated. Please switch to AddAuthenticated."""
    return AddAuthenticated(builder, authenticated)
def AddAuthenticatedOnNode(builder, authenticatedOnNode): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(authenticatedOnNode), 0)
def CookieAddAuthenticatedOnNode(builder, authenticatedOnNode):
    """This method is deprecated. Please switch to AddAuthenticatedOnNode."""
    return AddAuthenticatedOnNode(builder, authenticatedOnNode)
def StartAuthenticatedOnNodeVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def CookieStartAuthenticatedOnNodeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartAuthenticatedOnNodeVector(builder, numElems)
def AddAuthenticatedSession(builder, authenticatedSession): builder.PrependUint64Slot(7, authenticatedSession, 0)
def CookieAddAuthenticatedSession(builder, authenticatedSession):
    """This method is deprecated. Please switch to AddAuthenticatedSession."""
    return AddAuthenticatedSession(builder, authenticatedSession)
def AddAuthenticatedJoinedAt(builder, authenticatedJoinedAt): builder.PrependUint64Slot(8, authenticatedJoinedAt, 0)
def CookieAddAuthenticatedJoinedAt(builder, authenticatedJoinedAt):
    """This method is deprecated. Please switch to AddAuthenticatedJoinedAt."""
    return AddAuthenticatedJoinedAt(builder, authenticatedJoinedAt)
def AddAuthenticatedAuthmethod(builder, authenticatedAuthmethod): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(authenticatedAuthmethod), 0)
def CookieAddAuthenticatedAuthmethod(builder, authenticatedAuthmethod):
    """This method is deprecated. Please switch to AddAuthenticatedAuthmethod."""
    return AddAuthenticatedAuthmethod(builder, authenticatedAuthmethod)
def AddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def CookieAddAuthid(builder, authid):
    """This method is deprecated. Please switch to AddAuthid."""
    return AddAuthid(builder, authid)
def AddAuthrole(builder, authrole): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(authrole), 0)
def CookieAddAuthrole(builder, authrole):
    """This method is deprecated. Please switch to AddAuthrole."""
    return AddAuthrole(builder, authrole)
def AddAuthrealm(builder, authrealm): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(authrealm), 0)
def CookieAddAuthrealm(builder, authrealm):
    """This method is deprecated. Please switch to AddAuthrealm."""
    return AddAuthrealm(builder, authrealm)
def AddAuthextra(builder, authextra): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(authextra), 0)
def CookieAddAuthextra(builder, authextra):
    """This method is deprecated. Please switch to AddAuthextra."""
    return AddAuthextra(builder, authextra)
def StartAuthextraVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def CookieStartAuthextraVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartAuthextraVector(builder, numElems)
def End(builder): return builder.EndObject()
def CookieEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)