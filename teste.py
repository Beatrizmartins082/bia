import tkinter as tK 
def evaluate(event): 
    result_label.config(text=str(eval(entry.get()))) 
    root = tK.Tk() 
    root.title("Calculadora Simples") 
    entry = tK.Entry(root) 
    entry.bind("<Return>", evaluate) 
    entry.pack()
    result_label = tK.Label(root, text="") 
    result_label.pack()
    root.geometry("250x80")
    root.mainloop()