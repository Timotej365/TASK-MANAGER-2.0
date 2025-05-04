import pytest
from unittest.mock import patch
import mysql.connector
from src.task_manager_1_1_pre_mockup import pripojenie_db, vytvor_tabulku, pridat_ulohu, aktualizovat_ulohu, odstranit_ulohu

# Priprav databazu
spojenie = pripojenie_db()
vytvor_tabulku(spojenie)

# -----------------------------
# TEST: Pridanie úlohy (pozitívny scenár)
# -----------------------------
def test_pridat_ulohu_ok():
    with patch("builtins.input", side_effect=["Test úloha", "Popis test"]):
        pridat_ulohu(spojenie)

    kurzor = spojenie.cursor()
    kurzor.execute("SELECT * FROM ulohy WHERE nazov = %s", ("Test úloha",))
    vysledok = kurzor.fetchone()
    assert vysledok is not None
    kurzor.execute("DELETE FROM ulohy WHERE nazov = %s", ("Test úloha",))
    spojenie.commit()
    kurzor.close()

# -----------------------------
# TEST: Pridanie úlohy (negatívny scenár – prázdny názov)
# -----------------------------
def test_pridat_ulohu_neplatny_vstup():
    with patch("builtins.input", side_effect=["", "Správny názov", "Správny popis"]):
        pridat_ulohu(spojenie)

    kurzor = spojenie.cursor()
    kurzor.execute("SELECT * FROM ulohy WHERE nazov = %s", ("Správny názov",))
    vysledok = kurzor.fetchone()
    assert vysledok is not None
    kurzor.execute("DELETE FROM ulohy WHERE nazov = %s", ("Správny názov",))
    spojenie.commit()
    kurzor.close()

# -----------------------------
# TEST: Aktualizácia úlohy (pozitívny scenár)
# -----------------------------
def test_aktualizovat_ulohu_ok():
    kurzor = spojenie.cursor()
    kurzor.execute("INSERT INTO ulohy (nazov, popis) VALUES (%s, %s)", ("Aktualizačná", "Popis"))
    spojenie.commit()
    kurzor.execute("SELECT id FROM ulohy WHERE nazov = %s", ("Aktualizačná",))
    id_ulohy = kurzor.fetchone()[0]

    with patch("builtins.input", side_effect=[str(id_ulohy), "1"]):
        aktualizovat_ulohu(spojenie)

    kurzor.execute("SELECT stav FROM ulohy WHERE id = %s", (id_ulohy,))
    assert kurzor.fetchone()[0] == "Prebieha"
    kurzor.execute("DELETE FROM ulohy WHERE id = %s", (id_ulohy,))
    spojenie.commit()
    kurzor.close()

# -----------------------------
# TEST: Aktualizácia úlohy (neexistujúce ID)
# -----------------------------
def test_aktualizovat_ulohu_neexistujuce_id():
    with patch("builtins.input", side_effect=["9999", "1"]):
        aktualizovat_ulohu(spojenie)  # očakávame len výpis chyby, nie výnimku

# -----------------------------
# TEST: Odstránenie úlohy (pozitívny scenár)
# -----------------------------
def test_odstranit_ulohu_ok():
    kurzor = spojenie.cursor()
    kurzor.execute("INSERT INTO ulohy (nazov, popis) VALUES (%s, %s)", ("Na zmazanie", "Popis"))
    spojenie.commit()
    kurzor.execute("SELECT id FROM ulohy WHERE nazov = %s", ("Na zmazanie",))
    id_ulohy = kurzor.fetchone()[0]

    with patch("builtins.input", return_value=str(id_ulohy)):
        odstranit_ulohu(spojenie)

    kurzor.execute("SELECT * FROM ulohy WHERE id = %s", (id_ulohy,))
    assert kurzor.fetchone() is None
    kurzor.close()

# -----------------------------
# TEST: Odstránenie úlohy (neexistujúce ID)
# -----------------------------
def test_odstranit_ulohu_neexistujuce_id():
    with patch("builtins.input", return_value="9999"):
        odstranit_ulohu(spojenie)  # očakávame len výpis chyby, nie výnimku
