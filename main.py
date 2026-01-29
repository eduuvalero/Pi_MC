from configuration.server_menu import run_server_menu
from configuration.version_menu import run_version_menu
from configuration.config_menu import run_config_menu
from performance.performance_mode import performance_mode 
from installation.installer import install


server = run_server_menu()
version = run_version_menu(server)
config = run_config_menu()
performance = performance_mode()

install(version, server, config, performance)