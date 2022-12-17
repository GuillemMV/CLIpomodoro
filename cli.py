"""
Author: Guillem Magriña Vernet
Date: December, 2022
"""

import typer
from tqdm import tqdm
from time import sleep
from datetime import datetime
import os

app = typer.Typer()
WorkMinutes = 0
RelaxMinutes = 0

def workTime():
    seconds = int(WorkMinutes*60)
    for _ in tqdm(range(seconds),desc="WORK🔨",bar_format="{l_bar}{bar}", colour="red"):
        current = datetime.now()
        time = current.strftime("%H:%M:%S")

        print(time)
        sleep(1)
        os.system("clear")

def breakTime():
    seconds = int(RelaxMinutes*60)
    for _ in tqdm(range(seconds),desc="BREAK☕",bar_format="{l_bar}{bar}", colour="green"):
        current = datetime.now()
        time = current.strftime("%H:%M:%S")

        print(time)
        sleep(1)
        os.system("clear")

def start():
    try:
        while True:
            workTime()
            breakTime()
    except KeyboardInterrupt as stop:
        print("You finished the pomodoro! Bye!")

@app.command()
def setTime(worktime:int,relaxtime:int):
    try:
        global RelaxMinutes, RelaxMinutes
        RelaxMinutes = relaxtime
        WorkMinutes = worktime
        typer.echo("Time set correctly!")
        start()
    except Exception as exc:
        print("ERROR: ",exc)
if __name__ == "__main__":
    app()
