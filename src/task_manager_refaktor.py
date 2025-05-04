import mysql.connector
from mysql.connector import Error

# Pripojenie k databáze (vytvorí ak neexistuje)
def pripojenie_db():
    try:
        spojenie = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111"
        )
        kurzor = spojenie.cursor()
        kurzor.execute("CREATE DATABASE IF NOT EXISTS task_manager_1_1")
        spojenie.commit()
        kurzor.close()
        spojenie.close()

        spojenie = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="task_manager_1_1"
        )
        return spojenie
    except Error as e:
        raise ConnectionError(f"Chyba pri pripojení k databáze: {e}")

# Vytvorenie tabuľky ak neexistuje
def vytvor_tabulku(spojenie):
    try:
        cursor = spojenie.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ulohy (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nazov VARCHAR(255) NOT NULL,
                popis TEXT,
                stav ENUM('Nezahájená', 'Prebieha', 'Hotová') DEFAULT 'Nezahájená',
                datum_vytvoreni DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        spojenie.commit()
        cursor.close()
    except Error as e:
        raise RuntimeError(f"Chyba pri vytváraní tabuľky: {e}")

# Pridanie úlohy
def pridat_ulohu(nazov, popis, spojenie):
    if not nazov or not popis:
        raise ValueError("Názov aj popis úlohy musia byť vyplnené.")

    cursor = spojenie.cursor()
    try:
        sql = "INSERT INTO ulohy (nazov, popis) VALUES (%s, %s)"
        cursor.execute(sql, (nazov, popis))
        spojenie.commit()
    except Error as e:
        raise RuntimeError(f"Chyba pri ukladaní úlohy: {e}")
    finally:
        cursor.close()

# Zobrazenie aktívnych úloh
def zobrazit_ulohy(spojenie):
    cursor = spojenie.cursor()
    try:
        sql = "SELECT id, nazov, popis, stav FROM ulohy WHERE stav IN ('Nezahájená', 'Prebieha')"
        cursor.execute(sql)
        vysledky = cursor.fetchall()
        return vysledky
    except Error as e:
        raise RuntimeError(f"Chyba pri načítavaní úloh: {e}")
    finally:
        cursor.close()

# Ziskanie úlohy podľa ID
def ziskaj_ulohu_podla_id(id_ulohy, spojenie):
    cursor = spojenie.cursor()
    try:
        cursor.execute("SELECT * FROM ulohy WHERE id = %s", (id_ulohy,))
        return cursor.fetchone()
    except Error as e:
        raise RuntimeError(f"Chyba pri hľadaní úlohy: {e}")
    finally:
        cursor.close()

# Aktualizácia stavu úlohy
def aktualizovat_ulohu(id_ulohy, novy_stav, spojenie):
    if novy_stav not in ["Prebieha", "Hotová"]:
        raise ValueError("Neplatný stav")

    cursor = spojenie.cursor()
    try:
        if not ziskaj_ulohu_podla_id(id_ulohy, spojenie):
            raise ValueError("Úloha s daným ID neexistuje.")

        cursor.execute("UPDATE ulohy SET stav = %s WHERE id = %s", (novy_stav, id_ulohy))
        spojenie.commit()
    except Error as e:
        raise RuntimeError(f"Chyba pri aktualizácii: {e}")
    finally:
        cursor.close()

# Odstránenie úlohy
def odstranit_ulohu(id_ulohy, spojenie):
    cursor = spojenie.cursor()
    try:
        if not ziskaj_ulohu_podla_id(id_ulohy, spojenie):
            raise ValueError("Úloha s daným ID neexistuje.")

        cursor.execute("DELETE FROM ulohy WHERE id = %s", (id_ulohy,))
        spojenie.commit()
    except Error as e:
        raise RuntimeError(f"Chyba pri odstraňovaní: {e}")
    finally:
        cursor.close()

# --- Spustenie v konzolovom móde (voliteľné) ---
if __name__ == "__main__":
    spojenie = pripojenie_db()
    vytvor_tabulku(spojenie)

    while True:
        print("\nSprávca ú loh")
        print("1. Pridať ú lohu")
        print("2. Zobraziť ú lohy")
        print("3. Aktualizovať ú lohu")
        print("4. Odstrániť ú lohu")
        print("5. Koniec")
        vyber = input("Zadaj voľbu: ")

        try:
            if vyber == "1":
                nazov = input("Názov: ")
                popis = input("Popis: ")
                pridat_ulohu(nazov, popis, spojenie)
            elif vyber == "2":
                ulohy = zobrazit_ulohy(spojenie)
                for id, nazov, popis, stav in ulohy:
                    print(f"#{id} | {nazov} - {popis} [{stav}]")
            elif vyber == "3":
                id_ulohy = int(input("Zadaj ID úlohy: "))
                stav = input("Zadaj stav (Prebieha/Hotová): ")
                aktualizovat_ulohu(id_ulohy, stav, spojenie)
            elif vyber == "4":
                id_ulohy = int(input("Zadaj ID úlohy na odstránenie: "))
                odstranit_ulohu(id_ulohy, spojenie)
            elif vyber == "5":
                break
            else:
                print("Neplatná voľba")
        except Exception as e:
            print(f"Chyba: {e}")

    spojenie.close()
