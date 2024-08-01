import ctypes
import time
import var
import random

anel = var.F8
comida = var.F9
runa = var.F10
nRuna = 0

hwnd = ctypes.windll.user32.FindWindowW(0, 'Tibia - Tamesu')
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

#Função para precionar uma tecla.
def send_message_keyboard(hwnd, key_code):
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, key_code, 0)
    time.sleep(0.2)
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, key_code, 0)

def criarRunas(repet):
    #Criar Runas com o Tempo (3min 20 Seg + 1/10 Seg's de aleatoriedade)
    for _ in range(repet):
        espera = 200 + random.randint(1,10)
        time.sleep(espera)
        send_message_keyboard(hwnd, runa)
        print("Runa Criada")

def andar():
    #Andar x passos e voltar para mesmo local
    passos = random.randint(1,5)
    print("Andar " + str(passos))
    for _ in range(passos):
        send_message_keyboard(hwnd, var.W)
    time.sleep(1)
    for _ in range(passos):
        send_message_keyboard(hwnd, var.S)
    time.sleep(3)

#Repetir comando
while True:

    print("Iniciando")
    #Equipar Anel
    send_message_keyboard(hwnd, anel)
    time.sleep(3)

    #Usar Food (Brown Mushroom)
    for _ in range(8):
        send_message_keyboard(hwnd, comida)
    time.sleep(4)

    #Fazer runas iniciais (Mana Full)
    for _ in range(4):
        send_message_keyboard(hwnd, runa)
        time.sleep(3)  

    print("Iniciando contagem de Runas")
    repeticao = random.randint(1,3)
    criarRunas(repeticao)

    #Usar Food para completar 20min e andar
    andar()
    send_message_keyboard(hwnd, comida)

    repeticao = 6 - repeticao
    criarRunas(repeticao)
    
    print("Fim")

   