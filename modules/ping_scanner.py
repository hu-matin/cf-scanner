import socket
import struct
import time
import os


def checksum(data: bytes) -> int:
    if len(data) % 2:
        data += b"\x00"
    total = 0
    for i in range(0, len(data), 2):
        total += (data[i] << 8) + data[i + 1]
    total = (total >> 16) + (total & 0xFFFF)
    total += (total >> 16)
    return ~total & 0xFFFF


def build_icmp_echo(seq: int = 1) -> bytes:
    pid = os.getpid() & 0xFFFF
    header = struct.pack("!BBHHH", 8, 0, 0, pid, seq)
    payload = struct.pack("!d", time.monotonic())
    chksum = checksum(header + payload)
    header = struct.pack("!BBHHH", 8, 0, chksum, pid, seq)
    return header + payload


def scan_ping(ip: str, timeout: float = 1.0) -> int:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.settimeout(timeout)
    except PermissionError:
        return 1
    except Exception:
        return 1

    try:
        packet = build_icmp_echo(seq=1)
        start = time.monotonic()
        sock.sendto(packet, (ip, 0))

        while True:
            try:
                data, addr = sock.recvfrom(1024)
            except socket.timeout:
                return 1

            recv_time = time.monotonic()
            icmp_header = data[20:28]
            icmp_type, code, _, recv_id, recv_seq = struct.unpack("!BBHHH", icmp_header)
            if icmp_type == 0:
                _ = (recv_time - start) * 1000
                return 0
    except Exception:
        return 1
    finally:
        sock.close()