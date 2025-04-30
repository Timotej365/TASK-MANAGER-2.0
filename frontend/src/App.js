import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [ulohy, setUlohy] = useState([]);
  const [nazov, setNazov] = useState("");
  const [popis, setPopis] = useState("");

  useEffect(() => {
    nacitajUlohy();
  }, []);

  const nacitajUlohy = async () => {
    try {
      const odpoved = await fetch("http://127.0.0.1:5000/tasks");
      const data = await odpoved.json();
      setUlohy(data);
    } catch (err) {
      console.error("Chyba pri načítaní úloh:", err);
    }
  };

  const pridajUlohu = async () => {
    if (!nazov || !popis) return alert("Zadaj názov aj popis.");
    try {
      await fetch("http://127.0.0.1:5000/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nazov, popis })
      });
      setNazov("");
      setPopis("");
      nacitajUlohy();
    } catch (err) {
      console.error("Chyba pri pridávaní úlohy:", err);
    }
  };

  const zmenStav = async (id, novyStav) => {
    try {
      await fetch(`http://127.0.0.1:5000/tasks/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ stav: novyStav })
      });
      nacitajUlohy();
    } catch (err) {
      console.error("Chyba pri zmene stavu:", err);
    }
  };

  const odstranUlohu = async (id) => {
    if (!window.confirm("Naozaj chceš úlohu vymazať?")) return;
    try {
      await fetch(`http://127.0.0.1:5000/tasks/${id}`, {
        method: "DELETE"
      });
      nacitajUlohy();
    } catch (err) {
      console.error("Chyba pri odstraňovaní úlohy:", err);
    }
  };

  const renderUlohy = (stav) => (
    ulohy.filter(u => u.stav === stav).map(u => (
      <li key={u.id}>
        <strong>{u.nazov}</strong>: {u.popis} | Stav: {u.stav}
        {stav === "Nezahájená" && (
          <>
            <button onClick={() => zmenStav(u.id, "Prebieha")}>Prebieha</button>
            <button onClick={() => odstranUlohu(u.id)}>Odstrániť</button>
          </>
        )}
        {stav === "Prebieha" && (
          <>
            <button onClick={() => zmenStav(u.id, "Hotová")}>Hotová</button>
            <button onClick={() => odstranUlohu(u.id)}>Odstrániť</button>
          </>
        )}
        {stav === "Hotová" && (
          <button onClick={() => odstranUlohu(u.id)}>Odstrániť</button>
        )}
      </li>
    ))
  );

  return (
    <div style={{ padding: "20px" }}>
      <h1>Task Manager 2.0 – React Frontend</h1>

      <input
        type="text"
        placeholder="Zadaj názov"
        value={nazov}
        onChange={(e) => setNazov(e.target.value)}
      />
      <input
        type="text"
        placeholder="Zadaj popis"
        value={popis}
        onChange={(e) => setPopis(e.target.value)}
      />
      <button onClick={pridajUlohu}>Pridať</button>

      <h2>🕒 Nezahájené úlohy</h2>
      <ul>{renderUlohy("Nezahájená")}</ul>

      <h2>🌺 Prebiehajúce úlohy</h2>
      <ul>{renderUlohy("Prebieha")}</ul>

      <h2>✅ Hotová úlohy</h2>
      <ul>{renderUlohy("Hotová")}</ul>
    </div>
  );
}

export default App;
