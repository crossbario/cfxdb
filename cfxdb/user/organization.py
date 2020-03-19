from datetime import datetime
from pprint import pformat

import six

from cfxdb.common import ConfigurationElement
from cfxdb.gen.user.OrganizationType import OrganizationType


class Organization(ConfigurationElement):
    """
    CFC organization database class.
    """

    # oid: uuid.UUID
    # label: Optional[str]
    # description: Optional[str]
    # tags: Optional[List[str]]
    # name: str
    # otype: int
    # registered: Optional[datetime]

    OTYPES = [
        OrganizationType.NONE, OrganizationType.BUSINESS, OrganizationType.ACADEMICS,
        OrganizationType.PERSONAL
    ]

    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 name=None,
                 otype=None,
                 registered=None,
                 _unknown=None):
        """

        :param oid: Object ID of the organization
        :type oid: uuid.UUID

        :param label: Optional user label of the organization
        :type label: str

        :param description: Optional user description of the organization
        :type description: str

        :param tags: Optional list of user tags on the organization
        :type tags: list[str]

        :param name: Name of the organization
        :type name: str

        :param otype: Type of the organization.
        :type otype: int

        :param registered: Timestamp when the organization was created
        :type registered: datetime.datetime

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)

        self.name = name
        self.otype = otype
        self.registered = registered

        # private member with unknown/untouched data passing through
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.name != self.name:
            return False
        if other.otype != self.otype:
            return False
        if other.registered != self.registered:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pformat(self.marshal()))

    def copy(self, other):
        ConfigurationElement.copy(self, other)

        self.name = other.name
        self.otype = other.otype
        self.registered = other.registered

        # _unknown is not copied!

    def marshal(self):
        obj = ConfigurationElement.marshal(self)

        assert self.name is None or type(self.name) == six.text_type
        assert self.otype is None or self.otype in Organization.OTYPES
        assert self.registered is None or isinstance(self.registered, datetime)

        registered = int(self.registered.timestamp() * 1000000) if self.registered else None
        obj.update({
            'name': self.name,
            'otype': self.otype,
            'registered': registered,
        })

        if self._unknown:
            # pass through all attributes unknown
            obj.update(self._unknown)

        return obj

    @staticmethod
    def parse(data):
        assert type(data) == dict

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['name', 'otype', 'registered']:
                _unknown[k] = data[k]

        name = data.get('name', None)
        assert name is None or type(name) == six.text_type

        otype = data.get('otype', None)
        assert otype is None or otype in Organization.OTYPES

        registered = data.get('registered', None)
        assert registered is None or type(registered) == float or type(registered) in six.integer_types
        if registered:
            # registered = datetime.utcfromtimestamp(float(registered) / 1000000.)
            registered = datetime.fromtimestamp(float(registered) / 1000000.)

        obj = Organization(oid=obj.oid,
                           label=obj.label,
                           description=obj.description,
                           tags=obj.tags,
                           name=name,
                           otype=otype,
                           registered=registered,
                           _unknown=_unknown)
        return obj
