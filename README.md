![alt text](https://github.com/eduuvalero/Pi_MC/blob/main/assets/PiMC.png)

# Pi MC

---
**Pi MC** is a lightweight Minecraft server installer designed specifically for the **Raspberry Pi**. It allows users to **install, optimize, and configure a fully functional Minecraft server** on their Pi with just a few clicks.

This project was created as my **first mini-project**, starting with limited experience in Python and computing. The goal was to make it **easy for anyone to run a Minecraft server** without having to manually deal with complex configurations, file structures, or performance tuning.

With Pi MC, you can:

- Set up a Minecraft server **quickly and reliably**.
- Optimize server settings such as **RAM, max players, and chunks**.
- Choose between **Fabric, Paper or Vanilla** server types and their version.
- Enjoy a **user-friendly, menu-driven interface** that guides you through installation and configuration.

Pi MC makes hosting a Minecraft server on a Raspberry Pi **accessible even for beginners**, turning what would normally be a complex process into a simple and intuitive experience.

---

- **Pi MC** is a free and open-source Minecraft server installer. However, Minecraft itself is not free, so we provide only the installer and not a pre-compiled server.
To use your Minecraft server, you must first accept the Minecraft EULA, available here: https://account.mojang.com/documents/minecraft_eula.
- Other projects used by Pi MC, such as Java, are under their own licenses. Pi MC functions solely as an installation and configuration tool and does not distribute any proprietary software.

---
## How to use Pi MC
Follow these steps to get your Raspberry Pi ready and install a functional Minecraft Server with Pi MC. This guide assumes you are using a **64-bit Raspberry Pi OS**.

### 1️. Update and Upgrade your system
```
sudo apt update && sudo apt upgrade -y
```
### 2. Read and install the requirements
You can find the [Requirements](https://github.com/eduuvalero/Pi_MC?tab=readme-ov-file#requirements) below
### 3. Clone Pi MC repository or donwload the pimc.tar.gz file
```
git clone https://github.com/eduuvaleroPi_MC
```
```
cd Pi_MC
```
### 4. Run Pi MC Installer
```
chmod +x pimc
```
```
./pimc
```
### 6. Control the server using screen
- Use the server console (You can put all the minecraft console commands here): 
```
screen -r pimc
```
- Exit server console without stopping the server: `Ctrl + A -> D`
### 5. Enjoy the server

Once you have ran the program, your Rapsberry PI will have a folder named `minecraft-server` with a file named `start` inside. To turn on the server just put the command `./start` inside the `minecraft-server`folder. 

If you want to enable the Portable mode click [Here](https://github.com/eduuvalero/Pi_MC?tab=readme-ov-file#enable-portable-server)

---

## Requirements

Before installing Pi MC, make sure your Raspberry Pi meets the following requirements:

### Hardware
- Raspberry Pi 4 or 5 recommended, but can work on Raspberry Pi 3B/3B+
- Minimum **1 GB RAM** (Recommended **4 GB** at least and **8 GB** or more to use fabric with mods)
- NVME or MicroSD card or external storage with enough space (at least 8 GB free recommended) and in severs with many plugins or mods or many players is recommended to use an NVME
- An adequate cooling

### System Requirements and Installation
- **Operating System:** Raspberry Pi OS (Recommended Raspberry OS Lite), Ubuntu Server or another Debian-based Linux. 
- **IMPORTANT**: Always use a 64-Bit OS to use the RAM effectively.

### Install Required Packages
- **Python 3.12+**, but it is usually already installed in Raspberry OS (for running the installer scripts)
```
sudo apt install -y python3.12
```
- **Requests and Psutil** (Python library)
```
sudo apt install python3-requests
```
```
sudo apt install python3-psutil
```
- **Screen** 
```
sudo apt install screen
```
- **Java 21+** for versions 1.21.+ or **Java 17+** for previous versions. The Raspberry PI needs Java for ARM:

> Using Raspberry OS or Ubuntu Server (ARM):
```
sudo apt install openjdk-21-jdk
```
- **Git** (to clone the repository)
```
sudo apt install git
```

---

## Supported versions
- **Paper:** From 1.21.11 to 1.12 + 1.11.2, 1.10.2, 1.9.4 and 1.8.8
- **Fabric:** From 1.21.11 to 1.14
- **Vanilla:** From 1.21.11 to 1.0.0

---

## Recommended Server Software

Pi MC supports the next Minecraft server software, each suited for different use cases:

### 1. **Paper (Recommended)**
**Paper** is our **highly recommended** choice for Raspberry Pi, and it is **required** for devices with **less than 8 GB RAM** or models **earlier than Raspberry Pi 4**.  

- A **fork of Spigot**, optimized for better performance and resource management.  
- Supports **plugins** without heavy resource usage.  
- Can run a **Vanilla-like server** more efficiently than the official Vanilla server.  
- Ideal for both **plugin-based servers** and **pure Vanilla gameplay**.  

**Advantages of Paper:**  
- Higher performance than Vanilla.  
- Compatible with most Spigot plugins.  
- Handles more players efficiently.  
- Active development and strong community support.  

---

### 2. **Fabric (for Lightweight Mods)**

**Fabric** is only recommended for **Raspberry Pi 4 or 5** with **8 GB RAM or more**:  

- Supports **lightweight mods**, but all players must also run Fabric.  
- Recommended only for **simple, low-resource mods**, due to Raspberry Pi hardware limitations.  
- Does not include the performance optimizations that Paper provides for Vanilla gameplay.  
- **Not suitable** for older or lower-RAM Raspberry Pi models.  

---

### 3. **Vanilla (Not Recommended)**

The official **Vanilla server** provides a pure Minecraft experience:  

- Unmodified, same as the game’s default server.  
- **No plugin support**, and not optimized for performance.  
- On Raspberry Pi, it works but **Paper usually performs better**, even without plugins.  
- Has older versions than Paper.

**Summary Table:**  

| Server Type | Best Use Case | Notes |
|------------|---------------|--------------------|
| **Paper** | General use, plugins, Vanilla, or many players | Recommended for all Raspberry Pi, required for <8GB RAM or <Pi 4 |
| **Fabric** | Lightweight mods | Only for Pi 4 or 5 with 8 GB RAM or more; players must have Fabric installed |
| **Vanilla** | Pure Minecraft or use very old versions | Not recommended on Raspberry Pi as Paper without plugins is the same but has much better performance|

---

## Server Requirements and Performance

| SERVER RAM | RASPBERRY PI MODEL | PI RAM | Paper | Fabric (Mods) | Vanilla |
|------------|------------------|--------|-------|---------------|---------|
| 512 MB     | Raspberry PI 3B  | 1 GB   | **1 - 2 Players** | No recommended    | No recommended  |
| 1 GB       | Raspberry PI 4   | 2 GB   | **2 - 4 Players** | No recommended     | No recommended  |
| 2 GB       | Raspberry PI 4   | 4 GB   | **4 - 6 Players** | No recommended     | No recommended  |
| 4 GB       | Raspberry PI 4   | 8 GB   | **6 - 8 Players** | 4 - 6 Players    | 4 - 6 Players |
| 4 GB       | Raspberry PI 5   | 8 GB   | **8-10 Players** | 6-8 Players    | 6-8 Players |
| 6 GB       | Raspberry PI 5   | 16 GB  | **10-15 Players**| 8 - 10 Players    | 8 - 10 Players |
| 8 GB       | Raspberry PI 5   | 16 GB  | **15 - 20 Players**| 10 - 15 Players   | 10 - 15 Players |

> **Recommendations:**  
> - **Raspberry Pi 3B:** Only suitable for tiny servers (1–2 players).  
> - **Raspberry Pi 4:** Best for small - medium servers (up to 8 players).  
> - **Raspberry Pi 5:** Ideal for medium servers and for using mods or plugins, especially with 8GB+ RAM.  
> - **Paper** always offers the best performance; **Vanilla** has the lowest player capacity due to overhead.  
> - **Fabric** is recommended only if you need mods, as it reduces max players compared to Paper.

---

## Networking

The Minecraft server installed by this installer **listens on port 25565 by default** and is configured to run **only within your local network (LAN)**.  

- Only devices connected to the same network as your Raspberry Pi can join.  
- The server **is not accessible from the Internet** by default.  

### Allowing Access from Outside Your LAN

There are **three main approaches**: opening a port on your router, using a private VPN (Tailscale) or cofigure the Rapsbrry Pi as a portblae sever with autostart and a private network.

---

### 1️.) Opening the Router Port (Port Forwarding)

- Forward TCP port 25565 to your server’s local IP.  
- Ensure your firewall allows incoming connections on this port.  
- Keep `online-mode=true` to enforce Mojang account verification.  
- ⚠ Exposing the server can allow attacks if the router/server is not secured.

---

### 2️.) Using Tailscale (Secure Private VPN)

- Creates a **private encrypted network** for you and your friends.  
- Works like a LAN over the Internet, **no need for port forwarding**.  
- Install Tailscale on Raspberry Pi and your friends’ devices.  
- Run `tailscale up` and share the IP with friends.  

---

### 3.) Making a Portable Server

One of the coolest things about the Raspberry Pi is that it is a **small, low-power ARM computer** that is **highly portable**. This makes it perfect for turning into a **portable Minecraft server** that you can take anywhere.  

With Pi MC you can configure the server as a Portable Server in the installation. 

- **The Minecraft server starts automatically when the Pi is powered on.**  
  Just plug it in, and your server is ready to play — no need to manually start it every time.  

- **The Raspberry Pi can create its own Wi-Fi hotspot.**  
  This allows other devices to connect directly to the Pi’s network. Any device that joins this Wi-Fi can immediately access the Minecraft server **without needing an external router or internet connection**.  

This setup is ideal for **mobile LAN parties or just a private server you can carry around to play with friends anywhere**. Thanks to the Pi’s portability and low power consumption, you can have a **full-featured Minecraft server in your pocket**, ready to play anywhere you go.  

### Enable portable server
- **IMPORTANT:** The **portable Wi-FI ONLY** works using **Ubuntu Server**, if you are using Rpasberry OS, you can only use the auto-start option

- Once you have installed correctly the Minecraft Server, if you want to configure it as a portable server put the next in your terminal:
```
chmod +x portable_mode
```
```
./portable_mode
```
> Essentially, your Raspberry Pi becomes a **self-contained, plug-and-play Minecraft server**, giving you the freedom to play with friends wherever you want — no internet required. 
> Once you activate the portable Wi-Fi the Rapsberry PI will no longer be able to connect to the internet
