import psutil
from utils.menu_utils import select_menu

config = {}

total_ram_gb = psutil.virtual_memory().total / (1024 ** 3)
assigned_ram_gb = total_ram_gb * 0.5 
assigned_ram_str = (
    f"{int(assigned_ram_gb)}G" if assigned_ram_gb >= 1 else f"{int(assigned_ram_gb * 1024)}M"
)

def sim_distance(ram_gb):
    if ram_gb <= 2:
        return 1
    elif ram_gb <= 4:
        return 2
    elif ram_gb <= 8:
        return 4
    else:
        return 5

def view_distance(ram_gb):
    if ram_gb <= 1:
        return 2
    elif ram_gb <= 2:
        return 4
    elif ram_gb <= 4:
        return 6
    elif ram_gb <= 8:
        return 8
    else:
        return 10

def max_players(ram_gb):
    if ram_gb <= 1:
        return 4
    elif ram_gb <= 2:
        return 5
    elif ram_gb <= 4:
        return 8
    elif ram_gb <= 8:
        return 10
    else:
        return 20

def run_auto():
    config["sim-distance"] = sim_distance(total_ram_gb)
    config["view-distance"] = view_distance(total_ram_gb)
    config["max-players"] = max_players(total_ram_gb)
    config["ram"] = assigned_ram_str

    return config
