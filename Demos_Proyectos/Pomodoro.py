# Hacer una app de pomodoro donde te divide el estudio por partes (Cuando empiezas a estudiar temporizador de 30 mins, con luego 5 de descanso, etc.)

import time
import typer

# Formato de consola (ANSI)
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Tiempo en minutos
STUDY_TIME = 0.5
BREAK_TIME = 5

def main():
    cond = 0
    time_elapsed = 0
    while True:
        if not typer.confirm("Start"):
            break
        if cond == 0:
            pomodoro_time = int(STUDY_TIME * 60)
        else:
            pomodoro_time = int(BREAK_TIME * 60)
        print(CLEAR)
        while time_elapsed < pomodoro_time:
            time_left = pomodoro_time - time_elapsed
            minutes_left = time_left // 60
            seconds_left = time_left % 60
            print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")

            time.sleep(1)
            time_elapsed += 1

        cond = 1 - cond


if __name__ == "__main__":
    main()
