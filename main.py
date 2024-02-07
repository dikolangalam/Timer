import tkinter as tk
from datetime import timedelta

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer App")

        self.time_left = tk.StringVar()
        self.time_left.set("00:00:00")

        self.label = tk.Label(self.master, textvariable=self.time_left, font=("Helvetica", 48))
        self.label.pack(padx=20, pady=20)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=10)

        self.timer_running = False
        self.timer_value = 0
        self.update()

    def start_timer(self):
        self.timer_running = True
        self.timer_value = 0
        self.update()

    def stop_timer(self):
        self.timer_running = False

    def update(self):
        if self.timer_running:
            self.timer_value += 0.5
            time_str = str(timedelta(seconds=self.timer_value))
            self.time_left.set(time_str)
            self.master.after(1000, self.update)
        else:
            self.master.after(100, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
