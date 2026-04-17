from colorama import Fore, Style
import shutil


def get_terminal_width(default: int = 120) -> int:
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return default


TERM_WIDTH = get_terminal_width()

COL_IDX_WIDTH = 3
COL_IP_WIDTH = 18
COL_PING_WIDTH = 6
COL_P80_WIDTH = 6
COL_P443_WIDTH = 6
BASE_COL_DOMAIN_WIDTH = 25

if TERM_WIDTH < 80:
    COL_DOMAIN_WIDTH = 12
elif TERM_WIDTH < 100:
    COL_DOMAIN_WIDTH = 18
else:
    COL_DOMAIN_WIDTH = BASE_COL_DOMAIN_WIDTH

HEADER_PRINTED = False


def build_data_row(idx, ip, ping, http, https, domain):
    return (
        f"[{idx:>{COL_IDX_WIDTH}d}]  "
        f"{ip:<{COL_IP_WIDTH}}  "
        f"{ping:>{COL_PING_WIDTH}}  "
        f"{http:>{COL_P80_WIDTH}}  "
        f"{https:>{COL_P443_WIDTH}}  "
        f"{domain:<{COL_DOMAIN_WIDTH}}"
    )


def build_header_row():
    return (
        f"[{'#':>{COL_IDX_WIDTH}}]  "
        f"{'IP':<{COL_IP_WIDTH}}  "
        f"{'PING':>{COL_PING_WIDTH}}  "
        f"{'HTTP':>{COL_P80_WIDTH}}  "
        f"{'HTTPS':>{COL_P443_WIDTH}}  "
        f"{'DOMAIN':<{COL_DOMAIN_WIDTH}}"
    )


def print_header():
    global HEADER_PRINTED
    if HEADER_PRINTED:
        return
    HEADER_PRINTED = True

    header = build_header_row()
    print(Fore.MAGENTA + header + Style.RESET_ALL)
    print(Fore.MAGENTA + "─" * len(header) + Style.RESET_ALL)


def render_row(index, ip, ping_code, port80_code, port443_code, domain):
    print_header()

    ping_text = "Ok" if ping_code == 0 else "Fail"
    p80_text = "Open" if port80_code == 0 else "Close"
    p443_text = "Open" if port443_code == 0 else "Close"
    domain = (domain or "No")[:COL_DOMAIN_WIDTH]

    _ = build_data_row(index, ip, ping_text, p80_text, p443_text, domain)

    colored_row = (
        Fore.WHITE + "[" + f"{index:>{COL_IDX_WIDTH}d}" + "]" + "  " +
        Fore.CYAN + f"{ip:<{COL_IP_WIDTH}}" + "  " +
        (Fore.GREEN if ping_code == 0 else Fore.RED) + f"{ping_text:>{COL_PING_WIDTH}}" + Style.RESET_ALL + "  " +
        (Fore.GREEN if port80_code == 0 else Fore.RED) + f"{p80_text:>{COL_P80_WIDTH}}" + Style.RESET_ALL + "  " +
        (Fore.GREEN if port443_code == 0 else Fore.RED) + f"{p443_text:>{COL_P443_WIDTH}}" + Style.RESET_ALL + "  " +
        Fore.YELLOW + f"{domain:<{COL_DOMAIN_WIDTH}}" + Style.RESET_ALL
    )

    return colored_row