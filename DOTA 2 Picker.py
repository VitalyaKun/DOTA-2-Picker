import sqlite3
from collections import defaultdict
from statistics import mean
import tkinter as tk
from tkinter import ttk

min_win_rates = {}


class DotaPicker:
    def __init__(self, root):
        self.root = root
        self.root.title("DOTA 2 Picker")
        self.root.geometry("500x450")
        
        #список героев
        self.heroes = ['muerta', 'abaddon', 'alchemist', 'ancient-apparition', 'arc-warden', 'axe', 'bane', 'batrider', 'beastmaster', 'bloodseeker', 'bounty-hunter', 'brewmaster', 'bristleback', 'broodmother', 'centaur-warrunner', 'chaos-knight', 'chen', 'clinkz', 'clockwerk', 'crystal-maiden', 'dark-seer', 'dark-willow', 'dawnbreaker', 'dazzle', 'death-prophet', 'disruptor', 'doom', 'dragon-knight', 'drow-ranger', 'earth-spirit', 'earthshaker', 'elder-titan', 'ember-spirit', 'enchantress', 'enigma', 'faceless-void', 'grimstroke', 'gyrocopter', 'hoodwink', 'huskar', 'invoker', 'io', 'jakiro', 'juggernaut', 'keeper-of-the-light', 'kunkka', 'leshrac', 'lich', 'lifestealer', 'lina', 'lion', 'lone-druid', 'luna', 'lycan', 'magnus', 'marci', 'mars', 'medusa', 'meepo', 'mirana', 'monkey-king', 'morphling', 'naga-siren', 'natures-prophet', 'necrophos', 'night-stalker', 'nyx-assassin', 'ogre-magi', 'omniknight', 'oracle', 'outworld-destroyer', 'pangolier', 'phantom-assassin', 'phantom-lancer', 'phoenix', 'puck', 'pudge', 'pugna', 'queen-of-pain', 'razor', 'riki', 'rubick', 'sand-king', 'shadow-demon', 'shadow-fiend', 'shadow-shaman', 'silencer', 'skywrath-mage', 'slardar', 'slark', 'snapfire', 'sniper', 'spectre', 'spirit-breaker', 'storm-spirit', 'sven', 'techies', 'templar-assassin', 'terrorblade', 'tidehunter', 'timbersaw', 'tiny', 'treant-protector', 'troll-warlord', 'tusk', 'underlord', 'undying', 'ursa', 'vengeful-spirit', 'void-spirit', 'venomancer', 'viper', 'visage', 'warlock', 'weaver', 'windranger', 'winter-wyvern', 'witch-doctor', 'wraith-king', 'zeus']

        # создание Combobox
        self.combo_box_1 = ttk.Combobox(root, values=self.heroes)
        self.combo_box_2 = ttk.Combobox(root, values=self.heroes)
        self.combo_box_3 = ttk.Combobox(root, values=self.heroes)
        self.combo_box_4 = ttk.Combobox(root, values=self.heroes)
        self.combo_box_5 = ttk.Combobox(root, values=self.heroes)
        
        self.combo_box_1.pack()
        self.combo_box_2.pack()
        self.combo_box_3.pack()
        self.combo_box_4.pack()
        self.combo_box_5.pack()
        
        self.combo_box_1.bind('<KeyRelease>', self.handle_key_release)
        self.combo_box_2.bind('<KeyRelease>', self.handle_key_release)
        self.combo_box_3.bind('<KeyRelease>', self.handle_key_release)
        self.combo_box_4.bind('<KeyRelease>', self.handle_key_release)
        self.combo_box_5.bind('<KeyRelease>', self.handle_key_release)
        
        hero_01 = self.combo_box_1.get()
        hero_02 = self.combo_box_2.get()
        hero_03 = self.combo_box_3.get()
        hero_04 = self.combo_box_4.get()
        hero_05 = self.combo_box_5.get()
        
        # добавление кнопки
        self.button = ttk.Button(root, text="Выбрать героев", command=self.handle_selection)
        self.button.pack()

    def handle_key_release(self, event):
        # получение введенной пользователем строки
        typed_string = event.widget.get()
        
        # очистка списка значений Combobox
        event.widget['values'] = []
        
        # поиск совпадений среди всех героев и добавление их в список
        matches = [hero for hero in self.heroes if typed_string in hero]
        event.widget['values'] = matches
    
    def handle_selection(self):
        hero_01 = self.combo_box_1.get()
        hero_02 = self.combo_box_2.get()
        hero_03 = self.combo_box_3.get()
        hero_04 = self.combo_box_4.get()
        hero_05 = self.combo_box_5.get()

        heroes_list = [hero_01, hero_02, hero_03, hero_04, hero_05]
        known_heroes = list(filter(lambda hero: hero != "", heroes_list))
        
        if 1 == len(known_heroes):
            h_1 = what_procent_win_rate(hero_01)
            print("\nПредложенные герои:")
            stage_peak(h_1)
        
        if 2 == len(known_heroes):
            h_1 = what_procent_win_rate(hero_01)
            h_2 = what_procent_win_rate(hero_02)
            h_all = h_1 + h_2
            print("\nПредложенные герои:")
            stage_peak(h_all)
            
        if 3 == len(known_heroes):
            h_1 = what_procent_win_rate(hero_01)
            h_2 = what_procent_win_rate(hero_02)
            h_3 = what_procent_win_rate(hero_03)
            h_all = h_1 + h_2 + h_3
            print("\nПредложенные герои:")
            stage_peak(h_all)
                   
        if 4 == len(known_heroes):
            h_1 = what_procent_win_rate(hero_01)
            h_2 = what_procent_win_rate(hero_02)
            h_3 = what_procent_win_rate(hero_03)
            h_4 = what_procent_win_rate(hero_04)
            h_all = h_1 + h_2 + h_3 + h_4
            print("\nПредложенные герои:")
            stage_peak(h_all)

        if 5 == len(known_heroes):
            h_1 = what_procent_win_rate(hero_01)
            h_2 = what_procent_win_rate(hero_02)
            h_3 = what_procent_win_rate(hero_03)
            h_4 = what_procent_win_rate(hero_04)
            h_5 = what_procent_win_rate(hero_05)
            h_all = h_1 + h_2 + h_3 + h_4 + h_5
            print("\nПредложенные герои:")
            stage_peak(h_all)
        
            
            


        # добавление текстового поля для вывода результата
        self.result_label = ttk.Label(root, text=f"Выбранные герои: {hero_01}, {hero_02}, {hero_03}, {hero_04}, {hero_05}")
        self.result_label.pack()

