##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import os

import zlmdb
import cfxdb
import cbor2
import click

from pprint import pprint

import uuid
import binascii

from cfxdb.xbrnetwork import Account, UserKey
from txaio import time_ns
import numpy as np


class Exporter(object):
    """
    CFXDB database exporter.
    """
    def __init__(self, dbpath):
        """

        :param dbpath: Database file to open.
        """
        self._dbpath = os.path.abspath(dbpath)
        self._db = zlmdb.Database(dbpath=self._dbpath, maxsize=2**30, readonly=False)
        self._db.__enter__()

        # cfxdb.schema.Schema
        # cfxdb.meta.Schema
        # cfxdb.globalschema.GlobalSchema
        # cfxdb.mrealmschema.MrealmSchema
        # cfxdb.xbr.Schema
        # cfxdb.xbrmm.Schema
        # cfxdb.xbrnetwork.Schema

        self._meta = cfxdb.meta.Schema.attach(self._db)
        self._globalschema = cfxdb.globalschema.GlobalSchema.attach(self._db)
        self._mrealmschema = cfxdb.mrealmschema.MrealmSchema.attach(self._db)
        self._xbr = cfxdb.xbr.Schema.attach(self._db)
        self._xbrmm = cfxdb.xbrmm.Schema.attach(self._db)
        self._xbrnetwork = cfxdb.xbrnetwork.Schema.attach(self._db)

        self._schemata = {
            # 'meta': self._meta,
            'globalschema': self._globalschema,
            # 'mrealmschema': self._mrealmschema,
            'xbr': self._xbr,
            'xbrmm': self._xbrmm,
            'xbrnetwork': self._xbrnetwork,
        }

        pprint(self._schemata)

        self._schema_tables = {}

        for schema_name, schema in self._schemata.items():
            tables = {}
            first = None
            for k, v in schema.__annotations__.items():
                for line in v.__doc__.splitlines():
                    line = line.strip()
                    if line != "":
                        first = line[:80]
                        break
                tables[k] = first
            self._schema_tables[schema_name] = tables

        pprint(self._schema_tables)

    def add_test_data(self):
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

        with self._db.begin(write=True) as txn:
            self._xbrnetwork.accounts[txn, account.oid] = account
            self._xbrnetwork.user_keys[txn, userkey.pubkey] = userkey

    def print_slots(self):
        print('\nDatabase slots [dbpath="{dbpath}"]:\n'.format(dbpath=self._dbpath))
        slots = self._db._get_slots()
        for slot_id in slots:
            slot = slots[slot_id]
            print('   Slot {} using DB table class {}: {}'.format(
                click.style(str(slot_id), fg='white', bold=True), click.style(slot.name, fg='yellow'),
                slot.description))
        print('')

    def print_stats(self):
        print('\nDatabase table statistics [dbpath="{dbpath}"]:\n'.format(dbpath=self._dbpath))
        stats = {}
        with self._db.begin() as txn:
            for schema_name in self._schemata:
                stats[schema_name] = {}
                for table_name in self._schema_tables[schema_name]:
                    table = self._schemata[schema_name].__dict__[table_name]
                    cnt = table.count(txn)
                    stats[schema_name][table_name] = cnt
        for schema_name in stats:
            for table_name in stats[schema_name]:
                print('{:.<52}: {}'.format(
                    click.style('{}.{}'.format(schema_name, table_name), fg='white', bold=True),
                    click.style(str(stats[schema_name][table_name]) + ' records', fg='yellow')))

    def export(self, filename):
        result = {}
        with self._db.begin() as txn:
            for schema_name in self._schemata:
                for table_name in self._schema_tables[schema_name]:
                    table = self._schemata[schema_name].__dict__[table_name]
                    recs = []
                    for key, val in table.select(txn, return_keys=True, return_values=True):
                        if val:
                            if hasattr(val, 'marshal'):
                                val = val.marshal()
                        recs.append((table._serialize_key(key), val))
                    if recs:
                        if schema_name not in result:
                            result[schema_name] = {}
                        result[schema_name][table_name] = recs

        data = cbor2.dumps(result)
        with open(filename, 'wb') as f:
            f.write(data)

        data_recovered = cbor2.loads(data)
        pprint(data_recovered)


if __name__ == '__main__':
    exporter = Exporter('.xbrnetwork')
    exporter.add_test_data()
    exporter.print_slots()
    exporter.print_stats()
    exporter.export('test.dat')
