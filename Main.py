import tkinter as tk
from ToDo_Logic import  TodoList
from ToDo_Ui import TodoUi

if __name__ == "__main__":
    todo_list = TodoList()
    root = tk.Tk()
    app = TodoUi(root, todo_list)
    root.mainloop()