import os
import subprocess
from pathlib import Path
from utils.paths import SERVER_DIR

user = os.environ.get("SUDO_USER") or os.environ.get("USER")

def setup_portable_autostart():
  service_path = "/etc/systemd/system/portable-minecraft.service"

  service_config = f"""[Unit]
Description=Portable Minecraft Server
After=network.target

[Service]
Type=simple
User={user}
WorkingDirectory={SERVER_DIR}
ExecStart=/bin/bash {SERVER_DIR}/start
ExecStop=/bin/kill -SIGTERM $MAINPID
Restart=always
RestartSec=3
KillSignal=SIGTERM

[Install]
WantedBy=multi-user.target
"""

  Path(service_path).write_text(service_config)

  subprocess.run(["systemctl", "daemon-reload"], check=True)
  subprocess.run(["systemctl", "enable", "portable-minecraft.service"], check=True)
  subprocess.run(["systemctl", "start", "portable-minecraft.service"], check=True)

  print("Autostart successfully configured")

def setup_portable_wifi(wifi_name, wifi_password):
  netplan_path = "/etc/netplan/10-portable-minecraft.yaml"

  netplan_config = f"""network:
  version: 2
  renderer: NetworkManager
  ethernets:
    eth0:
      dhcp4: true
      optional: true
  wifis:
    wlan0:
      dhcp4: true
      optional: true
      addresses:
        - 10.42.0.1/24
      access-points:
        "{wifi_name}":
          password: "{wifi_password}"
          mode: ap
"""

  Path(netplan_path).write_text(netplan_config)

  subprocess.run([
        "bash", "-c",
        "echo 'network: {config: disabled}' > /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg"
    ], check=True)

  subprocess.run(["netplan", "generate"], check=True)
  subprocess.run(["netplan", "apply"], check=True)

  script_content = f"""SSID: {wifi_name}
Passowrd: {wifi_password}
    """
  path = os.path.join(SERVER_DIR, "wifi_credentials.txt")

  with open(path, "w") as f:
    f.write(script_content)

  print(f"Your Wwi-Fi name is: {wifi_name}")
  print(f"Your Wwi-Fi Passowrd is: {wifi_password}")
  print(f"If you forget the Wi-Fi credentials you can find them in: {path}")

  print("Portable wifi successfully configured”")

def setup_portable_server():
  print("Enter Wi-Fi network name for your portable server:")
  wifi_name = input("Wi-Fi Name (SSID): ").strip()
  if not wifi_name:
    wifi_name = "Raspberry PI"

  print("Enter Wi-Fi password:")
  wifi_password = input("Wi-Fi Password (Min 4 characters): ").strip()
  while(len(wifi_password) < 4):
    wifi_password = input("The Wi-Fi Passoword must have at minimum 4 charcters\nEnter anoter Wi-Fi Password: ").strip()

  print("etting up portable Wi-Fi...")
  setup_portable_wifi(wifi_name, wifi_password)

  print("Enabling server auto-start...")
  setup_portable_autostart()

  print("Portable mode enabled successfully!")
  print(f"Connect to Wi-Fi '{wifi_name}' to play!\nPassword: {wifi_password}")