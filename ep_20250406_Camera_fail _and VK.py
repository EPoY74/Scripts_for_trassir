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
    with open("errors.log", "a", buffering=1) as f:
        try:
            f.write(
                "\nВремя: %s "
                % time.strftime(
                    "%H:%M:%S %d.%m.%Y", time.gmtime(ev.ts / 1000000)
                )  # localtime было
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


class OriginObject:
    name: str


class EventData:
    def __init__(self):
        pass

    origin_object: OriginObject
    type: str
    origin: str
    origin_server: str


message = print


def on_event(ev):
    # Перебираем все атрибуты события
    for attr in dir(ev):
        if not attr.startswith("__"):  #  Пропускаю служебные атрибуты
            try:
                # message("%s: %s" % (attr, getattr(ev, attr)))  # Форматирование для Python 2.7
                with open("events.log", "a") as f:
                    f.write("%s: %s\n" % (attr, getattr(ev, attr)))
            except Exception as e:
                message("Ошибка при обработке атрибута %s: %s" % (attr, str(e)))


event_handlers: dict[str, callable] = {}


def activate_on_events(event_name, something, handler):
    event_handlers[event_name] = handler


def invoke_handler(event_name, event_data):
    if event_name in event_handlers:
        event_handlers[event_name](event_data)
    else:
        print(f"No handler for event {event_name}")


for event in events_to_handle:
    activate_on_events(event, "", f)

# for event in events_to_handle:
#     activate_on_events(event, "", on_event)

print(str(event_handlers))

invoke_handler(
    "Signal Lost", EventData(origin... = "abcdef")
)

def test_signal_lost():
    # Arrange
    event_data = EventData(field1="abcdef", ...)
    
    # Act
    on_event(event_data)
    
    # Assert
    # TODO: check logs - find event data in the log
    with open(logfile) as f:
        # TODO: find log message in the file
        # search for 'field1=abcdef'
    