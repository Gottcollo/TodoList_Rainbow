import json
import os

FILENAME = "tasks.json"

def save_tasks(tasks_list):
    """Speichert die Aufgabenliste als JSON-Datei."""
    try:
        # Jede Aufgabe als Dict speichern: {"task": "...", "date": "..."}
        data_to_save = [{"task": t[0], "date": str(t[1])} for t in tasks_list]
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
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
            data_loaded = json.load(f)
        # In Tuple (task, date) umwandeln
        tasks_list = [(item["task"], item.get("date")) for item in data_loaded]
        return tasks_list
    except Exception as e:
        print("Fehler beim Laden:", e)
        return []
