import tkinter as tk
from tkinter import messagebox
import tasks
import storage
import theme  # importiertes Theme-Modul

def create_gui():
    root = tk.Tk()
    root.title("Rainbow-Liste")
    root.geometry("600x600")

    ## Eingabe für neue Aufgabe
    entry_task = tk.Entry(root, width=40)
    entry_task.pack(pady=10)

    ## Liste selbst 
    listbox_tasks = tk.Listbox(root, width=50, height=15)
    listbox_tasks.pack(pady=10)

    ## Vorhandene Aufgaben aus JSON laden
    for task_item in tasks.get_tasks():
        listbox_tasks.insert(tk.END, task_item)

    ## Funktionen für Buttons
    def add_task_gui():
        task_item = entry_task.get()
        if tasks.add_task(task_item):
            listbox_tasks.insert(tk.END, task_item)
            entry_task.delete(0, tk.END)
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

    ## Buttons hinzufügen
    button_add = tk.Button(root, text="Hinzufügen", width=15, command=add_task_gui)
    button_add.pack(pady=5)

    button_delete = tk.Button(root, text="Löschen", width=15, command=delete_task_gui)
    button_delete.pack(pady=5)

    button_theme_back = tk.Button(root, text="Theme zurück", width=20)
    button_theme_back.pack(pady=5)

    button_theme = tk.Button(root, text="Theme wechseln", width=20)
    button_theme.pack(pady=10)

    ## Theme-Funktionen (jetzt existieren alle Buttons)
    def switch_theme_gui():
        current = theme.next_theme()
        root.configure(bg=current["bg"])
        listbox_tasks.configure(bg=current["bg"], fg=current["fg"])
        entry_task.configure(bg=current["entry_bg"], fg=current["entry_fg"])
        button_add.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_delete.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_theme.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_theme_back.configure(bg=current["button_bg"], fg=current["button_fg"])

    def switch_theme_back_gui():
        current = theme.prev_theme()
        root.configure(bg=current["bg"])
        listbox_tasks.configure(bg=current["bg"], fg=current["fg"])
        entry_task.configure(bg=current["entry_bg"], fg=current["entry_fg"])
        button_add.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_delete.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_theme.configure(bg=current["button_bg"], fg=current["button_fg"])
        button_theme_back.configure(bg=current["button_bg"], fg=current["button_fg"])

    # Buttons mit Theme-Funktionen verbinden
    button_theme.configure(command=switch_theme_gui)
    button_theme_back.configure(command=switch_theme_back_gui)

    # Initiales Theme setzen
    switch_theme_gui()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
