import random
import tkinter as tk
from tkinter import messagebox
import xlrd
window=tk.Tk()

window.title('Call Name')

window.geometry('300x400')
excel_path = tk.Entry(

    window,

    width=50

)
excel_path.pack()
x_values = []
def load_excel():
    try:
        reader = xlrd.open_workbook(excel_path.get())
        sheet = reader.sheet_by_index(0)
        global x_values
        x_values = sheet.col_values(0)
    except:
        tk.messagebox.showwarning(title='Warning', message='Read excel Error!')
btn_read_name=tk.Button(

    window,

    text='load',

    width=15,

    height=2,

    command=load_excel

)
btn_read_name.pack(pady=30)
var=tk.StringVar()
lab_show=tk.Label(

    window,

    textvariable=var,

    bg='black',

    fg='white',

    font=('Arial',12),

    width=15,

    height=2

)
lab_show.pack(pady=30)
def rand_get_name():

    var.set('')

    var.set(x_values[random.randint(0, len(x_values)-1)])
btn_rand_name=tk.Button(

    window,

    text='Click',

    width=15,

    height=2,

    command=rand_get_name

)
btn_rand_name.pack(pady=30)
window.mainloop()