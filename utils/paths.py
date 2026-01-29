import os
import pwd
import getpass

def get_real_user():
    return os.environ.get("SUDO_USER") or getpass.getuser()

def get_user_home():
    user = get_real_user()
    return pwd.getpwnam(user).pw_dir

SERVER_DIR = os.path.join(get_user_home(), "minecraft-server")
SERVER_JAR = "server.jar"