def stage_peak(h_all):
    hero_rates = defaultdict(list)
    for hero, rate in h_all:
        hero_rates[hero].append(float(rate[:-1]))
    heroes = [(hero, f"{mean(rates):.1f}%") for hero, rates in hero_rates.items()]
    avg_win_rate(heroes)

def what_procent_win_rate(hero):
    link_conn = f"./tables/{hero}.db"
    with sqlite3.connect(link_conn, check_same_thread=False) as conn:
        c = conn.cursor()
        c.execute("SELECT name, win_rate FROM heroes ORDER BY win_rate ASC LIMIT 122")
        rows = c.fetchall()
    return rows

def avg_win_rate(heroes):
    heroes = sorted(heroes, key=lambda x: float(x[1][:-1]))[:10]
    for hero, win_rate in heroes:
        if hero in min_win_rates:
            if float(win_rate[:-1]) < min_win_rates[hero]:
                min_win_rates[hero] = float(win_rate[:-1])
        else:
            min_win_rates[hero] = float(win_rate[:-1])
        #print(f"{hero} - {(((float(win_rate[:-1]) - 50) * 3 * -1).toFixed(1)}"))
        print(hero)
        #self.text_area.insert(tk.END, f"{hero} - {win_rate}\n")

if __name__ == "__main__":
    root = tk.Tk()
    dota_picker = DotaPicker(root)
    root.mainloop()

