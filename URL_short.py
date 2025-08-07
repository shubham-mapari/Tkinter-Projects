import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("500x300")

def shorten():
    shortener = pyshorteners.Shortener()
    short_URL = shortener.tinyurl.short(longURL_entry.get())
    print(shortURL_entry.insert(0,short_URL))

longURL_label = tkinter.Label(root,text="Enter Long URL")
longURL_entry = tkinter.Entry(root)
shortURL_label = tkinter.Label(root,text ="Output Shortened URL")
shortURL_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root,text="Shorten URL",command=shorten)

longURL_label.pack()
longURL_entry.pack()
shortURL_label.pack()
shortURL_entry.pack()
shorten_button.pack()


root.mainloop()