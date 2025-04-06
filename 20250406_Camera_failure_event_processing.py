'''
<parameters>
	<company>EugeniiPetrov</company>
	<title>Receive_events</title>
	<version>1.0</version>
</parameters>
'''
import time

events_to_handle = [
    "Signal Lost",
    "Signal Restored",
    "Disks Too Slow",
    "Connection Established",
    "Connection Lost",
]

def f(ev):
    with open("errors.log", "a", buffering = 1) as f:
        try:
            f.write("\nВремя: %s " % time.strftime("%H:%M:%S %d.%m.%Y",
                    time.gmtime(ev.ts/1000000))       # localtime было
            )
            message_to_write = (
                "Имя: %s, событие: %s,"
                " ИД камера: %s" % (
                    ev.origin_object.name,
                    ev.type,
                    ev.origin,
                    )
            )
            f.write(message_to_write)
            f.write("ИД сервера: %s " % ev.origin_server)
        except Exception as err:
            message_error = (
                "Ошибка при логировании события %s\n"
                % str(err)
            )
            f.write(message_error)
    f.close()


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


for event in events_to_handle:
    activate_on_events(event, "", f)
    
for event in events_to_handle:
    activate_on_events(event, "", on_event)