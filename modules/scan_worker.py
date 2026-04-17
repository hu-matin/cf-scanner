from queue import Queue
import threading

from .ping_scanner import scan_ping
from .port_checker import check_port
from .domain_resolver import resolve_domain
from .create_result import write_result
from .screen_display import render_row

results_lock = threading.Lock()


def run_scanner(ip_queue: Queue, output_file: str, counters: dict, results: dict):
    while not ip_queue.empty():
        try:
            index, ip = ip_queue.get_nowait()
        except Exception:
            break

        ping_result = scan_ping(ip)
        port80_result = check_port(ip, 80)
        port443_result = check_port(ip, 443)
        domain_name = resolve_domain(ip) if ping_result == 0 else "No"

        line = render_row(
            index,
            ip,
            ping_result,
            port80_result,
            port443_result,
            domain_name,
        )

        with results_lock:
            results[index] = line

        if ping_result == 0:
            write_result(ip, output_file)
            counters["live"] += 1
        else:
            counters["dead"] += 1

        ip_queue.task_done()