import subprocess
import platform


def scan_ping(ip: str, timeout: int = 1) -> int:
    system = platform.system().lower()
    param = "-n" if system == "windows" else "-c"
    timeout_param = "-w" if system == "windows" else "-W"

    cmd = ["ping", param, "1", timeout_param, str(timeout), ip]
    proc = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return proc.returncode