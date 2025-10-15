import storage

# beim Start laden
tasks_list = storage.load_tasks()  # Liste von (task, date[, priority])

# Alte Tasks upgraden
for i, t in enumerate(tasks_list):
    if len(t) == 2:
        tasks_list[i] = (t[0], t[1], "low")  # Standard-Priorität "low"

def add_task(task, date=None, priority="low"):
    if task and task.strip() != "":
        tasks_list.append((task, date, priority))
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
