import sqlite3
import requests
from bs4 import BeautifulSoup

with open('hero_link.txt') as heroes:
    for hero in heroes:
        hero_rstrip = hero.strip()
        url = f'https://www.dotabuff.com/heroes/{hero_rstrip}/counters'
        print(url)
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        headers = {
            'User-Agent': user_agent
        }
        try:
            link_conn = f'C:/Users/Public/Documents/{hero_rstrip}.db'
            print(link_conn)
            conn = sqlite3.connect(link_conn, check_same_thread=False)
            c = conn.cursor()
            c.execute('''CREATE TABLE heroes
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          win_rate REAL)''')
        except sqlite3.OperationalError:
            pass

        response = requests.get(url, headers=headers, timeout=5)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        data = []
        for tr in soup.find_all('tr'):
            hero_name_elem = tr.find('td', {'class': 'cell-xlarge'})
            if hero_name_elem:
                hero_name = hero_name_elem.find('a').text
                win_rate = tr.find_all('td')[3].text.strip()
                data.append((hero_name, win_rate))
                print(hero_name, win_rate)

        c.executemany("INSERT INTO heroes (name, win_rate) VALUES (?, ?)", data)
        conn.commit()
        conn.close()
