import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog

root = tk.Tk()
root.geometry("900x800")
root.title("PyPad")
root.call('source', 'azure.tcl')
root.call('set_theme', 'dark')
filename = ""

class opacityS(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.result=None
        super().__init__(parent, title = title)

    def body(self,frame):
        tk.Label(frame, text="Opacity Slider").grid(row=0)
        self.entry_value = tk.Scale(frame, from_=0, to=100, orient="horizontal")
        self.entry_value.grid(row=1, column=1)
        return self.entry_value

    def apply(self):
        self.result = self.entry_value.get()
        return self.result

def load_file():

    filename = filedialog.askopenfilename()
    if filename != "":
        f2 = open(filename, 'r')
        dat = f2.read()
        f2.close()
        out.delete(1.0, "end-1c")
        out.insert("end-1c", dat)

def save():

    filename = filedialog.asksaveasfilename(filetypes=(("Text Document", "*.txt"), ("All Files", "*.*")))
    if filename != "":
        tw = out.get('1.0', 'end-1c')
        file = open(filename, 'w')
        file.write(tw)
        file.close()

def bl():
    root.call('set_theme', 'dark')

def li():
    root.call('set_theme', 'light')

def opa():
    dialog = opacityS(root, "Opacity Selector")
    print(dialog.result)
    alpha = dialog.result / 100
    root.attributes("-alpha", alpha)

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
vis_men.add_command(label="Opacity", command=opa)
he_men.add_command(label="Help", command=msg)

out = tk.Text(root, height=6, font=('Arial', 15), bg="gray")
out.pack(padx=12, pady=12, fill="both", expand=True)

root.mainloop()
