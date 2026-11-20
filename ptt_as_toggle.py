import json
import keyboard
from time import sleep


with open("config.json",encoding='utf-8') as f:
    config = json.load(f)
    ptt_key = config["ptt_key"]
    exit_key = config["exit_key"]

ptt_on : bool = False
stop:bool = False

def stop_script(e):
    global stop
    stop = True

def toggle_ptt(e):
    global ptt_on
    ptt_on = not ptt_on
    if not ptt_on:
        keyboard.release(ptt_key)

keyboard.on_press_key(exit_key,stop_script)
keyboard.on_press_key(ptt_key,toggle_ptt,suppress=True)
while not stop:
    sleep(0.1)
    if ptt_on:
        keyboard.press(ptt_key)
