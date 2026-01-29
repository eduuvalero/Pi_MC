import requests
from utils.paths import SERVER_DIR, SERVER_JAR

SERVER = f"{SERVER_DIR}/{SERVER_JAR}"

def paper(version):
    API = "https://api.papermc.io/v2"

    r = requests.get(f"{API}/projects/paper/versions/{version}")
    builds = r.json()["builds"]
    latest_build = builds[-1]

    r = requests.get(f"{API}/projects/paper/versions/{version}/builds/{latest_build}")
    jar = r.json()["downloads"]["application"]["name"]

    download_url = (
    f"{API}/projects/paper/versions/{version}"
    f"/builds/{latest_build}/downloads/{jar}"
    )

    print(f"Downloading Paper {version} from: {download_url}")

    r = requests.get(download_url, stream=True)
    r.raise_for_status()

    with open(SERVER, "wb") as f:
            f.write(r.content)

def vanilla(version):
    MANIFEST = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

    data = requests.get(MANIFEST).json()

    version_info = next(
        v for v in data["versions"] if v["id"] == version
    )

    version_data = requests.get(version_info["url"]).json()

    download_url = version_data["downloads"]["server"]["url"]

    print(f"Downloading Vanilla {version} from: {download_url}")

    r = requests.get(download_url, stream=True)
    r.raise_for_status()

    with open(SERVER, "wb") as f:
        f.write(r.content)

def fabric(version):
    download_url = f"https://meta.fabricmc.net/v2/versions/loader/{version}/0.18.4/1.1.1/server/jar"

    print(f"Downloading Fabric {version} from: {download_url}")

    r = requests.get(download_url, stream=True)
    r.raise_for_status()

    with open(SERVER, "wb") as f:
        f.write(r.content)

def download(server, version):
    match server:
        case "paper":
            paper(version)
        case "fabric":
            fabric(version)
        case "vanilla":
            vanilla(version)

    print(f"{server.title()} {version} downloaded in {SERVER_DIR}")