import curses
from configuration.versions import version

def menu(stdscr, versions):
    curses.curs_set(0)
    stdscr.keypad(True)
    current = 0
    offset = 0  

    title = [
        " _______   _    ____     ____   ______ ",
        "|_   __ \ (_)   |_   \  /   _|.' ___  | ",
        "  | |__) |__      |   \/   | / .'   \_| ",
        "  |  ___/[  |     | |\  /| | | |        ",
        " _| |_    | |    _| |_\/_| |_\ `.___.'\ ",
        "|_____|  [___]  |_____||_____|`.____ .' "                                   
    ]

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for i, line in enumerate(title):
            stdscr.addstr(i, 0, line, curses.A_BOLD)

        stdscr.addstr(len(title) + 1, 2, "Minecraft Version", curses.A_BOLD)
        stdscr.addstr(len(title) + 2, 3, "Use ↑ ↓ and Enter\n")

        max_display = h - (len(title) + 4)

        if current < offset:
            offset = current
        elif current >= offset + max_display:
            offset = current - max_display + 1

        for i, label in enumerate(versions[offset:offset + max_display]):
            idx = offset + i
            if idx == current:
                stdscr.addstr(len(title) + 4 + i, 3, label, curses.A_REVERSE)
            else:
                stdscr.addstr(len(title) + 4 + i, 3, label)

        key = stdscr.getch()
        if key == curses.KEY_UP and current > 0:
            current -= 1
        elif key == curses.KEY_DOWN and current < len(versions) - 1:
            current += 1
        elif key in (10, 13): 
            return versions[current]

def run_version_menu(server):
    versions = version(server)
    return curses.wrapper(menu, versions)