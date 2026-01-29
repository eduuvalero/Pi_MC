import curses
from utils.menu_utils import select_menu

OPTIONS = [
    ("paper", "Paper (Recommended)"),
    ("fabric", "Fabric (Mods)"),
    ("vanilla", "Vanilla (Official)"),
    ("exit", "Exit")
]

def menu(stdscr):
    a = select_menu(stdscr, "Minecraft Version",OPTIONS)
    return a

def run_server_menu():
    return curses.wrapper(menu)