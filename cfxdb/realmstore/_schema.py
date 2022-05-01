##############################################################################
#
#                        Crossbar.io Database
#     Copyright (c) Crossbar.io Technologies GmbH. Licensed under MIT.
#
##############################################################################

import zlmdb
from cfxdb.realmstore._appsession import AppSessions, IndexAppSessionsBySession


class RealmStoreSchema(object):
    """
    Persistent realm store.
    """

    def __init__(self, db):
        self.db = db

    app_sessions: AppSessions
    """
    Sessions persisted in this realm store.
    """

    idx_app_sessions_by_session: IndexAppSessionsBySession
    """
    Index: (session, joined_at) -> app_session_oid
    """

    @staticmethod
    def attach(db: zlmdb.Database) -> 'RealmStoreSchema':
        schema = RealmStoreSchema(db)

        schema.app_sessions = db.attach_table(AppSessions)

        schema.idx_app_sessions_by_session = db.attach_table(IndexAppSessionsBySession)
        schema.app_sessions.attach_index('idx1', schema.idx_app_sessions_by_session,
                                         lambda session: (session.session, session.joined_at))

        return schema
