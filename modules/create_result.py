def write_result(ip: str, filename: str = "actives.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(ip + "\n")