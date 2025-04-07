"""
<parameters>
        <company>EugeniiPetrov</company>
        <title>Receive_events</title>
        <version>1.0</version>
</parameters>
"""

import time

events_to_handle = [
    "Signal Lost",
    "Signal Restored",
    "Disks Too Slow",
    "Connection Established",
    "Connection Lost",
]


def f(ev):
    """
    Обрабатывает требуемые типы событий и пишет параметры события в файл
    Processes required event types and writes event parameters to a file
    """
    with open("errors.log", "a", buffering=1) as f:
        try:
            f.write(
                "\nВремя: %s "
                % time.strftime("%H:%M:%S %d.%m.%Y", time.gmtime(ev.ts / 1000000))
            )
            message_to_write = "Имя: %s, событие: %s, ИД камера: %s" % (
                ev.origin_object.name,
                ev.type,
                ev.origin,
            )
            f.write(message_to_write)
            f.write("ИД сервера: %s " % ev.origin_server)
        except Exception as err:
            message_error = "Ошибка при логировании события %s\n" % str(err)
            f.write(message_error)
    f.close()


def on_event(ev):
    """
    Обрабатывает все атрибуты события и пишет в файл
    Processes all event attributes and writes to a file
    """
    #  Перебираем все атрибуты события
    for attr in dir(ev):
        #  Пропускаю служебные атрибуты
        if not attr.startswith("__"):
            try:
                with open("events.log", "a") as f:
                    f.write("%s: %s\n" % (attr, getattr(ev, attr)))
            except Exception as e:
                message("Ошибка при обработке атрибута %s: %s" % (attr, str(e)))


for event in events_to_handle:
    activate_on_events(event, "", f)
