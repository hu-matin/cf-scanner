from colorama import Fore, Style


def final_report(counters: dict, duration: float):
    print(Fore.GREEN + "─" * 60 + Style.RESET_ALL)
    print(f"{Fore.MAGENTA}Scan reportation{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Total: {counters['total']:>7}")
    print(f"{Fore.GREEN}Live: {counters['live']:>7}")
    print(f"{Fore.RED}Dead: {counters['dead']:>7}")
    print(f"{Fore.YELLOW}Time: {duration:>7.2f} s{Style.RESET_ALL}")
    print(Fore.GREEN + "─" * 60 + Style.RESET_ALL)



