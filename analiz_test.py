from datetime import datetime

import click
import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных
data = []
with open("20250414_errors.log") as file:
    for line in file:
        parts = line.strip().split(",")
        time_str = parts[0].strip()
        name = parts[1].split(":")[1].strip()
        event = parts[2].split(":")[1].strip()
        server = parts[3].split(":")[1].strip()
        time = datetime.strptime(time_str, "%d.%m.%Y %H:%M:%S")
        data.append([time, name, event, server])

df = pd.DataFrame(data, columns=["Time", "Name", "Event", "Server"])
df = df.sort_values(["Name", "Time"]).reset_index(drop=True)

# Словари для хранения пар и незавершенных событий
paired_events = {name: [] for name in df["Name"].unique()}
unpaired_lost = {name: [] for name in df["Name"].unique()}

# Обработка для каждого устройства
for name, group in df.groupby("Name"):
    events = group.to_dict("records")
    i = 0
    while i < len(events):
        if events[i]["Event"] == "Signal Lost":
            lost_event = events[i]
            found_restored = False

            j = i + 1
            while j < len(events):
                if events[j]["Event"] == "Signal Restored":
                    paired_events[name].append((lost_event, events[j]))
                    found_restored = True
                    i = j  # Переходим к событию после Restored
                    break
                j += 1

            if not found_restored:
                unpaired_lost[name].append(lost_event)
        i += 1

# Создаем DataFrame с длительностями перерывов
downtime_data = []
for name, pairs in paired_events.items():
    for lost, restored in pairs:
        downtime = restored["Time"] - lost["Time"]
        downtime_data.append(
            {"Name": name, "Time": lost["Time"], "Downtime": downtime}
        )

lost_times = pd.DataFrame(downtime_data)

# Расчет статистики
if not lost_times.empty:
    click.echo("\n=== Статистика по перерывам ===")
    click.echo("Общее количество сбоев:", len(lost_times))
    click.echo("Средняя длительность перерыва:", lost_times["Downtime"].mean())
    click.echo("Максимальный перерыв:", lost_times["Downtime"].max())
    click.echo("Минимальный перерыв:", lost_times["Downtime"].min())

    # Визуализация
    lost_times["DowntimeSeconds"] = lost_times["Downtime"].dt.total_seconds()
    plt.figure(figsize=(10, 5))
    plt.plot(lost_times["Time"], lost_times["DowntimeSeconds"], "o-")
    plt.xlabel("Время")
    plt.ylabel("Длительность перерыва (секунды)")
    plt.title("Длительность перерывов по времени")
    plt.grid(True)
    plt.show()
else:
    click.echo("Нет данных для построения статистики.")

# Вывод незавершенных событий
click.echo("\n=== Незавершенные события ===")
for name, unpaired in unpaired_lost.items():
    if unpaired:
        click.echo(f"\nУстройство: {name}")
        unpaired_df = pd.DataFrame(unpaired)
        click.echo(unpaired_df)
