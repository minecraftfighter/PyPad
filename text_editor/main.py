import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.geometry("500x400")
root.title("python-TextEditor")
root.call('source', 'Azure/azure.tcl')
root.call('set_theme', 'dark')
filename = ""

def load_file():

    filename = fne.get(1.0, 'end-1c')
    f2 = open(filename, 'r')
    dat = f2.read()
    out.delete(1.0, "end-1c")
    out.insert("end-1c", dat)

def save():

    filename = fne.get(1.0, 'end-1c')
    tw = out.get('1.0', 'end-1c')
    file = open(filename, 'w')
    file.write(tw)
    file.close()

def bl():

    root.call('set_theme', 'dark')

def li():
    root.call('set_theme', 'light')

def msg():
    messagebox.showinfo("HELP", "Enter the filename to the first box, and enter the information to the second box.")


menuu = tk.Menu(root)
root.configure(menu=menuu)

file_men = tk.Menu(menuu)
vis_men = tk.Menu(menuu)
he_men = tk.Menu(menuu)
menuu.add_cascade(label="Files", menu=file_men)
menuu.add_cascade(label="Windows", menu=vis_men)
menuu.add_cascade(label="Help", menu=he_men)
file_men.add_command(label="Save", command=save)
file_men.add_command(label="Load", command=load_file)
vis_men.add_command(label="Dark", command=bl)
vis_men.add_command(label="Light", command=li)
he_men.add_command(label="Help", command=msg)

label = tk.Label(root, text="Python-TextEditor", font=('Arial', 15))
label.pack(padx=10, pady=10)

lab1 = tk.Label(root, text="Filename", font=('Arial', 15))
lab1.pack(padx=5, pady=5)

fne = tk.Text(root,height=1, font=('Arial', 15))
fne.pack(padx=12, pady=12)

lab2 = tk.Label(root, text="Input", font=('Arial', 15))
lab2.pack(padx=5, pady=5)

out = tk.Text(root, height=4, font=('Arial', 15))
out.pack(padx=12, pady=12)

root.mainloop()