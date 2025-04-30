# === API.py ===
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

# Funkcia na pripojenie k databáze
def pripojenie_db():
    try:
        spojenie = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="task_manager_1_1"
        )
        return spojenie
    except Error as e:
        print("Chyba pri pripájaní k databáze:", e)
        return None

@app.route('/tasks', methods=['GET'])
def get_tasks():
    spojenie = pripojenie_db()
    cursor = spojenie.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ulohy")
    ulohy = cursor.fetchall()
    cursor.close()
    spojenie.close()
    return jsonify(ulohy), 200

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    spojenie = pripojenie_db()
    cursor = spojenie.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ulohy WHERE id = %s", (id,))
    uloha = cursor.fetchone()
    cursor.close()
    spojenie.close()
    if uloha:
        return jsonify(uloha), 200
    else:
        return jsonify({"error": "Úloha neexistuje."}), 404

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    nazov = data.get("nazov")
    popis = data.get("popis")
    if not nazov or not popis:
        return jsonify({"error": "Názov a popis sú povinné."}), 400

    spojenie = pripojenie_db()
    cursor = spojenie.cursor()
    sql = "INSERT INTO ulohy (nazov, popis, stav) VALUES (%s, %s, 'Nezahájená')"
    cursor.execute(sql, (nazov, popis))
    spojenie.commit()
    nove_id = cursor.lastrowid
    cursor.close()
    spojenie.close()
    return jsonify({"message": "Úloha bola pridaná.", "id": nove_id}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    novy_stav = data.get("stav")
    if novy_stav not in ['Prebieha', 'Hotová']:
        return jsonify({"error": "Neplatný stav."}), 400

    spojenie = pripojenie_db()
    cursor = spojenie.cursor()
    cursor.execute("SELECT * FROM ulohy WHERE id = %s", (id,))
    if not cursor.fetchone():
        return jsonify({"error": "Úloha neexistuje."}), 404

    cursor.execute("UPDATE ulohy SET stav = %s WHERE id = %s", (novy_stav, id))
    spojenie.commit()
    cursor.close()
    spojenie.close()
    return jsonify({"message": f"Úloha {id} bola aktualizovaná na '{novy_stav}'."}), 200

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    spojenie = pripojenie_db()
    cursor = spojenie.cursor()
    cursor.execute("SELECT * FROM ulohy WHERE id = %s", (id,))
    if not cursor.fetchone():
        return jsonify({"error": "Úloha neexistuje."}), 404

    cursor.execute("DELETE FROM ulohy WHERE id = %s", (id,))
    spojenie.commit()
    cursor.close()
    spojenie.close()
    return jsonify({"message": f"Úloha {id} bola odstránená."}), 200

if __name__ == '__main__':
    app.run(debug=True)
