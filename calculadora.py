import tkinter as tk

def ad_num(num):
    campo_texto.insert(tk.END, num)
def calcular():
    express = campo_texto.get()
    result = eval(express)
    campo_texto.delete(0,tk.END)
    campo_texto.insert(tk.END, result)

janela = tk.Tk()

campo_texto = tk.Entry(janela, width=20)
campo_texto.grid(row=0, column=0, columnspan=5)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]

row = 1 
col = 0
for botao in buttons:
    tk.Button(janela, text=botao, width=5, command=lambda num=botao: ad_num(num)).grid(row=row, column=col)
    col += 1 
    if col > 3:
        col = 0
        row += 1
tk.Button(janela, text="Calcular", width=20, command=calcular).grid(row=row, column=0, columnspan=5)
janela.mainloop()