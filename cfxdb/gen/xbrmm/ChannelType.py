# automatically generated by the FlatBuffers compiler, do not modify

# namespace: xbrmm

# Type of a XBR off-chain channel: paying channel (for provider delegates selling data services) or payment channel (for consumer delegates buying data services).
class ChannelType(object):
    # Unset
    NONE = 0
    # Payment channel: from buyer/consumer delegate to maker maker.
    PAYMENT = 1
    # Paying channel: from market maker to seller/provider delegate.
    PAYING = 2
