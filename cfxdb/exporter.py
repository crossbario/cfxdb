##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import os

import zlmdb
import cfxdb


# cfxdb.schema.Schema
# cfxdb.meta.Schema
# cfxdb.globalschema.GlobalSchema
# cfxdb.mrealmschema.MrealmSchema
# cfxdb.xbr.Schema
# cfxdb.xbrmm.Schema
# cfxdb.xbrnetwork.Schema

import uuid
import binascii

from cfxdb.xbrnetwork import VerifiedAction, Account, UserKey
from txaio import make_logger, time_ns, sleep
import numpy as np



dbpath = os.path.abspath('.xbrnetwork')
db = zlmdb.Database(dbpath=dbpath, maxsize=2 ** 30, readonly=False)
db.__enter__()

meta = cfxdb.meta.Schema.attach(db)
xbr = cfxdb.xbr.Schema.attach(db)
xbrnetwork = cfxdb.xbrnetwork.Schema.attach(db)

account = Account()
account.oid = uuid.uuid4()
account.created = np.datetime64(time_ns(), 'ns')
account.username = 'alice'
account.email = 'alice@example.com'
account.wallet_type = 2  # metamask
account.wallet_address = binascii.a2b_hex('f5173a6111B2A6B3C20fceD53B2A8405EC142bF6')

userkey = UserKey()
userkey.pubkey = binascii.a2b_hex('b7e6462121b9632b2bfcc5a3beef0b49dd865093ad003d011d4abbb68476d5b4')
userkey.created = account.created
userkey.owner = account.oid

with db.begin(write=True) as txn:
    xbrnetwork.accounts[txn, account.oid] = account
    xbrnetwork.user_keys[txn, userkey.pubkey] = userkey

with db.begin() as txn:
    cnt_accounts = xbrnetwork.accounts.count(txn)
    cnt_idx_accounts_by_username = xbrnetwork.idx_accounts_by_username.count(txn)
    cnt_verified_actions = xbrnetwork.verified_actions.count(txn)

print(
    'Database opened from {dbpath} (cnt_accounts={cnt_accounts}, cnt_idx_accounts_by_username={cnt_idx_accounts_by_username}, cnt_verified_actions={cnt_verified_actions})'.format(
        dbpath=dbpath,
        cnt_accounts=cnt_accounts,
        cnt_idx_accounts_by_username=cnt_idx_accounts_by_username,
        cnt_verified_actions=cnt_verified_actions))

print('-' * 80)
slots = db._get_slots()
for slot_id in slots:
    slot = slots[slot_id]
    print('slot {}: {}'.format(slot_id, slot.name, slot.description))

print('-' * 80)
tables = []
first = None
for k, v in xbrnetwork.__annotations__.items():
    for line in v.__doc__.splitlines():
        line = line.strip()
        if line != "":
            first = line[:80]
            break
    print('{:<30}: {}..'.format(k, first))
    tables.append(k)

print('-' * 80)
with db.begin() as txn:
    # print('{} members'.format(xbrnetwork.members.count(txn)))
    for table in tables:
        if table in xbrnetwork.__dict__:
            print('{} {}'.format(table, xbrnetwork.__dict__[table].count(txn)))
