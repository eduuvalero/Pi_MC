import curses

def select_menu(stdscr, titles, options):
    curses.curs_set(0)
    stdscr.keypad(True)
    current = 0

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

        for i, line in enumerate(title):
            stdscr.addstr(i, 0, line, curses.A_BOLD)

        y=0
        if titles.startswith("Do you want to make this server portable"):
            stdscr.addstr(len(title) + 2, 2, "(It starts the server automatically as soon as the Rapsberry PI is ON and creates a private Wi-Fi network)")
            y=1

        stdscr.addstr(len(title) + 1, 2, titles, curses.A_BOLD)
        stdscr.addstr(len(title) + y + 2, 3, "Use ↑ ↓ y Enter\n")

        x=0
        if titles.startswith("Select RAM for Minecraft Server"):
            stdscr.addstr(len(title) + y + 4, 2, " SERVER RAM | Recommendated PI model\n")
            x=1

        for i, (_, label) in enumerate(options):
            if i == current:
                stdscr.addstr(len(title) + i + x + y + 4, 3, label, curses.A_REVERSE)
            else:
                stdscr.addstr(len(title) + i + x + y + 4, 3, label)

        key = stdscr.getch()

        if key == curses.KEY_UP and current > 0:
            current -= 1
        elif key == curses.KEY_DOWN and current < len(options) - 1:
            current += 1
        elif key in (10, 13): 
            return options[current][0] 



