import json
import os
from datetime import datetime

FILENAME = "tasks.json"

def save_tasks(tasks_list):
    """Speichert die Aufgabenliste als JSON-Datei."""
    try:
        # Konvertiere das Datum in ISO-Format (YYYY-MM-DD)
        serializable_list = [
            {"task": t, "date": d.isoformat() if d else None} for t, d in tasks_list
        ]
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(serializable_list, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("Fehler beim Speichern:", e)
        return False

def load_tasks():
    """Lädt Aufgaben aus der JSON-Datei, falls vorhanden."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        tasks_list = []
        for item in loaded:
            task = item.get("task")
            date_str = item.get("date")
            date_obj = datetime.fromisoformat(date_str).date() if date_str else None
            tasks_list.append((task, date_obj))
        return tasks_list
    except Exception as e:
        print("Fehler beim Laden:", e)
        return []
