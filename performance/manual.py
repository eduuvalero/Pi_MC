import psutil
import curses
from utils.menu_utils import select_menu

config = {}

total_ram_gb = psutil.virtual_memory().total / (1024 ** 3)

assigned_ram_gb = total_ram_gb * 0.75 

assigned_ram_str = (
    f"{int(assigned_ram_gb)}G" if assigned_ram_gb >= 1 else f"{int(assigned_ram_gb * 1024)}M"
)

def ram_to_mb(ram_str):
    ram_str = ram_str.upper()
    if ram_str.endswith("G"):
        return int(ram_str[:-1]) * 1024
    elif ram_str.endswith("M"):
        return int(ram_str[:-1])
    else:
        raise ValueError("Formato de RAM inválido")

def optimize(stdscr):
    title = "Server RAM"

    while True:
        config["ram"] = select_menu(
            stdscr,
            title,
            [
                ("512M", "  512 MB   |  Raspberry PI 3B"),
                ("1G", "   1 GB    |  Raspberry PI 4"),
                ("2G", "   2 GB    |  Raspberry PI 4/5"),
                ("3G", "   3 GB    |  Raspberry PI 4/5"),
                ("4G", "   4 GB    |  Raspberry Pi 4/5"),
                ("5G", "   5 GB    |  Raspberry Pi 4/5"),
                ("6G", "   6 GB    |  Raspberry Pi 5"),
                ("7G", "   7 GB    |  Raspberry Pi 5"),
                ("8G", "   8 GB    |  Raspberry Pi 5"),
                ("9G", "   9 GB    |  Raspberry Pi 5"),
                ("10G", "   10 GB   |  Raspberry Pi 5"),
                ("11G", "   11 GB   |  Raspberry Pi 5"),
                ("12G", "   12 GB   |  Raspberry Pi 5")
            ]
        )
        if ram_to_mb(config["ram"]) <= ram_to_mb(assigned_ram_str):
            break
        else:
            title = f"Server RAM | ERROR: Selected RAM exceeds maximun available RAM ({assigned_ram_str})"

    config["max-players"] = select_menu(
        stdscr,
        "Max Players",
        [
        (1, "1 player"),
        (5, "5 players"),
        (10, "10 players"),
        (15, "15 players"),
        (20, "20 players"),
        (25, "25 players"),
        (30, "30 players"),
        (35, "35 players"),
        ]
    )

    config["sim-distance"] = select_menu(
        stdscr,
        "Simulation distance",
        [
        (1, "1 chunk"),
        (2, "2 chunk"),
        (4, "4 chunk"),
        (6, "6 chunk"),
        (8, "8 chunk"),
        (10, "10 chunk"),
        (12, "12 chunk"),
        (14, "14 chunk"),
        (16, "16 chunk")
        ]
    )

    config["view-distance"] = select_menu(
        stdscr,
        "View/Render distance",
        [
        (1, "1 chunk"),
        (2, "2 chunk"),
        (4, "4 chunk"),
        (6, "6 chunk"),
        (8, "8 chunk"),
        (10, "10 chunk"),
        (12, "12 chunk"),
        (14, "14 chunk"),
        (16, "16 chunk"),
        (18, "18 chunk"),
        (20, "20 chunk")
        ]
    )

    return config

def run_manual():
    return curses.wrapper(optimize)
