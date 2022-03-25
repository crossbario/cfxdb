Management Domain
=================

The domain controller running on the master node stores its configuration and run-time
information in an embedded database

.. contents:: :local:

.. note::

    There exists only one domain controller database per master node. This database is separate
    from all managament realm controller databases, and only used to book keep users, Management
    realms and paired nodes. All configuration and management within a given management realm is
    then stored in the management realm controller database dedicated to the respective realm.

-------


Database Schema
---------------

.. autoclass:: cfxdb.globalschema.GlobalSchema
    :members:
        attach,
        nodes,
        idx_nodes_by_pubkey,
        idx_nodes_by_authid,
        organizations,
        idx_organizations_by_name,
        idx_users_by_pubkey,
        idx_users_by_email,
        activation_tokens,
        idx_act_tokens_by_authid_pubkey,
        mrealms,
        idx_mrealms_by_name,
        users,
        users_mrealm_roles,
        usage


Metadata Tables
---------------

.. autoclass:: cfxdb.common.ConfigurationElement
    :members:
    :show-inheritance:


User Tables
-----------

.. autoclass:: cfxdb.user.User
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.Users
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.IndexUsersByName
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.IndexUsersByPubkey
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.IndexUsersByEmail
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.user.UserMrealmRole
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.UserMrealmRoles
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.user.ActivationToken
    :members:

.. autoclass:: cfxdb.globalschema.ActivationTokens
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.IndexActivationTokensByAuthidPubkey
    :members:
    :show-inheritance:


Organization Tables
-------------------

.. autoclass:: cfxdb.user.Organization
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.Organizations
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.IndexOrganizationsByName
    :members:
    :show-inheritance:


Management Realm Tables
-----------------------

.. autoclass:: cfxdb.mrealm.ManagementRealm
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.ManagementRealms
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.IndexManagementRealmByName
    :members:
    :show-inheritance:


Node Tables
-----------

.. autoclass:: cfxdb.mrealm.Node
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.Nodes
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.IndexNodesByPubkey
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.IndexNodesByAuthid
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.usage.MasterNodeUsage
    :members:
    :show-inheritance:

.. autoclass:: cfxdb.globalschema.UsageRecords
    :members:
    :show-inheritance:
