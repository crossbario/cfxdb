##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

from cfxdb.xbrmm.consent import Consents, IndexConsentByMemberAddress

from cfxdb.xbrmm.channel import PaymentChannels, IndexPaymentChannelByDelegate, \
    PaymentChannelBalances, PayingChannels, IndexPayingChannelByDelegate, \
    PayingChannelBalances

from cfxdb.xbrmm.offer import Offers, IndexOfferByKey
from cfxdb.xbrmm.transaction import Transactions


class Schema(object):
    """
    CFC edge database schema for ZLMDB.
    """
    def __init__(self, db):
        self.db = db

    consents: Consents
    """
    XBR data consents.
    """

    idx_consent_by_member_adr: IndexConsentByMemberAddress
    """
    Consents-by-members-address index with ``(member_adr|bytes[20], joined|int) -> member_adr|UUID`` mapping.
    """

    payment_channels: PaymentChannels
    """
    Payment channels for XBR consumer delegates.
    """

    idx_payment_channel_by_delegate: IndexPaymentChannelByDelegate
    """
    Maps from XBR consumer delegate address to the currently active payment
    channel address for the given consumer delegate.
    """

    payment_balances: PaymentChannelBalances
    """
    Current off-chain balances within payment channels.
    """

    paying_channels: PayingChannels
    """
    Paying channels for XBR provider delegates.
    """

    idx_paying_channel_by_delegate: IndexPayingChannelByDelegate
    """
    Maps from XBR provider delegate address to the currently active paying
    channel address for the given provider delegate.
    """

    paying_balances: PayingChannelBalances
    """
    Current off-chain balances within paying channels.
    """

    offers: Offers
    """
    Data encryption key offers.
    """

    idx_offer_by_key: IndexOfferByKey
    """
    Index of key offers by key ID (rather than offer ID, as the object table
    is indexed by).
    """

    transaction: Transactions
    """
    """

    @staticmethod
    def attach(db):
        """
        Factory to create a schema from attaching to a database. The schema tables
        will be automatically mapped as persistant maps and attached to the
        database slots.

        :param db: zlmdb.Database
        :return: object of Schema
        """
        schema = Schema(db)

        schema.consents = db.attach_table(Consents)

        schema.idx_consent_by_member_adr = db.attach_table(IndexConsentByMemberAddress)

        schema.payment_channels = db.attach_table(PaymentChannels)

        schema.idx_payment_channel_by_delegate = db.attach_table(IndexPaymentChannelByDelegate)
        # schema.payment_channels.attach_index('idx1',
        #                                      schema.idx_payment_channel_by_delegate,
        #                                      lambda payment_channel: (bytes(payment_channel.delegate), np.datetime64(time_ns(), 'ns')))

        schema.payment_balances = db.attach_table(PaymentChannelBalances)

        schema.paying_channels = db.attach_table(PayingChannels)

        schema.idx_paying_channel_by_delegate = db.attach_table(IndexPayingChannelByDelegate)
        # schema.paying_channels.attach_index('idx1',
        #                                      schema.idx_paying_channel_by_delegate,
        #                                      lambda paying_channel: (bytes(paying_channel.delegate), np.datetime64(time_ns(), 'ns')))

        # schema.idx_paying_channel_by_recipient = db.attach_table(IndexPayingChannelByRecipient)
        # schema.paying_channels.attach_index('idx2',
        #                                      schema.idx_paying_channel_by_recipient,
        #                                      lambda paying_channel: (bytes(paying_channel.recipient), np.datetime64(time_ns(), 'ns')))

        schema.paying_balances = db.attach_table(PayingChannelBalances)

        schema.offers = db.attach_table(Offers)
        schema.idx_offer_by_key = db.attach_table(IndexOfferByKey)
        schema.offers.attach_index('idx1', schema.idx_offer_by_key, lambda offer: offer.key)

        schema.transactions = db.attach_table(Transactions)

        return schema
