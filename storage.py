import json
import os

FILENAME = "tasks.json"

def save_tasks(tasks_list):
    """Speichert die Aufgabenliste als JSON-Datei."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(tasks_list, f, ensure_ascii=False, indent=4)
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
            tasks_list = json.load(f)
        # Sicherheitscheck – falls Datei leer oder kaputt
        if isinstance(tasks_list, list):
            return tasks_list
        else:
            print("Warnung: Ungültiges Format in tasks.json, leere Liste wird verwendet.")
            return []
    except Exception as e:
        print("Fehler beim Laden:", e)
        return []
