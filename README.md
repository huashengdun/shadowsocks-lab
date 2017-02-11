# shadowsocks-lab

Simplified shadowsocks base on https://pypi.python.org/pypi/shadowsocks.

## how to use

On client side, change LISTEN_ADDR and REMOTE_ADDR in client.py as needed, then run

$ python client.py

On server side, change LISTEN_ADDR in server.py as needed, then run

$ python server.py

Also don't forget to change the encryption password and method on line 43 of tcprelay.py.
