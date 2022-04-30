DATA1 = {
    'authextra': {
        'transport': {
            'channel_framing':
            'websocket',
            'channel_id': {},
            'channel_serializer':
            None,
            'channel_type':
            'tcp',
            'http_cbtid':
            'ch0oFqC4EQMCqpYmj/78bQ5D',
            'http_headers_received': {
                'cache-control': 'no-cache',
                'connection': 'Upgrade',
                'host': 'localhost:8080',
                'pragma': 'no-cache',
                'sec-websocket-extensions': 'permessage-deflate; '
                'client_no_context_takeover; '
                'client_max_window_bits',
                'sec-websocket-key': 'FG9K1Vx44MqEE9c37YgPEw==',
                'sec-websocket-protocol': 'wamp.2.json',
                'sec-websocket-version': '13',
                'upgrade': 'WebSocket',
                'user-agent': 'AutobahnPython/22.4.1.dev7'
            },
            'http_headers_sent': {
                'Set-Cookie': 'cbtid=ch0oFqC4EQMCqpYmj/78bQ5D;max-age=604800'
            },
            'is_secure':
            False,
            'is_server':
            True,
            'own':
            None,
            'own_fd':
            -1,
            'own_pid':
            28806,
            'own_tid':
            28806,
            'peer':
            'tcp4:127.0.0.1:48812',
            'peer_cert':
            None,
            'websocket_extensions_in_use': [{
                'client_max_window_bits': 13,
                'client_no_context_takeover': False,
                'extension': 'permessage-deflate',
                'is_server': True,
                'mem_level': 5,
                'server_max_window_bits': 13,
                'server_no_context_takeover': False
            }],
            'websocket_protocol':
            'wamp.2.json'
        },
        'x_cb_node': 'intel-nuci7-28788',
        'x_cb_peer': 'unix',
        'x_cb_pid': 28797,
        'x_cb_worker': 'test_router1'
    },
    'authid': 'client1',
    'authmethod': 'anonymous-proxy',
    'authprovider': 'static',
    'authrole': 'frontend',
    'session': 941369063710961,
    'transport': {
        'channel_framing': 'rawsocket',
        'channel_id': {},
        'channel_serializer': 'cbor',
        'channel_type': 'tcp',
        'http_cbtid': None,
        'http_headers_received': None,
        'http_headers_sent': None,
        'is_secure': False,
        'is_server': None,
        'own': None,
        'own_fd': -1,
        'own_pid': 28797,
        'own_tid': 28797,
        'peer': 'unix',
        'peer_cert': None,
        'websocket_extensions_in_use': None,
        'websocket_protocol': 'wamp.2.cbor'
    }
}

from cfxdb.realmstore import AppSession
