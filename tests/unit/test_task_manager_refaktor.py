import pytest
import mysql.connector
from src.task_manager_refaktor import pridat_ulohu, aktualizovat_ulohu, odstranit_ulohu, zobrazit_ulohy



def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1111",
        database="task_manager_1_1"
    )

def test_pridanie_ulohy_spravne():
    spojenie = get_connection()
    kurzor = spojenie.cursor()

    # 1. Pridáme testovaciu úlohu do databázy
    pridat_ulohu("Testovacia úloha", "tester", spojenie)

    # 2. Overíme, že sa úloha naozaj uložila
    kurzor.execute("SELECT * FROM ulohy WHERE nazov = 'Testovacia úloha'")
    vysledok = kurzor.fetchone()
    assert vysledok is not None  # ak nič nenájde, test zlyhá

    # 3. Vyčistenie – po teste zmažeme testovaciu úlohu
    kurzor.execute("DELETE FROM ulohy WHERE nazov = 'Testovacia úloha'")
    spojenie.commit()
    spojenie.close()

def test_pridanie_ulohy_neplatne_vstupy():
    spojenie = get_connection()

    # Pokus o pridanie úlohy bez zadania používateľa (prázdny reťazec)
    with pytest.raises(ValueError):
        pridat_ulohu("Chybná úloha", "", spojenie)

    spojenie.close()

def test_aktualizacia_uloha_spravne():
    spojenie = get_connection()
    kurzor = spojenie.cursor()

    # 1. Pridáme testovaciu úlohu, ktorú budeme aktualizovať
    pridat_ulohu("Úloha na aktualizáciu", "tester", spojenie)

    # 2. Získame ID tejto úlohy podľa názvu
    kurzor.execute("SELECT id FROM ulohy WHERE nazov = 'Úloha na aktualizáciu'")
    vysledok = kurzor.fetchone()
    assert vysledok is not None
    id_ulohy = vysledok[0]

    # 3. Aktualizujeme stav úlohy na „Prebieha“
    aktualizovat_ulohu(id_ulohy, "Prebieha", spojenie)

    # 4. Overíme, že zmena prebehla správne
    kurzor.execute("SELECT stav FROM ulohy WHERE id = %s", (id_ulohy,))
    novy_stav = kurzor.fetchone()[0]
    assert novy_stav == "Prebieha"

    # 5. Vyčistenie – odstránime testovaciu úlohu
    kurzor.execute("DELETE FROM ulohy WHERE id = %s", (id_ulohy,))
    spojenie.commit()
    spojenie.close()

def test_aktualizacia_neexistujucej_ulohy():
    spojenie = get_connection()

    # Skúsime aktualizovať úlohu s ID, ktoré neexistuje
    neexistujuce_id = -999  # predpokladáme, že také ID určite v databáze nie je

    with pytest.raises(ValueError):
        aktualizovat_ulohu(neexistujuce_id, "Hotová", spojenie)

    spojenie.close()

def test_odstranenie_ulohy_spravne():
    spojenie = get_connection()
    kurzor = spojenie.cursor()

    # 1. Pridáme testovaciu úlohu
    pridat_ulohu("Úloha na odstránenie", "tester", spojenie)

    # 2. Získame jej ID
    kurzor.execute("SELECT id FROM ulohy WHERE nazov = 'Úloha na odstránenie'")
    vysledok = kurzor.fetchone()
    assert vysledok is not None
    id_ulohy = vysledok[0]

    # 3. Odstránime túto úlohu
    odstranit_ulohu(id_ulohy, spojenie)

    # 4. Overíme, že už v databáze neexistuje
    kurzor.execute("SELECT * FROM ulohy WHERE id = %s", (id_ulohy,))
    vysledok_po = kurzor.fetchone()
    assert vysledok_po is None

    spojenie.close()

def test_odstranenie_neexistujucej_ulohy():
    spojenie = get_connection()

    # Použijeme ID, ktoré neexistuje – napr. záporné číslo
    neexistujuce_id = -999

    with pytest.raises(ValueError):
        odstranit_ulohu(neexistujuce_id, spojenie)

    spojenie.close()

