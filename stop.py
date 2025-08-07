import tkinter as tk

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")

        self.running = False
        self.time_elapsed = 0  # Time in seconds

        self.label = tk.Label(master, text="00:00:00", font=('Arial', 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start, width=10)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop, width=10)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset, width=10)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update_clock()

    def update_clock(self):
        if self.running:
            self.time_elapsed += 1
            hours, remainder = divmod(self.time_elapsed, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.master.after(1000, self.update_clock)  # Update every second

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

# Create the main window
root = tk.Tk()
stopwatch = Stopwatch(root)

# Start the main loop
root.mainloop()
