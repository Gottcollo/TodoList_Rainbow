## gui herstellen
import tkinter as tk
from tkinter import messagebox
import tasks

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

    ## Funktionen für Buttons
    def add_task_gui():
        task = entry_task.get()
        if tasks.add_task(task):
            listbox_tasks.insert(tk.END, task)
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

    ##Button hinzufügen
    button_add = tk.Button(root, text="Hinzufügen", width=15, command=add_task_gui)
    button_add.pack(pady=5)

    button_delete = tk.Button(root, text="Löschen", width=15, command=delete_task_gui)
    button_delete.pack(pady=5)

    root.mainloop()
