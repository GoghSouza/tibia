import json
import threading
import time
from tkinter import messagebox
import pygetwindow as gw
import pyautogui
import keyboard
import random


def hotkeyConfig(consulta):
    with open('hotkeyRunaConfig.json', 'r') as file:
        data = json.loads(file.read())
    
    return data[consulta]["value"]

#Encontrar Janela do Tibia independente do personagem logado
def encontrarJanela():
    windows = pyautogui.getAllWindows()
    for window in windows:
        try:
            window_name = window.title.split('Tibia -')[1]
            if window_name:
                WINDOW_TITLE = window.title
        except:
            continue

    try:
        target_window = [item for item in gw.getWindowsWithTitle(WINDOW_TITLE) if item.title == WINDOW_TITLE][0]
    except:
        pyautogui.alert(title="Hidden Client Tibia", text='Janela do Tibia não localizada')
        raise ValueError('Janela do Tibia não localizada')

    target_hwnd = target_window._hWnd

    return target_hwnd

# Evento global para sinalizar o encerramento das threads
stop_event = threading.Event()
lock = threading.Lock()

def verificarItens(timeCollar, timeTiara, timeBoot):
    soma = 0
    if time.time() < timeCollar:
        soma += 8
    if time.time() < timeTiara:
        soma += 8
    if time.time() < timeBoot:
        soma += 12

    return soma

def regenerarMana(lifeRing, ringHealing, ringPlasma, collarPlasma, softBoot, tiara):
    inicio = time.time()
    global regenMana

    # Calcula os tempos finais para cada item
    timeCollar = inicio + collarPlasma
    timeBoot = inicio + softBoot
    timeTiara = inicio + tiara

    # RingHealing
    inicioRunas = time.time()
    while time.time() - inicioRunas < ringHealing:
        if stop_event.is_set():
            break
        regen = 12
        regen = (regen + 24 + verificarItens(timeCollar, timeTiara, timeBoot)) * 1.5
        regenMana = regen
        time.sleep(30)
                    
    # LifeRing
    inicioRunas = time.time()
    while time.time() - inicioRunas < lifeRing:
        if stop_event.is_set():
            break
        regen = 12
        regen = (regen + 8 + verificarItens(timeCollar, timeTiara, timeBoot)) * 1.5
        regenMana = regen
        time.sleep(30)

    # RingPlasma
    inicioRunas = time.time()
    while time.time() - inicioRunas < ringPlasma:
        if stop_event.is_set():
            break
        regen = 12
        regen = (regen + 4 + verificarItens(timeCollar, timeTiara, timeBoot)) * 1.5
        regenMana = regen
        time.sleep(30)

    regenMana = 0
    #Verificar e desequipa itens caso ainda tenha tempo de uso ao fim dos aneis
    if time.time() > timeCollar:
        pyautogui.press(hotkeyConfig("collar_plasma"))
    if time.time() > timeTiara:
        pyautogui.press(hotkeyConfig("tiara"))
    if time.time() > timeBoot:
        pyautogui.press(hotkeyConfig("soft_boot"))

    #Finaliza todas as Threads
    stop_event.set()

    messagebox.showinfo("Fim das Rotinas", f"Bot Finalizado, foram criadas aproximadamente: {nRunas}")
    

def controleRing(life, healing, plasma):
    #Controlando uso do Ring Healing
    for _ in range(healing):
        if stop_event.is_set():
            break
        with lock:
            pyautogui.press(hotkeyConfig("ring_healing"))
        espera = 450 + random.randint(1,10)
        time.sleep(espera)

    #Controlando uso do Life Ring
    for _ in range(life):
        if stop_event.is_set():
            break
        with lock:
            pyautogui.press(hotkeyConfig("life_ring"))
        espera = 1200 + random.randint(1,10)
        time.sleep(espera)

    #Controlando uso do Ring of Green Plasma
    for _ in range(plasma):
        if stop_event.is_set():
            break
        with lock:
            pyautogui.press(hotkeyConfig("ring_plasma"))
        espera = 1800 + random.randint(1,10)
        time.sleep(espera)

