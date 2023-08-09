import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title = "packs"

tk.Label(root, text='Label left', bg='green').pack(side='left', fill='both',expand=True)

tk.Label(root, text='Label1', bg="red").pack(side='top',fill="both", expand=True)
tk.Label(root, text='Label2', bg="green").pack(side='top', fill="both", expand=True)

root.mainloop()
