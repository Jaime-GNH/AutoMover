from pynput import mouse, keyboard
import pyautogui as pag
import random
import time
from time import perf_counter, sleep

TIMEOUT = 180
SENTENCES = ["Don't worry. The owl is working...",
             "Nevermind. The owl never sleeps!",
             "Enjoy your coffee. The owl is here.",
             "Hard day huh? The owl protects you!",
             "Disobey! The owl keeps you safe.",
             "Relax the eyes. The owl is watching.",
             "The owl is here while you are absent.",
             "Is good to take some time. Glory to the owl.",
             "Five minutes gone. No-one knows thanks to the owl!",
             "Keep calm and let the owl work.",
             "Which is the best nation? Procrastination.",
             "Whatever you are doing is okay. I'm here.",
             "Being paid for doing nothing? You are on the right track!",
             "Let you rest is my favourite job"]


def on_move(x, y):
    global last_time
    last_time = perf_counter()


def on_click(x, y, button, pressed):
    global last_time
    last_time = perf_counter()


def on_scroll(x, y, dx, dy):
    global last_time
    last_time = perf_counter()


def on_press(key):
    global last_time
    last_time = perf_counter()


last_time = perf_counter()
listenerk = keyboard.Listener(on_press=on_press)
listenerk.start()
listenerm = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listenerm.start()
while True:
    if perf_counter() - last_time >= TIMEOUT:
        pag.keyDown('alt')
        pag.press('tab')
        pag.keyUp('alt')
        sleep(0.1)
        pag.keyDown('alt')
        pag.press('tab')
        pag.keyUp('alt')
        print(time.asctime().split(' ')[-2] + ':', random.choice(SENTENCES))
        last_time = perf_counter()
    else:
        sleep(1)
