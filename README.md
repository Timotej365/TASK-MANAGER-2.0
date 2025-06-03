# 🗂 Task Manager 2.0

Verzia 2.0 je rozšírený projekt správcu úloh, ktorý prepája konzolovú aplikáciu v Pythone s REST API postaveným vo Flasku, databázou MySQL a React frontendom. Projekt vznikol ako súčasť budovania portfólia QA testera.

---

## 🚀 Funkcionalita

- CRUD operácie nad úlohami (Create, Read, Update, Delete)
- REST API (GET, POST, PUT, DELETE)
- MySQL databáza: ukladanie a správa úloh
- Konzolová aplikácia aj Flask API používajú tú istú databázu
- React frontend: zobrazenie úloh podľa stavu, zmena stavu, mazanie
- Automatické testy pomocou `pytest` (refaktorovaná aj konzolová verzia)
- Jednoduché štýly pre lepšiu čitateľnosť a použiteľnosť

---

## ⚙️ Technológie

- Python 3.11
- Flask
- MySQL (lokálne, automatické vytvorenie DB a tabuľky cez konzolovku)
- Postman (API testovanie)
- Pytest (unit + mock testy)
- React
- Playwright (plánované E2E testy frontendu v TM 2.1)

---

## 🛠️ Spustenie projektu

### 1. Spusti konzolovú aplikáciu

```bash
python src/task_manager_1_1_pre_mockup.py
```

➡️ Aplikácia vytvorí MySQL databázu a tabuľku s názvom `task_manager_1_1`.

### 2. Spusti Flask API

```bash
python API.py
```

➡️ API beží na `http://127.0.0.1:5000`

---

➡️ Spusti React frontend

```bash
cd frontend
npm install
npm start
```

➡️ Frontend bude dostupný na http://localhost:3000/.

## 📬 API Endpointy

| Metóda | Endpoint       | Popis                         |
|--------|----------------|-------------------------------|
| GET    | /tasks         | Získať všetky aktívne úlohy   |
| POST   | /tasks         | Pridať novú úlohu              |
| PUT    | /tasks/<id>    | Aktualizovať stav úlohy        |
| DELETE | /tasks/<id>    | Odstrániť úlohu podľa ID       |

---

## 📦 Postman kolekcia

Súbor `task_manager_2_0_api_collection.json` obsahuje testy všetkých CRUD operácií nad úlohami:
- GET všetkých úloh
- POST vytvorenie novej úlohy
- PUT aktualizácia stavu
- DELETE úlohy
- GET neexistujúcej úlohy (negatívny scenár)

Testy využívajú premenné a overujú odpovede API.

👉 Kolekciu je možné importovať do Postmanu a spustiť ako ukážku testovania.

---

## 🧪 Testovanie
✅ Automatické testy – pytest 

Projekt obsahuje dve testované verzie aplikácie:

1. Refaktorovaná verzia (testovateľná bez input())
- Zdrojový súbor: src/task_manager_refaktor.py

- Testy: tests/unit/test_task_manager_refaktor.py

- Testy pokrývajú CRUD operácie priamo nad databázou s validáciou vstupov.

2. Konzolová verzia (mockované vstupy)
- Zdrojový súbor: src/task_manager_1_1_pre_mockup.py

- Testy: tests/unit/test_task_manager_mockup.py

- Používa unittest.mock.patch() na simuláciu vstupov z konzoly (input()).

▶️ Spustenie testov:
Spusti všetky unit testy:
```bash
python -m pytest tests/unit/ -v
```

Spusti konkrétny test:
```bash
python -m pytest tests/unit/test_task_manager_refaktor.py -v
```
---

## 🖼️ Frontend
- Frontend aplikácie je postavený v Reacte a umožňuje:
- Zobrazenie úloh rozdelených podľa stavu: Nezahájená, Prebieha, Hotová
- Pridávanie nových úloh
- Zmenu stavu úloh
- Mazanie úloh s potvrdením
- Jednoduché štýly pre lepšiu čitateľnosť a použiteľnosť
- Štýly sú definované v súbore App.css a importované v App.js.

---

## 📁 Štruktúra projektu

<pre>
task-manager-2.0/
├── src/
│   ├── task_manager_refaktor.py           # testovateľná verzia
│   └── task_manager_1_1_pre_mockup.py     # konzolová verzia s input()
│
├── tests/
│   ├── unit/
│   │   ├── test_task_manager_refaktor.py  # testy bez input()
│   │   └── test_task_manager_mockup.py    # testy s mockovaním input()
│   │
│   └── e2e/                                # (rezervované pre Playwright testy v TM 2.1)
│
├── frontend/                              # React aplikácia
│
├── postman kolekcia a foto/               # Postman kolekcia + testovacie screenshoty
│
├── API.py
├── README.md
└── .gitignore
</pre>

---

🔍 Manuálne testovanie
- Konzolová verzia testovaná manuálne (CRUD cez terminál)

- API testované manuálne cez Postman kolekciu

---

## 📌 Poznámka
Pre rýchle prezretie spustenia a používania aplikácie odporúčam prezrieť priloženú fotodokumentáciu.
Snímky obrazovky z priebehu testovania a práce s aplikáciou nájdeš v priečinku:  
📁 [priebeh spustenim a CRUD operaciami-foto](https://github.com/Timotej365/TASK_MANAGER-2.0/tree/main/priebeh%20spustenim%20a%20CRUD%20operaciami-foto)

Tento projekt je súčasťou širšieho portfólia QA/testerských projektov.  
Pre viac informácií navštív [hlavný rozcestník portfólia](https://github.com/Timotej365/TESTER-PORTFOLIO-ROZCESTNIK).

---

## 👨‍💻 Autor

Timotej – junior software tester
