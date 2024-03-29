# automatically generated by the FlatBuffers compiler, do not modify

# namespace: arealm

# WAMP authentication methods.
class AuthenticationMethod(object):
    # No authentiation method defined (undefined).
    NONE = 0
    # WAMP-anonymous authentication.
    ANONYMOUS = 1
    # WAMP-ticket authentication.
    TICKET = 2
    # WAMP-CRA authentication.
    WAMPCRA = 3
    # TLS client certificate authentication [TRANSPORT LEVEL].
    TLS = 4
    # HTTP cookie authentication [TRANSPORT LEVEL].
    COOKIE = 5
    # WAMP-cryptosign authentication.
    CRYPTOSIGN = 6
    # WAMP-SCRAM authentication.
    SCRAM = 7
