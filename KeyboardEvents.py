import pyautogui as pyag
import time


def hold_space(holding_time):
    pyag.keyDown("space")
    time.sleep(holding_time)
    pyag.keyUp("space")


def press_esc():
    pyag.keyDown("esc")
    time.sleep(0.05)
    pyag.keyUp("esc")


def press_enter():
    pyag.keyDown("enter")
    time.sleep(0.05)
    pyag.keyUp("enter")
