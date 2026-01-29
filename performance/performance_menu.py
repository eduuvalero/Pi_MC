import curses
from utils.menu_utils import select_menu

OPTIONS = [
    ("A", "Automatic configuration (Recommended)"),
    ("M", "Configure performance manually")
]

def menu(stdscr):
    a = select_menu(stdscr, "Server performance",OPTIONS)
    return a

def run_performance_menu():
    return curses.wrapper(menu)