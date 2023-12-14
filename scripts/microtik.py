from librouteros import connect
from librouteros.query import Key
import ssl
from auth import keys


def get_ip(router_ip, mac):
    username = keys.username  # Имя пользователя
    password = keys.password  # Пароль
    port = 8729
    connection = None

    try:
        # Устанавливаем соединение с MikroTik
        # connection = connect(username=username, password=password, host=router_ip)

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.set_ciphers('ADH:@SECLEVEL=0')
        connection = connect(
            username=username,
            password=password,
            host=router_ip,
            ssl_wrapper=ctx.wrap_socket,
            port=port
        )

        # Each key must be created first in order to reference it later.
        address = Key('address')
        mac_address = Key('mac-address')

        ip, *_ = connection.path('/ip/arp').select(address).where(mac_address == mac)
        return ip.get('address')


    except Exception as e:
        return f"Ошибка при подключении к MikroTik: {e}"
    finally:
        if connection is not None:
            # Закрываем соединение
            connection.close()


