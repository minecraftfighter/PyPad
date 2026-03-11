import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.geometry("900x800")
root.title("PyPad")
root.call('source', 'Azure/azure.tcl')
root.call('set_theme', 'dark')
filename = ""

def load_file():

    filename = filedialog.askopenfilename()
    f2 = open(filename, 'r')
    dat = f2.read()
    out.delete(1.0, "end-1c")
    out.insert("end-1c", dat)

def save():

    filename = filedialog.asksaveasfilename(filetypes=(("Text Document", "*.txt"), ("All Files", "*.*")))
    tw = out.get('1.0', 'end-1c')
    file = open(filename, 'w')
    file.write(tw)
    file.close()

def bl():
    root.call('set_theme', 'dark')

def li():
    root.call('set_theme', 'light')

def msg():
    messagebox.showinfo("HELP", "Enter the things you want to save.")


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

label = tk.Label(root, text="PyPad", font=('Arial', 15))
label.pack(padx=10, pady=10)

out = tk.Text(root, height=6, font=('Arial', 15))
out.pack(padx=12, pady=12)

root.mainloop()

