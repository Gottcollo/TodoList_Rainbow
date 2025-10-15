import os

FILENAME = "tasks.txt"

def save_tasks(tasks_list):
    """Schreibt alle Aufgaben in die Datei (eine Aufgabe pro Zeile)."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            for task in tasks_list:
                # optional: prüfen, dass keine Zeilenumbrüche in Aufgaben sind
                f.write(task + "\n")
        return True
    except Exception as e:
        print("Fehler beim Speichern:", e)
        return False

def load_tasks():
    """Liest Aufgaben aus der Datei und gibt eine Liste zurück."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Entferne Zeilenumbrüche
        tasks = [line.strip() for line in lines if line.strip() != ""]
        return tasks
    except Exception as e:
        print("Fehler beim Laden:", e)
        return []
