from portable.portable_menu import run_portable_menu 
from portable.portable_mode import setup_portable_server, setup_portable_autostart 

portable_mode = run_portable_menu()
if portable_mode == "Y":
    setup_portable_server()
elif portable_mode == "A":
    setup_portable_autostart ()