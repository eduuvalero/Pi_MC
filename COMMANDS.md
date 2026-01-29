# Minecraft with auto-start basic commands:
- **Acces server terminal:** screen -r pimc
- **Status:** sudo systemctl status portable-minecraft.service
- **Console:** sudo journalctl -u portable-minecraft.service -f
- **Stop:** sudo systemctl stop portable-minecraft.service
- **Start:** sudo systemctl start portable-minecraft.service
- **Restart server:** sudo systemctl restart portable-minecraft.service
- **Disbale auto-stat:** sudo systemctl disable portable-minecraft.service
- **Enable auto-start:** sudo systemctl enable portable-minecraft.service
