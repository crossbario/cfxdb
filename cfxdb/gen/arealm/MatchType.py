# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

# WAMP URI match type applied (for pattern subscription/registrations and permissions).
class MatchType(object):
    # No match type.
    NONE = 0
    # Match URI exactly.
    EXACT = 1
    # Match by URI prefix.
    PREFIX = 2
    # Match by URI wildcard pattern.
    WILDCARD = 3
