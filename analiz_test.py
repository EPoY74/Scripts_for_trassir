"""
Разбираю строку для анадиза данных
"""

import click

line = "13.04.2025 00:02:12,  Имя: kpp1-vyhod, событие: Signal Lost, Имя сервера: UK"

parts = line.strip().split(",")
time_str = parts[0].strip()
name = parts[1].split(":")[1].strip()
event = parts[2].split(":")[1].strip()
server = parts[3].split(":")[1].strip()

click.echo(parts)
click.echo(time_str)
click.echo(event)
click.echo(server)
