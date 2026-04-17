import socket


def check_port(ip: str, port: int, timeout: int = 1) -> int:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result
    except Exception:
        return 1