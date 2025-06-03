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

➡️ The API runs on `http://127.0.0.1:5000`

---

➡️ Run the React frontend

```bash
cd frontend
npm install
npm start
```

➡️ The frontend will be available at http://localhost:3000/.

## 📬 API Endpoints

| Method | Endpoint       | 	Description                 |
|--------|----------------|-------------------------------|
| GET    | /tasks         | Retrieve all active tasks   |
| POST   | /tasks         | 	Add a new task             |   
| PUT    | /tasks/<id>    | Update the status of a task        |
| DELETE | /tasks/<id>    | Delete a task by ID       |

---

## 📦 Postman Collection

The file task_manager_2_0_api_collection.json contains tests for all CRUD operations on tasks:

GET all tasks
POST create a new task
PUT update task status
DELETE task
GET non-existent task (negative scenario)

The tests use variables and validate API responses.

👉 The collection can be imported into Postman and run as a testing demo.

---

## 🧪 Testing
✅ Automated tests – pytest 

The project includes two tested versions of the application:

1. Refactored version (testable without input())
- Source file: src/task_manager_refaktor.py

- Tests: tests/unit/test_task_manager_refaktor.py

- Tests cover CRUD operations directly on the database with input validation.

2. Console version (mocked inputs)
- Source file: src/task_manager_1_1_pre_mockup.py

- Tests: tests/unit/test_task_manager_mockup.py

- Uses unittest.mock.patch() to simulate console inputs (input()).

▶️ Run tests:
Run all unit tests:
```bash
python -m pytest tests/unit/ -v
```

Run a specific test:
```bash
python -m pytest tests/unit/test_task_manager_refaktor.py -v
```
---

## 🖼️ Frontend
The frontend application is built with React and allows:

-Viewing tasks divided by status: Not Started, In Progress, Completed
-Adding new tasks
-Changing task status
-Deleting tasks with confirmation
-Simple styles for better readability and usability
-Styles are defined in the App.css file and imported in App.js.

---

## 📁 Project Structure

<pre>
task-manager-2.0/
├── src/
│   ├── task_manager_refaktor.py           # testable version
│   └── task_manager_1_1_pre_mockup.py     # console version with input()
│
├── tests/
│   ├── unit/
│   │   ├── test_task_manager_refaktor.py  # tests without input()
│   │   └── test_task_manager_mockup.py    # tests with mocked input()
│   │
│   └── e2e/                                # (reserved for Playwright tests in TM 2.1)
│
├── frontend/                              # React application
│
├── postman collection and photos/         # Postman collection + test screenshots
│
├── API.py
├── README.md
└── .gitignore
</pre>

---

🔍 Manual Testing

Console version tested manually (CRUD via terminal)
API tested manually via Postman collection

---

## 📌 Note
For a quick overview of running and using the application, I recommend reviewing the attached photo documentation.
Screenshots from the testing process and application usage can be found in the folder:
📁 [priebeh spustenim a CRUD operaciami-foto](https://github.com/Timotej365/TASK_MANAGER-2.0/tree/main/priebeh%20spustenim%20a%20CRUD%20operaciami-foto)

This project is part of a broader portfolio of QA/testing projects.
For more information, visit the [hlavný rozcestník portfólia](https://github.com/Timotej365/TESTER-PORTFOLIO-ROZCESTNIK).

---

## 👨‍💻 Author

Timotej – junior software tester
