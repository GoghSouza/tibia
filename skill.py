import ctypes
import time
import var
import random

hwnd = ctypes.windll.user32.FindWindowW(0, 'Tibia - Tamesu')
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

#Função para precionar uma tecla.
def send_message_keyboard(hwnd, key_code):
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, key_code, 0)
    time.sleep(0.2)
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, key_code, 0)


while True:
    time.sleep(1)
    send_message_keyboard(hwnd, 0x62)