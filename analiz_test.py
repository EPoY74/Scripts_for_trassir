import click
import pandas as pd
from datetime import datetime

# Чтение данных (пример для файла 'events.log')
data = []
with open("20250414_errors.log") as file:
    for line in file:
        click.echo(len(line))

        # if len(line) <= 1:
        #     continue
        parts = line.strip().split(",")
        click.echo(parts)
        time_str = parts[0].strip()
        name = parts[1].split(":")[1].strip()
        event = parts[2].split(":")[1].strip()
        server = parts[3].split(":")[1].strip()

        time = datetime.strptime(time_str, "%d.%m.%Y %H:%M:%S")
        data.append([time, name, event, server])

df = pd.DataFrame(data, columns=["Time", "Name", "Event", "Server"])

# Расчет длительности перерывов
lost_times = df[df["Event"] == "Signal Lost"].copy()
restored_times = df[df["Event"] == "Signal Restored"].copy()

lost_times["NextRestore"] = restored_times["Time"].values
lost_times["Downtime"] = lost_times["NextRestore"] - lost_times["Time"]

# Результаты
click.echo("Общее количество сбоев:", len(lost_times))
click.echo("Средняя длительность перерыва:", lost_times["Downtime"].mean())
click.echo("Максимальный перерыв:", lost_times["Downtime"].max())
click.echo("Минимальный перерыв:", lost_times["Downtime"].min())

# График временных промежутков
import matplotlib.pyplot as plt

lost_times["DowntimeSeconds"] = lost_times["Downtime"].dt.total_seconds()
plt.plot(lost_times["Time"], lost_times["DowntimeSeconds"], "o-")
plt.xlabel("Время")
plt.ylabel("Длительность перерыва (секунды)")
plt.show()
