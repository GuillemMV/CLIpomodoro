import typer
from tqdm import tqdm
from time import sleep

app = typer.Typer()
WorkMinutes = 0
RelaxMinutes = 0

def workTime():
    seconds = int(WorkMinutes*60)
    for i in tqdm(range(seconds),desc="Work time",bar_format="{l_bar}{bar}"):
        sleep(1)

def relaxTime():
    seconds = int(RelaxMinutes*60)
    for i in tqdm(range(seconds),desc="Relax Time",bar_format="{l_bar}{bar}"):
        sleep(1)

def start():
    try:
        while True:
            workTime()
            relaxTime()
    except KeyboardInterrupt as stop:
        print("You finished the pomodoro! Bye!")

@app.command()
def setTime(worktime:int,relaxtime:int):
    global RelaxMinutes, WorkMinutes
    RelaxMinutes = relaxtime
    WorkMinutes = worktime
    typer.echo("Time set correctly!")
    start()

if __name__ == "__main__":
    app()
