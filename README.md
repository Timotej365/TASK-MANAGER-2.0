# 🗂 Task Manager 2.0

Verzia 2.0 je rozšírený projekt správcu úloh, ktorý prepája konzolovú aplikáciu v Pythone s REST API postaveným vo Flasku, databázou MySQL a React frontendom. Projekt vznikol ako súčasť budovania portfólia QA testera a vývojára.

---

## 🚀 Funkcionalita

- CRUD operácie nad úlohami (Create, Read, Update, Delete)
- REST API (GET, POST, PUT, DELETE)
- MySQL databáza: ukladanie a správa úloh
- Konzolová aplikácia aj Flask API používajú tú istú databázu
- React frontend: zobrazenie úloh podľa stavu, zmena stavu, mazanie
- Jednoduché štýly pre lepšiu čitateľnosť a použiteľnosť

---

## ⚙️ Technológie

- Python 3.11
- Flask
- MySQL (lokálne, automatické vytvorenie DB a tabuľky cez konzolovku)
- Postman (API testovanie)
- Pytest (plánované)
- React
- Playwright (plánované E2E testy frontendu)

---

## 🛠️ Spustenie projektu

### 1. Spusti konzolovú aplikáciu

```bash
python task_manager_1_1.py
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

## 🔍 Testovanie

- **Manuálne testovanie**: prebehlo na konzolovej aj API úrovni
- **Postman kolekcia**: vytvorená a uložená v repozitári
- **Pytest testy**: budú doplnené po výuke na kurze
- **Playwright**: plánované pre webové E2E testy po doplnení React frontendu

---

## 📌 Poznámka

Tento projekt je súčasťou širšieho portfólia QA/testerských projektov.  
Pre viac informácií navštív [hlavný rozcestník portfólia](https://github.com/Timotej365/TESTER-PORTFOLIO-ROZCESTNIK).

---

## 👨‍💻 Autor

Timotej – junior QA tester & Python developer
