import os
from .ip import generate_ips


def read_ranges(filename: str):
    if not os.path.exists(filename):
        return []

    all_ips = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            line = line.strip()
            if line:
                ips = generate_ips(line)
                all_ips.extend(ips)
    return all_ips