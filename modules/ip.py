def generate_ips(cidr: str):
    try:
        base_ip, mask = cidr.split("/")
        parts = base_ip.split(".")
        ip_prefix = ".".join(parts[:3])
        return [f"{ip_prefix}.{i}" for i in range(1, 255)]
    except Exception:
        return []