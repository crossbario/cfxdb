Database Schema
===============

.. contents:: :local:

---------------


.. autoclass:: cfxdb.mrealmschema.MrealmSchema
    :members:
        attach,
        roles,
        idx_roles_by_name,
        permissions,
        idx_permissions_by_uri,
        arealms,
        idx_arealms_by_name,
        idx_arealm_by_webcluster,
        arealm_role_associations,
        principals,
        idx_principals_by_name,
        credentials,
        idx_credentials_by_auth,
        idx_credentials_by_principal,
        routerclusters,
        idx_routerclusters_by_name,
        routercluster_node_memberships,
        router_workergroups,
        idx_workergroup_by_cluster,
        router_workergroup_placements,
        idx_clusterplacement_by_workername,
        webclusters,
        idx_webclusters_by_name,
        webcluster_node_memberships,
        webservices,
        idx_webservices_by_path,
        mnode_logs,
        mworker_logs
