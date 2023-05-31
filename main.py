import functions

import tkinter as tk
from tkinter import filedialog as fd
import os

win = tk.Tk()
w = 700
h = 500
# photo = tk.PhotoImage(file="icon.ico")
# win.iconphoto(False, photo)
win.title('EasyQoima')
win.geometry(f"{w}x{h}+350+70")
win.resizable(True, True)

def sayMoney():
    label_money = tk.Label(win, text="\"Время - деньги, достар!\"", padx=15, pady=15).pack()
def showPDF():
    os.startfile('table_example.pdf')
def openFiles():
    global list_files
    win.filename = fd.askopenfilename(initialdir="pdf", title = "Select A File", filetype=(("pdf files", "*.pdf"), ("all files", "*.*")))
    functions.find_book_place(win.filename)

    label_1 = tk.Label(win, text="Дайын!", padx=15, pady=15).pack()
    button_open_pfd = tk.Button(win, text="PDF-ті ашу", command=showPDF).pack()

sayMoney()
button = tk.Button(win, text="Файлды таңдау", command=openFiles)
button.place(relx=50, rely=50, anchor='center')
button.pack()


win.mainloop()

