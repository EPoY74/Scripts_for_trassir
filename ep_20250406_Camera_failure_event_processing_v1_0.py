#  Принимает и обрабатыывает события от сервера видеонаблюдения trassir
#  и записывает их в файл.
#  Работает только непосредственно на серверах
#  trassir или на  trassir client для ПК

import os
import time

"""
<parameters>
        <company>EugeniiPetrov</company>
        <title>Receive_events</title>
        <version>1.0</version>
</parameters>
"""


events_to_handle = [
    "Signal Lost",
    "Signal Restored",
    "Disks Too Slow",
    "Connection Established",
    "Connection Lost",
]
# /home/trassir/shots/errors.log
ERR_FILE_NAME = "errors.log"


def get_linux_path(*args):
    """
    Формирую путь для использования на линукс
    сервере видеонаблюдения. Скрипт запускается на
    ПК windows, поэтому путь ормируется неправильно.
    Оболочки trassir под Линукс - нет
    """

    path = os.path.join(*args)
    return path.replace("\\", "/")


def get_server_name(server_name):
    """
    Получаю имя сервера из двух возможных мест
    """

    path_1 = get_linux_path("/", server_name, "network_interfaces")
    path_2 = get_linux_path("/", server_name, "system_wide_options")

    server_name_1 = str(settings(path_1)["hostname"])  # noqa
    server_name_2 = str(settings(path_2)["alternative_name"])  # noqa

    if (len(server_name_1) > 0) and (server_name_1 != "trassir"):
        s_name = server_name_1
    elif len(server_name_2) > 0:
        s_name = server_name_2
    else:
        s_name = server_name_1

    return s_name


def handle_camera_event(ev, err_log_filename, is_full_info=False):
    """
    Пишу требуемые события по неисправностям
    камер в файл errors.log
    """
    message_to_write = ""
    with open(err_log_filename, "a", buffering=1) as err_log_file:
        try:
            err_log_file.write(
                "\n{} ".format(
                    time.strftime(
                        "%d.%m.%Y %H:%M:%S ", time.gmtime(ev.ts / 1000000)
                    )
                )  # localtime было
            )
            message_to_write = "Имя: {}, событие: {}, ".format(  # noqa
                ev.origin_object.name, ev.type
            )
            err_log_file.write(message_to_write)
            if is_full_info:
                message_to_write = "ИД камера: {} , ИД сервера: {} , ".format(  # noqa
                    ev.origin,
                    ev.origin_server,
                )
                err_log_file.write(message_to_write)

            server_name = get_server_name(ev.origin_server)
            err_log_file.write("Имя сервера: {} ".format(server_name))  # noqa
            # err_log_file.write("Имя сервера: %s " % server_name)
        except Exception as err:
            message_error = "Ошибка при логировании события {}\n".format(  # noqa
                str(err)
            )
            err_log_file.write(message_error)


for event in events_to_handle:
    activate_on_events(  # noqa
        event, "", lambda ev: handle_camera_event(ev, ERR_FILE_NAME)
    )
