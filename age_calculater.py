import tkinter as tk
from datetime import datetime

def calculate_age():
    dob = birthdate_entry.get()
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Invalid date format! Use YYYY-MM-DD")

window = tk.Tk()
window.title("<<AGE CALCULATOR>>")
window.geometry('500x440')
window.configure(bg='')


age_calculator_label = tk.Label(window, text='Age Calculator', bg='skyblue', font=("Arial", 20))
age_calculator_label.pack(pady=20)

birthdate_label = tk.Label(window, text='Enter Your DOB (YYYY-MM-DD):', font=("Arial", 16), bg='skyblue')
birthdate_label.pack(pady=5)

birthdate_entry = tk.Entry(window, font=("Arial", 16))
birthdate_entry.pack(pady=10)


calculate_button = tk.Button(window, text='Calculate Age', command=calculate_age, font=("Arial", 16))
calculate_button.pack(pady=10)


result_label = tk.Label(window, text='', font=("Arial", 16), bg='skyblue')
result_label.pack(pady=10)

 
window.mainloop()
