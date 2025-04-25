# 🗂 Task Manager 2.0

Verzia 2.0 je rozšírený projekt správcu úloh, ktorý prepája konzolovú aplikáciu v Pythone s REST API postaveným vo Flasku a databázou MySQL. Projekt vznikol ako súčasť budovania portfólia QA testera a vývojára.

---

## 🚀 Funkcionalita

- CRUD operácie nad úlohami (Create, Read, Update, Delete)
- REST API (GET, POST, PUT, DELETE)
- MySQL databáza: ukladanie a správa úloh
- Konzolová aplikácia aj Flask API používajú tú istú databázu

---

## ⚙️ Technológie

- 🐍 Python 3.11
- 🌐 Flask
- 💾 MySQL (lokálne, automatické vytvorenie DB a tabuľky cez konzolovku)
- 🧪 Postman (API testovanie)
- 📋 Pytest (plánované)
- 💻 React (plánované frontend UI)
- 🧭 Playwright (plánované E2E testy frontendu)

---

## 🛠️ Spustenie projektu

### 1. Spusti konzolovú aplikáciu

```bash
python task_manager_1_1.py
➡️ Aplikácia vytvorí MySQL databázu a tabuľku s názvom task_manager_1_1.
-Spusti Flask API python - API.py
-API beží na http://127.0.0.1:5000

Metóda | Endpoint | Popis
GET | /tasks | Získať všetky aktívne úlohy
POST | /tasks | Pridať novú úlohu
PUT | /tasks/<id> | Aktualizovať stav úlohy
DELETE | /tasks/<id> | Odstrániť úlohu podľa ID
