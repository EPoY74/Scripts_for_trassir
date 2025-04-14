from datetime import datetime

import click
import pandas as pd

# Загрузка данных
data = []
with open("events.log") as file:
    for line in file:
        parts = line.strip().split(",")
        time_str = parts[0].strip()
        name = parts[1].split(":")[1].strip()
        event = parts[2].split(":")[1].strip()
        server = parts[3].split(":")[1].strip()
        time = datetime.strptime(time_str, "%d.%m.%Y %H:%M:%S")
        data.append([time, name, event, server])

df = pd.DataFrame(data, columns=["Time", "Name", "Event", "Server"])
df = df.sort_values(["Name", "Time"]).reset_index(
    drop=True
)  # Сортировка по устройству и времени

# Словари для хранения результатов
paired_events = {name: [] for name in df["Name"].unique()}
unpaired_lost = {name: [] for name in df["Name"].unique()}

# Обработка для каждого устройства отдельно
for name, group in df.groupby("Name"):
    events = group.to_dict("records")
    i = 0
    while i < len(events):
        if events[i]["Event"] == "Signal Lost":
            lost_event = events[i]
            found_restored = False

            # Ищем ближайший Restored для этого устройства
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

# Вывод результатов
click.echo("=== Найденные пары (Lost -> Restored) ===")
for name, pairs in paired_events.items():
    if pairs:
        click.echo(f"\nУстройство: {name}")
        for lost, restored in pairs:
            click.echo(
                f"  Lost: {lost['Time']} -> Restored: {restored['Time']}"
            )

click.echo("\n=== Незавершенные события (Signal Lost без пары) ===")
for name, unpaired in unpaired_lost.items():
    if unpaired:
        click.echo(f"\nУстройство: {name}")
        unpaired_df = pd.DataFrame(unpaired)
        click.echo(unpaired_df)
