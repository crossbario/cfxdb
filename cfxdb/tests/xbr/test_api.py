##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import os
import uuid
import random
import timeit
import pytest

import numpy as np
import flatbuffers

import zlmdb

import txaio
txaio.use_twisted()  # noqa

from txaio import time_ns
from autobahn import util

from cfxdb.xbr import TokenApproval, TokenTransfer, Market, Member, Actor, \
    PaymentChannel, PayingChannelRequest, PaymentChannelBalance, Offer, Transaction

from cfxdb.tests._util import _gen_ipfs_hash

zlmdb.TABLES_BY_UUID = {}


@pytest.fixture(scope='function')
def builder():
    _builder = flatbuffers.Builder(0)
    return _builder


def fill_api(actor):
    actor.actor = os.urandom(20)
    actor.actor_type = random.randint(1, 2)
    actor.market = uuid.uuid4()
    actor.timestamp = np.datetime64(time_ns(), 'ns')
    actor.joined = random.randint(0, 2**256 - 1)
    actor.security = random.randint(0, 2**256 - 1)
    actor.meta = _gen_ipfs_hash()
    actor.tid = os.urandom(32)
    actor.signature = os.urandom(65)


@pytest.fixture(scope='function')
def actor():
    _actor = Actor()
    fill_api(_actor)
    return _actor


def test_api_roundtrip(actor, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = actor.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 368

    # create python object from bytes (flatbuffes)
    _actor = Actor.cast(data)

    assert _actor.actor == actor.actor
    assert _actor.actor_type == actor.actor_type
    assert _actor.market == actor.market
    assert _actor.timestamp == actor.timestamp
    assert _actor.joined == actor.joined
    assert _actor.security == actor.security
    assert _actor.meta == actor.meta
    assert _actor.tid == actor.tid
    assert _actor.signature == actor.signature
