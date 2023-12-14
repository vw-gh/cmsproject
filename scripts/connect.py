# Команди запуска з cmd, для нагадування
# cmd openvpn --config C:\Users\Vitalii\OpenVPN\config\gagarina.ovpn --auth-user-pass "auth.txt"
# cmd openvpn-gui --config_dir "C:\Users\Vitalii\OpenVPN\config" --connect smartovpn.ovpn
import os
import subprocess
from auth import keys


ovpn = keys.ovpn

def connect(ovpn):
    ovpn_dir = 'C:\\Program Files\\OpenVPN\\bin\\'
    ovpn_config_dir = 'C:\\Users\\Vitalii\\OpenVPN\\config\\'
    os.chdir(ovpn_dir)

    # disconnect
    command = ' '.join(('openvpn-gui', '--command', 'disconnect_all'))
    subprocess.run(command, shell=True, encoding='utf-8')

    # connect
    command = ' '.join(('openvpn-gui', '--config_dir', ovpn_config_dir, '--connect', ovpn))
    subprocess.run(command, shell=True, encoding='utf-8')

