##############################################################################
#
#                        Crossbar.io Database
#     Copyright (c) typedef int GmbH. Licensed under MIT.
#
##############################################################################

from cfxdb.mrealm.web_service import WebService


def test_other_without_unknown_returns_default():
    # A web service built directly has no _unknown attributes (it is None): other()
    # returns the default instead of failing on None (#149).
    ws = WebService()
    assert ws.other("x") is None
    assert ws.other("x", "dflt") == "dflt"


def test_other_with_unknown():
    ws = WebService(_unknown={"x": 23})
    assert ws.other("x") == 23
    assert ws.other("y", "dflt") == "dflt"