#Controle do Collar of Green Plasma        
def controleColar(colar):
    for _ in range(colar):
        if stop_event.is_set():
            break
        pyautogui.press(hotkeyConfig("collar_plasma"))
        espera = 1800 + random.randint(1,10)
        time.sleep(espera)
        
#Controle da Tiara        
def controleTiara(tiara):
    for _ in range(tiara):
        if stop_event.is_set():
            break
        pyautogui.press(hotkeyConfig("tiara"))
        espera = 3600 + random.randint(1,10)
        time.sleep(espera)

#Controle da Soft Boot
def controleBoot(boot):
    for _ in range(boot):
        if stop_event.is_set():
            break
        pyautogui.press(hotkeyConfig("soft_boot"))
    espera = 14400 + random.randint(1,10)
    time.sleep(espera)

#Andar x passos e voltar para mesmo local
def andar():
    while not stop_event.is_set():
        passos = random.randint(1,5)
        tempoEspera = random.randint(400,600)

        for _ in range(2 + passos):
            with lock:
                pyautogui.press(hotkeyConfig("food"))  

        for _ in range(passos):
            with lock:
                pyautogui.press("W")
            time.sleep(2)
        for _ in range(passos):
            with lock:
                pyautogui.press("S")
            time.sleep(3)
        time.sleep(tempoEspera)
    
#Controle da Criação de Runas
def criarRunas(runa):
    idRuna = runa.current()
    global nRunas
    nRunas = 0
    print("Criar Runas")
    if idRuna == 1:
        custoRuna = 985
        hotRuna = "runa_death"
        qtdRunas = 3
    elif idRuna == 2:
        custoRuna = 530
        hotRuna = "runa_fireball"
        qtdRunas = 4
    elif idRuna == 3:
        custoRuna = 430
        hotRuna = "runa_thunderstorm"
        qtdRunas = 4
    else:
        stop_event.set()
    mana = 0

    #Tenta 2 Runas para a mana não ficar cheia
    if not stop_event.is_set():
        with lock:
            print("Criando runas Iniciais")
            pyautogui.press(hotkeyConfig(hotRuna))
            time.sleep(2)
            pyautogui.press(hotkeyConfig(hotRuna))
    
    #Enquanto tiver regeneração de Mana irá somar a mana a cada 6 seg's
    while regenMana > 0:
        if stop_event.is_set():
            break
        mana += regenMana
        if mana > custoRuna:
            with lock:
                print("Criado Runa")
                pyautogui.press(hotkeyConfig(hotRuna))
            mana -= custoRuna
            nRunas += qtdRunas
        time.sleep(6)

#Função inicial do Bot
def inicioBot(runa, lifeRing, ringHealing, ringPlasma, collarPlasma, softBoot, tiara):
    
    print(runa)
    #Limpa a chave para encerrar o bot
    stop_event.clear()
    #Tempo de duração dos itens
    timerHealing = ringHealing * 450
    timerLife = lifeRing * 1200
    timerPlasma = ringPlasma * 1800
    timerCPlasma = collarPlasma * 1800
    timerBoot = softBoot * 14400
    timerTiara = tiara * 3600

    messagebox.showinfo("Inicio do Bot", "Abra a tela do Tibia com seu personagem logado e aperte Insert para iniciar")
    keyboard.wait("Insert")

    # Criar as threads, passando as funções como referência
    aneis_th = threading.Thread(target=controleRing, args=(lifeRing, ringHealing, ringPlasma), daemon=True)
    colar_th = threading.Thread(target=controleColar, args=(collarPlasma,), daemon=True)
    tiara_th = threading.Thread(target=controleTiara, args=(tiara,), daemon=True)
    boot_th = threading.Thread(target=controleBoot, args=(softBoot,), daemon=True)
    regen_th = threading.Thread(target=regenerarMana, args=(timerLife,timerHealing,timerPlasma,timerCPlasma,timerBoot,timerTiara), daemon=True)
    criar_th = threading.Thread(target=criarRunas, args=(runa,), daemon=True)
    andar_th = threading.Thread(target=andar, daemon=True)

    # Iniciar as threads
    aneis_th.start()
    colar_th.start()
    tiara_th.start()
    boot_th.start()
    regen_th.start()
    criar_th.start()
    andar_th.start()
