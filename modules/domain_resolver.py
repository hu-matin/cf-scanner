import socket


def resolve_domain(ip: str, max_len: int = 35) -> str:
    try:
        host = socket.gethostbyaddr(ip)[0]
        return host[:max_len]
    except Exception:
        return "No"