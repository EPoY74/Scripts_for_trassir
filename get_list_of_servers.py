# Напишите здесь описание скрипта
"""
<parameters>
        <company>EugeniiPetrov</company>
        <email>p174@mail.ru</email>
        <title>Finding_appenned servers</title>
        <version>1.0</version>
</parameters>
"""
# objects_list("Channel")
# Folder - класс родительских объектов ("Channels", "IP Devices", "Templates"),
#  которым принадлежат все остальные классы;

# Server - класс подключенных серверов;
# IP Device - класс подключенных IP-устройств;
# Channel - класс подключенных каналов;
# GPIO Input - класс тревожных входов;
# GPIO Output - класс тревожных выходов;
# OperatorGUI - класс интерфейса оператора;
# Template - класс шаблонов.

#  Имя файла, куда пишем и режим его открытия
PATH_AND_FILENAME_TO_WRITE = "/tmp/servers_list.txt"
FILE_OPENING_MODE = "a"
TARGET_COFINURATION_OBJECT = "Channel"

message_to_user = message  #  noqa  #  type: ignore

class FileErrorCustom(Exception):
    """
    Пробрасываю полученные ошибки далее
    """

    pass


def main():
    """
    основной код программы
    """
    # objects_list is internal trassirs function
    list_of_servers = objects_list(TARGET_COFINURATION_OBJECT)  # noqa # type: ignore
    try:
        with open(
            PATH_AND_FILENAME_TO_WRITE, FILE_OPENING_MODE
        ) as file_for_info:
            # pass
            for index, server_name in enumerate(list_of_servers, start=1):
                info_of_server = ("{}. {}".format(  #  noqa
                        index,
                        server_name))
                message_to_user(info_of_server)
                file_for_info.write(info_of_server)  
    except OSError as err:
        #  Написано для пайтона 2.7. там конструкции  raise ... from ... нет
        #  и вызывает ошибку
        #  Written for Python 2.7 — raise ... from ... syntax
        #  is not supported and causes an error
        raise (FileErrorCustom(err))  # noqa



#  Это не подходит, так как это не запускается, как основной скрипт
#  if __name__ == "__main__":
"""
Точка входа в программу
"""
message_to_user("Запуск системы логирования определенных настроек")
main()
