import tkinter as tk
from tkinter import messagebox

class TodoUi:
    def __init__(self, root, todo_list):
        self.root = root
        self.todo_list = todo_list
        self.root.title("TODO LIST")

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remover Selecionada", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if self.todo_list.add_task(task):
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "A tarefa não pode estar vazia!")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.todo_list.remove_task(index)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.get_tasks():
            self.task_listbox.insert(tk.END, task)