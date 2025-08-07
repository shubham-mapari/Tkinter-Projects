import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S') 
    label.config(text=current_time)  
    label.after(1000, update_time)  


root = tk.Tk()
root.title("Digital Watch")


label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

update_time()

root.mainloop()
