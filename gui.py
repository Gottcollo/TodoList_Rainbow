import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import tasks
import storage
import theme

def create_gui():
    root = tk.Tk()
    root.title("Rainbow-Liste")
    root.geometry("600x650")

    ## Eingabe für neue Aufgabe
    entry_task = tk.Entry(root, width=40)
    entry_task.pack(pady=10)

    ## Datumsauswahl
    entry_date = DateEntry(root, width=12)
    entry_date.pack(pady=5)

    ## Priorität Dropdown
    priority_var = tk.StringVar(value="Low")
    priority_combo = ttk.Combobox(
        root, textvariable=priority_var,
        values=["Low", "Medium", "High"],
        state="readonly", width=10
    )
    priority_combo.pack(pady=5)

    ## Liste selbst
    listbox_tasks = tk.Listbox(root, width=50, height=15)
    listbox_tasks.pack(pady=10)

    ## Farbmap für Priorität
    priority_colors = {"Low": "green", "Medium": "orange", "High": "red"}

    ## Aufgaben laden
    for task_item, task_date, task_priority in tasks.get_tasks():
        display_text = f"{task_item} | {task_date} | {task_priority}"
        listbox_tasks.insert(tk.END, display_text)

    ## Buttons Funktionen
    def add_task_gui():
        task_item = entry_task.get()
        due_date = entry_date.get_date()
        priority = priority_var.get()
        if tasks.add_task(task_item, due_date, priority):
            display_text = f"{task_item} | {due_date} | {priority}"
            listbox_tasks.insert(tk.END, display_text)
            entry_task.delete(0, tk.END)
            apply_theme(theme.get_current_theme())
        else:
            messagebox.showwarning("FAIL", "Irgendwas muss man eingeben!")

    def delete_task_gui():
        try:
            selected_index = listbox_tasks.curselection()[0]
            if tasks.delete_task(selected_index):
                listbox_tasks.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Fail", "Wähl was aus!")

    def on_close():
        storage.save_tasks(tasks.get_tasks())
        root.destroy()

    ## Buttons
    button_add = tk.Button(root, text="Hinzufügen", width=15, command=add_task_gui)
    button_add.pack(pady=5)

    button_delete = tk.Button(root, text="Löschen", width=15, command=delete_task_gui)
    button_delete.pack(pady=5)

    button_theme_back = tk.Button(root, text="Theme zurück", width=20)
    button_theme_back.pack(pady=5)

    button_theme = tk.Button(root, text="Theme wechseln", width=20)
    button_theme.pack(pady=10)

    ## Theme + Prioritätsfarben
    def apply_theme(current):
        # Fenster & Widgets färben
        root.configure(bg=current["bg"])
        listbox_tasks.configure(bg=current["bg"], fg=current["fg"])
        entry_task.configure(bg=current["entry_bg"], fg=current["entry_fg"])
        entry_date.configure(background=current["entry_bg"], foreground=current["entry_fg"])
        priority_combo.configure(background=current["entry_bg"], foreground=current["entry_fg"])
        button_add.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_delete.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_theme.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_theme_back.configure(bg=current["button_bg"], fg=current["button_fg"])

        # Listbox-Einträge nach Priorität färben
        for i, task in enumerate(tasks.get_tasks()):
            _, _, task_priority = task
            color = priority_colors.get(task_priority, current["fg"])
            listbox_tasks.itemconfig(i, fg=color)

    ## Theme Funktionen
    def switch_theme_gui():
        apply_theme(theme.next_theme())

    def switch_theme_back_gui():
        apply_theme(theme.prev_theme())

    button_theme.configure(command=switch_theme_gui)
    button_theme_back.configure(command=switch_theme_back_gui)

    apply_theme(theme.get_current_theme())

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
