import curses
from utils.menu_utils import select_menu

OPTIONS = [
    ("N", "NO"),
    ("Y", "YES (Portable Server)"),
    ("A", "AUTO-START: You only want auto-start (Without private Wi-Fi)")
]

def menu(stdscr):
    a = select_menu(stdscr, "Do you want to make this server portable (Auto-start + Private Wi-Fi)?",OPTIONS)
    if a == 'Y':
        OPTION = [
            ("Y", "YES"),
            ("N", "NO")
        ]
        a = select_menu(stdscr, "ARE YOU SURE?",OPTION)
    elif a == 'A':
        OPTION = [
            ("A", "YES"),
            ("N", "NO")
        ]
        a = select_menu(stdscr, "ARE YOU SURE?",OPTION)
    return a

def run_portable_menu():
    return curses.wrapper(menu)