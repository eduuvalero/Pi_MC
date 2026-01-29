import os
import subprocess
import json
import urllib.request
import time

from utils.paths import SERVER_DIR, SERVER_JAR
from installation.donwloader import download

def write_server_properties(config, config_per):
    os.makedirs(SERVER_DIR, exist_ok=True)

    props = {
        "difficulty": config["difficulty"],
        "gamemode": config["gamemode"],
        "hardcore": config["hardcore"],
        "online-mode": config["online_mode"],
        "max-players": config_per["max-players"],
        "simulation-distance=": config_per["sim-distance"],
        "view-distance": config_per["view-distance"]
    }

    file_path = os.path.join(SERVER_DIR, "server.properties")

    with open(file_path, "w") as f:
        for k, v in props.items():
            f.write(f"{k}={v}\n")

def ensure_server_dir():
    os.makedirs(SERVER_DIR, exist_ok=True)

def write_eula():
    eula_path = os.path.join(SERVER_DIR, "eula.txt")
    with open(eula_path, "w") as f:
        f.write("eula=true\n")


def write_start_script(config):
    ram = config["ram"]

    script_content = f"""#!/bin/bash
screen -DmS pimc java -Xms{ram} -Xmx{ram} -jar server.jar nogui
    """
    script_path = os.path.join(SERVER_DIR, "start")

    with open(script_path, "w") as f:
        f.write(script_content)

    os.chmod(script_path, 0o755)

def first_run(version, server):

    print("-"*85)
    print(f"   Installing {server.title()} {version} | This process will take a minute, don't do anything")
    print("-"*85)

    process = subprocess.Popen(
        ["java", "-jar", SERVER_JAR, "nogui"],
        cwd=SERVER_DIR,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,  
        stderr=subprocess.DEVNULL,
        text=True
    )

    time.sleep(45)

    process.stdin.write("stop\n")
    process.stdin.flush()
    process.wait()

def install(version, server, config, performance):
    print("-" * 20 + "\n  " + server.upper() + " | " +  version + "\n" + "-" * 20)

    write_server_properties(config, performance)
    ensure_server_dir()
    download(server, version)
    write_eula()
    write_start_script(performance)
    first_run(version, server)

    print(f"✅ {server.title()} installed and ready to use")