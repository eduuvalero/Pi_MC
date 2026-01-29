import curses
from utils.menu_utils import select_menu

def config_menu(stdscr):
    config = {}

    config["difficulty"] = select_menu(
        stdscr,
        "Select Difficulty",
        [
            ("peaceful", "Peaceful"),
            ("easy", "Easy"),
            ("normal", "Normal (recommended)"),
            ("hard", "Hard")
        ]
    )

    config["gamemode"] = select_menu(
        stdscr,
        "Select Gamemode",
        [
            ("survival", "Survival"),
            ("adventure", "Adventure"),
            ("creative", "Creative"),
            ("spectator", "Spectator")
        ]
    )

    config["hardcore"] = (
        select_menu(
            stdscr,
            "Hardcore Mode",
            [
                ("false", "Disabled (Default)"), 
                ("true", "Enabled")
            ]
        )
    )

    config["online_mode"] = (
        select_menu(
            stdscr,
            "Mojang Authentication",
            [
                ("true", "Premium"), 
                ("false", "Offline")
            ]
        )
    )

    return config


def run_config_menu():
    return curses.wrapper(config_menu)