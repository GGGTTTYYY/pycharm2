import xlrd
import random
import tkinter as tk
import pygame
# 点名
workbook = xlrd.open_workbook("name.xls")  # 读取表格
Data_sheet = workbook.sheets()[0]  # 读取sheet1
name_list = Data_sheet.col_values(1)  # 读取第二列
data = set()  # 一个空set保存选过的同学
root = tk.Tk()
root.title("点名册")
root.geometry('250x150')
global var
var = tk.StringVar()
on_strat = False
l = tk.Label(root, textvariable=var, font=('Arial', 35), width=15, height=2)
l.pack()
def start():
    try:
        rdata = random.choice(name_list)
        if on_strat == False:
            name_list.remove(rdata)
            if rdata not in data:
                var.set(rdata)
                data.add(rdata)
        if len(name_list) == 0:
            var.set("-----所有同学已经遍历完-------")
    except ValueError as e:
        var.set("-----所有同学已经遍历完-------")
B = tk.Button(root, text="start", command=start)
B.pack()
# pygame.init()
# music = pygame.mixer.music.load('bg.mp3')
# pygame.mixer.music.play(-1, 100)
# screen = pygame.display.set_mode((800, 600))
root.mainloop()