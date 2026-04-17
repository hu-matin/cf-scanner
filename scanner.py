from colorama import Fore, Style
import time
import threading
from queue import Queue

from modules.banner import banner
from modules.ip_reader import read_ranges
from modules.scan_worker import run_scanner, results_lock
from modules.state_reporter import final_report


def printer_thread(results: dict, total: int):
    current = 1
    while current <= total:
        with results_lock:
            line = results.get(current)
        if line:
            print(line)
            current += 1
        else:
            time.sleep(0.01)


def main():
    banner()

    target_file = input(f"{Fore.YELLOW}Enter the IPs file by (.txt) format or type (hosts.txt): {Fore.WHITE}")
    ip_list = read_ranges(target_file)

    if not ip_list:
        print(f"{Fore.RED}No IPs' file found!{Style.RESET_ALL}")
        return

    threads_input = input(f"{Fore.YELLOW}Enter a number for threading or type (50): {Fore.WHITE}")
    max_threads = int(threads_input) if threads_input.strip() else 50

    counters = {"live": 0, "dead": 0, "total": len(ip_list)}
    results = {}

    print(f"\n{Fore.CYAN}{counters['total']:,} targets | {max_threads} threads")
    print(f"{Fore.BLUE}{'─' *60}\n")

    start = time.time()
    ip_queue = Queue()

    for idx, ip in enumerate(ip_list, 1):
        ip_queue.put((idx, ip))

    open("actives.txt", "w").close()

    workers = []
    for _ in range(max_threads):
        t = threading.Thread(
            target=run_scanner,
            args=(ip_queue, "actives.txt", counters, results),
            daemon=True,
        )
        t.start()
        workers.append(t)

    printer = threading.Thread(
        target=printer_thread,
        args=(results, counters["total"]),
        daemon=True,
    )
    printer.start()

    ip_queue.join()
    printer.join()

    elapsed = time.time() - start
    final_report(counters, elapsed)


if __name__ == "__main__":
    main()