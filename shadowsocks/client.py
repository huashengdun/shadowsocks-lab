#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, \
    with_statement

import json
import logging
import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from shadowsocks.eventloop import EventLoop
from shadowsocks.tcprelay import TcpRelay, TcpRelayClientHanler


FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def main():
    config_file = sys.argv[1] if len(sys.argv) > 1 else 'config.json'
    config = json.load(open(config_file))
    listen_addr = (config['local_address'], config['local_port'])
    remote_addr = (config['server'], config['server_port'])
    method = config['method']
    password = config['password']
    log_level = config.get('log-level', 'INFO').upper()
    log_file = config.get('log-file')
    logging.basicConfig(level=getattr(logging, log_level), format=FORMATTER,
                        filename=log_file)

    loop = EventLoop()
    relay = TcpRelay(TcpRelayClientHanler, listen_addr, method, password,
                     remote_addr)
    relay.add_to_loop(loop)
    loop.run()


if __name__ == '__main__':
    main()
