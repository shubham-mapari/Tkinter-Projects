import tkinter as tk


currency_rates = {
    "INR": 1.0,
    "USD": 0.012,
    "EUR": 0.011,
    "JPY": 1.70
}

def convert():
    try:
        amount = float(entry_amount.get())  
        from_currency = dropdown_from.get()
        to_currency = dropdown_to.get()

        in_inr = amount / currency_rates[from_currency]
        
        converted_amount = in_inr * currency_rates[to_currency]

        label_result.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    
    except:
        label_result.config(text="Please enter valid amount!")


window = tk.Tk()
window.title("Simple Currency Converter")
window.geometry("350x300")
window.config(bg="lightblue")


label_title = tk.Label(window, text="Currency Converter", font=("Arial", 16), bg="lightblue")
label_title.pack(pady=10)

label_amount = tk.Label(window, text="Enter Amount:", bg="lightblue")
label_amount.pack()
entry_amount = tk.Entry(window)
entry_amount.pack(pady=5)

label_from = tk.Label(window, text="From Currency:", bg="lightblue")
label_from.pack()
dropdown_from = tk.StringVar()
dropdown_menu_from = tk.OptionMenu(window, dropdown_from, *currency_rates.keys())
dropdown_menu_from.pack()
dropdown_from.set("INR")

label_to = tk.Label(window, text="To Currency:", bg="lightblue")
label_to.pack()
dropdown_to = tk.StringVar()
dropdown_menu_to = tk.OptionMenu(window, dropdown_to, *currency_rates.keys())
dropdown_menu_to.pack()
dropdown_to.set("USD")  


button_convert = tk.Button(window, text="Convert", command=convert, bg="green", fg="white")
button_convert.pack(pady=10)

label_result = tk.Label(window, text="", font=("Arial", 12), bg="lightblue")
label_result.pack(pady=10)

window.mainloop()
