import  customtkinter as ctk
import json

root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.geometry("500x600")
root.title("ClickMine")
root.resizable(False,False)


def load_data():
    with open("miner_save.json", "r", encoding="utf-8") as file:
        data_from_json = json.load(file)
        return data_from_json


def save_data():
    data_new = {
        "coins": coins,
        "coins_per_click": coins_per_click,
        "coins_per_second": coins_per_second,
        "pickaxe_level": pickaxe_level,
        "miner_level": miner_level,
        "pickaxe_price": pickaxe_price,
        "miner_price": miner_price,
        "time": time
    }

    with open("miner_save.json", "w", encoding="utf-8") as file:
        json.dump(data_new,file,ensure_ascii=False,indent=2)


def update_labels():
    coins_label.configure(text=f"🪙монеты: {coins}")
    stats_label.configure(text=(f"⛏️ Сила кирки{coins_per_click}\n"
                                f"🔨 Уровень кирки:{pickaxe_level}\n"
                                f"👷 Уровень шахтёра:{miner_level}"))
    pickaxe_button.configure(text=f"Улучшить кирку\nЦена:{pickaxe_price}💎")
    miner_button.configure(text=f"Нанять шахтера\nЦена:{miner_price}")


def time_counter():
    global time,coins
    time += 1
    coins += coins_per_second
    save_data()
    update_labels()
    timer_label.configure(text=f"Время в пещере:{time}")
    root.after(1000,time_counter)


def mine_crystal():
    global coins
    coins += coins_per_click
    log_label.configure(text=f"Вы добыли {coins_per_click} кристаллов")
    update_labels()
    save_data()


def buy_pickaxe():
    global coins_per_click,coins,pickaxe_level,pickaxe_price
    if coins >= pickaxe_price:
        print("покупка")
        coins -= pickaxe_price
        pickaxe_level += 1
        coins_per_click += 1000000
        pickaxe_price += 25
        save_data()
        update_labels()

def buy_miner():
    global coins_per_second,coins,miner_level,miner_price
    if coins >= miner_price:
        print("покупка майнера")
        coins -= miner_price
        miner_level += 1
        coins_per_second += 1
        miner_price += 50
        save_data()
        update_labels()




def reset_game():
    global coins,coins_per_click,coins_per_second,pickaxe_level,miner_level,pickaxe_price,miner_price,time
    coins = 0
    coins_per_click = 1
    coins_per_second = 0
    pickaxe_level = 1
    miner_level = 0
    pickaxe_price = 25
    miner_price = 50
    time = 0
    update_labels()
    save_data()



data = load_data()
coins = data["coins"]
coins_per_click = data["coins_per_click"]
coins_per_second = data["coins_per_second"]
pickaxe_level = data["pickaxe_level"]
miner_level = data["miner_level"]
pickaxe_price = data["pickaxe_price"]
miner_price = data["miner_price"]
time = data["time"]


title_label = ctk.CTkLabel(root,text="⛏️кликер шахтер",font=("Arial",32,"bold"))
title_label.pack(pady=20)

coins_label = ctk.CTkLabel(root,text="🪙монеты: 0",font=("Arial",24,"bold"))
coins_label.pack(pady=10)

timer_label = ctk.CTkLabel(root,text=f"Время в пещере:{time}",font=("Arial",28,"bold"))
timer_label.pack(pady=0)


stats_label = ctk.CTkLabel(root,text="характеристика",font=("Arial",16),justify="left")
stats_label.pack(pady=10)

mine_button = ctk.CTkButton(root,text="Добыть ресурсы",font=("Arial",22,"bold"),width=300,height=70,command=mine_crystal)
mine_button.pack(pady=20)

pickaxe_button = ctk.CTkButton(root,text="Улучшить кирку",font=("Arial",22,"bold"),width=300,height=60,command=buy_pickaxe)
pickaxe_button.pack(pady=10)

miner_button = ctk.CTkButton(root,text="Купить шахтера",font=("Arial",22,"bold"),width=300,height=60,command=buy_miner)
miner_button.pack(pady=10)

log_label = ctk.CTkLabel(root,text="Добро пожаловать в шахту!",font=("Arial",15),text_color="lightgray")
log_label.pack(pady=10)

reset_button = ctk.CTkButton(root,text="Сбросить игру",font=("Arial",14),
                             width=200,height=40,fg_color="darkred",hover_color="red",command=reset_game)
reset_button.pack(pady=5)

update_labels()
time_counter()

root.mainloop()