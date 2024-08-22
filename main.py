import json
from tkinter import Button, Entry, Label
from tkinter.ttk import Combobox, Frame, Notebook
from ttkthemes import ThemedTk
import var, runa


app = ThemedTk()
app.title("Gogh Bot para MS")
app.geometry("500x500+450+100")

nb = Notebook(app)
nb.place(x=0,y=50, width=500, height=500)

runaMS = Frame(nb)
nb.add(runaMS, text="Criador de Runas")

hotkeysConfig = Frame(nb)
nb.add(hotkeysConfig, text="Hotkey's")

runas = ["Desligado", "SD - Death Rune", "GFB - Great Fireball", "Thunderstorm"]
hotkeys = ["Desligado","F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]

#Criação dos Widget
def generate_widget(widget, row, column, sticky="NSEW", columnspan=None,aba=None, **kwargs):
    my_wydget = widget(aba, **kwargs)
    my_wydget.grid(row=row, column=column, padx=5, pady=5, columnspan=columnspan,sticky=sticky)
    return my_wydget

#Validar que apenas Numeros serão digitados
def only_numbers(char):
    return char.isdigit()

validate_cmd = app.register(only_numbers)

#Salvar
def salvarHotkey():
    var.save(
    cbx_food,
    cbx_lifeRing,
    cbx_ringHealing,
    cbx_ringPlasma,
    cbx_collarPlasma,
    cbx_softBoot,
    cbx_tiara,
    cbx_deathRune,
    cbx_fireBall,
    cbx_thunderStorm)

def carregarHotkey():
    with open('hotkeyRunaConfig.json', 'r') as file:
        data = json.loads(file.read())
    cbx_food.current(data["food"]["position"])
    cbx_lifeRing.current(data["life_ring"]["position"])
    cbx_ringHealing.current(data["ring_healing"]["position"])
    cbx_ringPlasma.current(data["ring_plasma"]["position"])
    cbx_collarPlasma.current(data["collar_plasma"]["position"])
    cbx_softBoot.current(data["soft_boot"]["position"])
    cbx_tiara.current(data["tiara"]["position"])
    cbx_deathRune.current(data["runa_death"]["position"])
    cbx_fireBall.current(data["runa_fireball"]["position"])
    cbx_thunderStorm.current(data["runa_thunderstorm"]["position"])
        
def iniciarBot():
    runa.inicioBot(
        cbx_runaCriada,
        int(cbx_qtnLifeRing.get()),
        int(cbx_qtnRingHealing.get()),
        int(cbx_qtnRingPlasma.get()),
        int(cbx_qtnCollarPlasma.get()),
        cbx_escSoftBoot.current(),
        cbx_escTiara.current())

#Configuração da Aba Criador de Runas
lbl_tituloBot = generate_widget(Label, row=0, column=0, sticky="W", text="Treino de ML por Criação de Runas", font=("Roboto",12))
lbl_foodRecomend = generate_widget(Label,aba=runaMS, row=1, column=0, sticky="W", text="Melhor Food para uso será Brown Mushroom", font=("Roboto",12))

lbl_qtnLifeRing = generate_widget(Label,aba=runaMS, row=2, column=0, sticky="W", text="Quantos Life Rings serão usados ?", font=("Roboto",12))
cbx_qtnLifeRing = generate_widget(Entry,aba=runaMS, row=2, column=1, sticky="w", validate="key", validatecommand=(validate_cmd, "%S"))
cbx_qtnLifeRing.insert(0, "0")

lbl_qtnRingHealing = generate_widget(Label,aba=runaMS, row=3, column=0, sticky="W", text="Quantos Ring of Healing serão usados ?", font=("Roboto",12))
cbx_qtnRingHealing = generate_widget(Entry,aba=runaMS, row=3, column=1, sticky="w", validate="key", validatecommand=(validate_cmd, "%S"))
cbx_qtnRingHealing.insert(0, "0")

lbl_qtnRingPlasma = generate_widget(Label,aba=runaMS, row=4, column=0, sticky="W", text="Quantos Ring of Green Plasma serão usados ?", font=("Roboto",12))
cbx_qtnRingPlasma = generate_widget(Entry,aba=runaMS, row=4, column=1, sticky="w", validate="key", validatecommand=(validate_cmd, "%S"))
cbx_qtnRingPlasma.insert(0, "0")

lbl_qtnCollarPlasma = generate_widget(Label,aba=runaMS, row=5, column=0, sticky="W", text="Quantos Collar of Green Plasma serão usados ?", font=("Roboto",12))
cbx_qtnCollarPlasma = generate_widget(Entry,aba=runaMS, row=5, column=1, sticky="w", validate="key", validatecommand=(validate_cmd, "%S"))
cbx_qtnCollarPlasma.insert(0, "0")

lbl_softBoot = generate_widget(Label,aba=runaMS, row=6, column=0, sticky="W", text="Irá Usar Pair of Soft Boots ?", font=("Roboto",12))
cbx_escSoftBoot = generate_widget(Combobox,aba=runaMS, row=6, column=1, values=("Não", "Sim"), state="readonly", font=("Roboto", 12),width=12)
cbx_escSoftBoot.current(0)

lbl_tiara = generate_widget(Label,aba=runaMS, row=7, column=0, sticky="W", text="Irá Usar Tiara of Power ?", font=("Roboto",12))
cbx_escTiara = generate_widget(Combobox,aba=runaMS, row=7, column=1, values=("Não", "Sim"), state="readonly", font=("Roboto", 12),width=12)
cbx_escTiara.current(0)

lbl_runaCriada = generate_widget(Label,aba=runaMS, row=8, column=0, sticky="W", text="Qual Runa deseja criar ?", font=("Roboto",12))
cbx_runaCriada = generate_widget(Combobox,aba=runaMS, row=8, column=1, values=runas, state="readonly", font=("Roboto", 12),width=12)
cbx_runaCriada.current(0)

btn_inicio = generate_widget(Button, aba=runaMS, row=9, column=0, text="Iniciar Bot", command=iniciarBot)


#Configuração da Aba Hotkey's
lbl_configHotkey = generate_widget(Label, aba=hotkeysConfig, row=0, column=0, sticky="W", columnspan=2, text="Configure as Hotkey dos itens/spell para a criação das runas", font=("Roboto",12))

lbl_food = generate_widget(Label, aba=hotkeysConfig, row=1, column=0, sticky="W", text="Comida/Food", font=("Roboto",12))
cbx_food = generate_widget(Combobox,aba=hotkeysConfig, row=1, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_food.current(0)

lbl_lifeRing = generate_widget(Label, aba=hotkeysConfig, row=2, column=0, sticky="W", text="Life Ring", font=("Roboto",12))
cbx_lifeRing = generate_widget(Combobox,aba=hotkeysConfig, row=2, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_lifeRing.current(0)

lbl_ringHealing = generate_widget(Label, aba=hotkeysConfig, row=3, column=0, sticky="W", text="Ring of Healing", font=("Roboto",12))
cbx_ringHealing = generate_widget(Combobox,aba=hotkeysConfig, row=3, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_ringHealing.current(0)

lbl_ringPlasma = generate_widget(Label, aba=hotkeysConfig, row=4, column=0, sticky="W", text="Ring of Green Plasma", font=("Roboto",12))
cbx_ringPlasma = generate_widget(Combobox,aba=hotkeysConfig, row=4, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_ringPlasma.current(0)

lbl_collarPlasma = generate_widget(Label, aba=hotkeysConfig, row=5, column=0, sticky="W", text="Collar of Green Plasma", font=("Roboto",12))
cbx_collarPlasma = generate_widget(Combobox,aba=hotkeysConfig, row=5, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_collarPlasma.current(0)

lbl_softBoot = generate_widget(Label, aba=hotkeysConfig, row=6, column=0, sticky="W", text="Pair of Soft Boots", font=("Roboto",12))
cbx_softBoot = generate_widget(Combobox,aba=hotkeysConfig, row=6, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_softBoot.current(0)

lbl_tiara = generate_widget(Label, aba=hotkeysConfig, row=7, column=0, sticky="W", text="Tiara of Power", font=("Roboto",12))
cbx_tiara = generate_widget(Combobox,aba=hotkeysConfig, row=7, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_tiara.current(0)

lbl_deathRune = generate_widget(Label, aba=hotkeysConfig, row=8, column=0, sticky="W", text="Cast - Sudden Death", font=("Roboto",12))
cbx_deathRune = generate_widget(Combobox,aba=hotkeysConfig, row=8, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_deathRune.current(0)

lbl_fireBall = generate_widget(Label, aba=hotkeysConfig, row=9, column=0, sticky="W", text="Cast - Great Fireball", font=("Roboto",12))
cbx_fireBall = generate_widget(Combobox,aba=hotkeysConfig, row=9, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_fireBall.current(0)

lbl_thunderStorm = generate_widget(Label, aba=hotkeysConfig, row=10, column=0, sticky="W", text="Cast ThunderStorm", font=("Roboto",12))
cbx_thunderStorm = generate_widget(Combobox,aba=hotkeysConfig, row=10, column=1, values=hotkeys, state="readonly", font=("Roboto", 12),width=12)
cbx_thunderStorm.current(0)

btn_carregar = generate_widget(Button, aba=hotkeysConfig, row=11, column=0, text="Carregar Configurações", command=carregarHotkey)
btn_salvar = generate_widget(Button, aba=hotkeysConfig, row=11, column=1, text="Salvar", command=salvarHotkey)


app.mainloop()