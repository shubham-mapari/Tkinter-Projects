import tkinter as tk
from datetime import datetime

def calculate_age():
    dob = birthdate_entry.get()
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

        if age < 18:
            result_label.config(text="You cannot vote")
        else:
            result_label.config(text="You can vote")
    except ValueError:
        result_label.config(text="Invalid date format! Use YYYY-MM-DD")


window = tk.Tk()
window.title("You can vote or not")
window.geometry('500x440')
window.configure(bg='#333333')

age_calculator_label = tk.Label(window, text='You can vote or note ', bg='#FF3399', font=("Arial", 20))
age_calculator_label.pack(pady=20)

birthdate_label = tk.Label(window, text='Enter Your DOB (YYYY-MM-DD):', font=("Arial", 16), bg='skyblue')
birthdate_label.pack(pady=5)

birthdate_entry = tk.Entry(window, font=("Arial", 16))
birthdate_entry.pack(pady=10)

submit_button = tk.Button(window, text='Submit', command=calculate_age, font=("Arial", 16))
submit_button.pack(pady=10)

result_label = tk.Label(window, text='', font=("Arial", 16), bg='#333333')
result_label.pack(pady=10)
 
window.mainloop()
