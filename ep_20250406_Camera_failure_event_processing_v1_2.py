#  Принимает и обрабатыывает события от сервера видеонаблюдения trassir
#  и записывает их в файл.
#  Работает только непосредственно на серверах
#  trassir или на  trassir client для ПК

import os
import sys
import time

"""
<parameters>
        <company>EugeniiPetrov</company>
        <email>p174@mail.ru</email>
        <title>Receive_events</title>
        <version>1.0</version>
</parameters>
"""

# Переопределяю на более человекочитаемые имена 
# и в том числеЮ .что бы в vscode было меньше ошибок, 
# так как message и settings это встроенные функции в Trassir
message_to_user = message
server_settings = settings

events_to_handle = [
    "Signal Lost",
    "Signal Restored",
    "Disks Too Slow",
    # "Connection Established",
    # "Connection Lost",
]
# /home/trassir/shots/errors.log
# "/G6sKoF8w/system_wide_options"[screenshots_folder]
ERR_FILE_NAME = "errors.log"


def get_linux_path(*args):
    """
    Формирую путь для использования на линукс
    сервере видеонаблюдения. Скрипт запускается на
    ПК windows, поэтому путь формируется неправильно.
    Оболочки trassir под Линукс - нет
    """
    # pass
    path = os.path.join(*args)
    return path.replace("\\", "/")


def get_server_name(server_name):
    """
    Получаю имя сервера из двух возможных мест
    """

    path_1 = get_linux_path("/", server_name, "network_interfaces")
    path_2 = get_linux_path("/", server_name, "system_wide_options")

    server_name_1 = str(server_settings(path_1)["hostname"])  # noqa
    server_name_2 = str(server_settings(path_2)["alternative_name"])  # noqa

    if (len(server_name_1) > 0) and (server_name_1 != "trassir"):
        s_name = server_name_1
    elif len(server_name_2) > 0:
        s_name = server_name_2
    else:
        s_name = server_name_1

    return s_name


def get_screenshot_folder(server_id):
    """
    Получаю из настроек путь к папке скриншотов,
    так как сохранять можно туда
    """

    screenshot_folder_path = get_linux_path(
        "/", server_id, "system_wide_options",
    )
    return str(server_settings(screenshot_folder_path)["screenshots_folder"])  # noqa


def write_err_to_file(ev, is_full_info, server_name, full_err_filename):
    """
    Пишет информацию в файл, вынесена, так как требуется дополнительная
    обработка ошибок, не во всех серверах  есть папка со
    скриншотами, хотя путь к ней моществует
    """

    message_to_write = ""
    with open(full_err_filename, "a", buffering=1) as err_log_file:
        try:
            err_log_file.write(
                "\n{} ".format(
                    time.strftime(
                        "%d.%m.%Y %H:%M:%S, ", time.gmtime(ev.ts / 1000000)
                    )
                )  # localtime было
            )
            message_to_write = "Имя: {}, событие: {}, ".format(  # noqa
                ev.origin_object.name, ev.type
            )
            # message_to_user(message_to_write)  # noqa
            err_log_file.write(message_to_write)
            if is_full_info:
                message_to_write = "ИД камера: {} , ИД сервера: {} , ".format(  # noqa
                    ev.origin,
                    ev.origin_server,
                )
                err_log_file.write(message_to_write)
            err_log_file.write("Имя сервера: {} ".format(server_name))  # noqa
            # err_log_file.write("Имя сервера: %s " % server_name)
        except (IOError, KeyError, TypeError) as err:  # noqa
            message_error = "Ошибка при логировании события {}\n".format(  # noqa
                str(err)
            )
            err_log_file.write(message_error)


def get_os():
    """
	Проверяю какая операционная система
    """
    if sys.platform.startswith('win'):
        return "Windows"
    elif sys.platform.startswith('linux'):
        return "Linux"
    else:
        return "Unknown OS"
    

def message_err_ev(ev):
    """
    Выводит сообщение нв экран
    """
    message_to_write = "Имя: {}, событие: {}, ".format(  # noqa
                ev.origin_object.name, ev.type
            )
    message_to_user(message_to_write)  # noqa
    

def get_linux_document_folder_path():
    """
    Выводит путь к папке с документами в ОС Linux
    """
    documents_dir = os.getenv("XDG_DOCUMENTS_DIR")
    if documents_dir is None:
        # home_dir = str(os.getenv("HOME"))
        # documents_dir = os.path.join(home_dir, "Documents")
        
        # Писать без проблем получилось только сюда,
        #  в другие места - проблема с правами
        documents_dir = "/tmp" 
    return documents_dir


def handle_camera_event(ev, err_log_filename, is_full_info=False):
    """
    Пишу требуемые события по неисправностям
    камер в файл errors.log
    """
    # Вывожу сообщение в любом случае
    # До записи в файл
    message_err_ev(ev)
    # Если это видеосервер то False 
    # Если клиент на ПК, то True
    is_client = False

    os_system_name = get_os()
    # Проверяю наличие папки со скриншотами по уникальному
    # адресу, характерному только для ПК клиента
    server_name = get_server_name(ev.origin_server)
    try:
        err_filelog_folder = str(
            server_settings("/client/system_wide_options")["screenshots_folder"]  # noqa
        )
        is_client = True
    except (IOError, KeyError, TypeError) as err:  # noqa
        message_to_user(err)  # noqa
        err_filelog_folder = ""
    if is_client and (os_system_name == "Linux") :
        err_filelog_folder = get_linux_document_folder_path()
        message_to_user("Пишу в папку {}".format(err_filelog_folder)) # noqa
        


    # Формирую имя и путь файла для логирования
    if ((len(err_filelog_folder) > 0) 
        and (is_client is False)
        and (os_system_name == "Windows")):
        message_to_user("Client False")
        full_err_filename = (
            err_filelog_folder.replace("/", "\\")
            + "\\"
            + str(time.strftime("%Y%m%d", time.gmtime(ev.ts / 1000000)))
            + "_"
            + err_log_filename
        )
    if ((len(err_filelog_folder) > 0) 
        and is_client
        and (os_system_name == "Linux")):
        message_to_user("Client True")
        full_err_filename = (
            err_filelog_folder
            + "/"
            + str(time.strftime("%Y%m%d", time.gmtime(ev.ts / 1000000)))
            + "_"
            + err_log_filename
        )
    else:
        message_to_user("Client Else")
        full_err_filename = (
            get_screenshot_folder(ev.origin_server)
            + "/"
            + str(time.strftime("%Y%m%d", time.gmtime(ev.ts / 1000000)))
            + "_"
            + server_name
            + "_"
            + err_log_filename
        )
    # try:
    write_err_to_file(ev, is_full_info, server_name, full_err_filename)
    #except IOError as err:  # noqa
     #   message_to_user(str(err))  # noqa
      #  raise Exception(err)


for event in events_to_handle:
    activate_on_events(  # noqa
        event, "", lambda ev: handle_camera_event(ev, ERR_FILE_NAME)
    )
