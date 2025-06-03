# 🗂 Task Manager 2.0

Version 2.0 is an advanced task manager project that connects a console application in Python with a REST API built in Flask, a MySQL database, and a React frontend. This project was created as part of building a QA tester portfolio.

---

## 🚀 Functionality

- CRUD operations on tasks (Create, Read, Update, Delete)
- REST API (GET, POST, PUT, DELETE)
- MySQL database: storing and managing tasks
- Both the console application and the Flask API use the same database
- React frontend: display tasks by status, change status, delete tasks
- Automated tests using `pytest` (refactored and console versions)
- Simple styles for better readability and usability

---

## ⚙️ Technologies

- Python 3.11
- Flask
- MySQL (local, automatic DB and table creation via console)
- Postman (API testing)
- Pytest (unit + mock tests)
- React
- Playwright (planned E2E frontend tests)

---

## 🛠️ Running the Project

### 1. Run the console application

```bash
python src/task_manager_1_1_pre_mockup.py
```

➡️ The application will create a MySQL database and a table named `task_manager_1_1`.

### 2. Run the Flask API

```bash
python API.py
```

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
│   └── e2e/                                # (rezervované pre Playwright testy)
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

- Automatické pytest testy pre backend (2 verzie)

- E2E testovanie cez Playwright (pripravuje sa)

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
