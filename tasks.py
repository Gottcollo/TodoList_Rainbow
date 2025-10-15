import storage

# beim Start laden
tasks_list = storage.load_tasks()  # jetzt Liste von (task, date)

def add_task(task, date=None):
    if task and task.strip() != "":
        tasks_list.append((task, date))  # Tuple: Aufgabe + Datum
        return True
    return False

def delete_task(index):
    try:
        tasks_list.pop(index)
        return True
    except IndexError:
        return False

def get_tasks():
    return tasks_list
