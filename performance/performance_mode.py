from performance.performance_menu import run_performance_menu
from performance.auto import run_auto
from performance.manual import run_manual

def performance_mode():
    option = run_performance_menu()

    match option:
        case "A":
            mode = run_auto()
        case "M":
            mode = run_manual()

    return mode