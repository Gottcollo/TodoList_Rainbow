import json
import os
from datetime import datetime, date

FILENAME = "tasks.json"

def save_tasks(tasks_list):
    """Speichert die Aufgabenliste als JSON-Datei (Task, Datum, Priorität)."""
    try:
        # Datum in ISO-Format konvertieren
        serializable_list = [
            {
                "task": t,
                "date": d.isoformat() if d else None,
                "priority": p
            }
            for t, d, p in tasks_list
        ]
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(serializable_list, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("Fehler beim Speichern:", e)
        return False

def load_tasks():
    """Lädt Aufgaben aus JSON-Datei und konvertiert Datum zurück zu datetime.date."""
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            tasks_list = json.load(f)

        corrected_list = []
        for t in tasks_list:
            task = t.get("task")
            due_date = datetime.fromisoformat(t["date"]).date() if t.get("date") else None
            priority = t.get("priority", "Low")  # Default-Priorität
            corrected_list.append((task, due_date, priority))

        return corrected_list
    except Exception as e:
        print("Fehler beim Laden:", e)
        return []
