Database Schema
===============

All database tables and indexes can be accessed using the type information and
schema definitions from a single database schema class:

.. autoclass:: cfxdb.mrealmschema.MrealmSchema
    :members:
    :undoc-members:

Database Tables
---------------

Application Realms
..................

* :class:`cfxdb.mrealm.ApplicationRealm`
* :class:`cfxdb.mrealmschema.ApplicationRealms`
* :class:`cfxdb.mrealmschema.IndexApplicationRealmByName`
* :class:`cfxdb.mrealmschema.IndexApplicationRealmByWebCluster`
* :class:`cfxdb.mrealm.ApplicationRealmRoleAssociation`
* :class:`cfxdb.mrealmschema.ApplicationRealmRoleAssociations`
* :class:`cfxdb.mrealmschema.Principal`
* :class:`cfxdb.mrealmschema.Principals`
* :class:`cfxdb.mrealmschema.IndexPrincipalByName`
* :class:`cfxdb.mrealmschema.Credential`
* :class:`cfxdb.mrealmschema.Credentials`
* :class:`cfxdb.mrealmschema.IndexCredentialsByAuth`
* :class:`cfxdb.mrealmschema.IndexCredentialsByPrincipal`
* :class:`cfxdb.mrealm.Role`
* :class:`cfxdb.mrealmschema.Roles`
* :class:`cfxdb.mrealmschema.IndexRoleByName`
* :class:`cfxdb.mrealm.Permission`
* :class:`cfxdb.mrealmschema.Permissions`
* :class:`cfxdb.mrealmschema.IndexPermissionByUri`
