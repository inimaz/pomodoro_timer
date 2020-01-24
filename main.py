import time
from tkinter import Tk, Label, Canvas, Frame, Button, BOTH, BOTTOM, RIGHT, TOP
from winsound import *


WIDTH = 170
HEIGHT = 50


class PomodoroUI():
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro timer")
        master.minsize(width=WIDTH, height=HEIGHT)
        master.iconbitmap('images/favicon.ico')
        self.clock = Label(master)
        self.clock.grid(row=0, column=1, padx=10, pady=10)

        self.start_button = Button(
            master, text="Start", fg='#fdf7de', bg='#ce2c2c', command=self.start_timer)
        self.start_button.grid(row=0, column=4, padx=10, pady=10)

    def start_timer(self):
        self.start_time = time.time()
        PlaySound("sounds/start_timer.wav", SND_FILENAME)
        self.__draw_clock()

    def __draw_clock(self):
        '''
        Draw the time that is passing by.
        The time of the pomodoro is a countdown starting in 25 min
        '''
        max_time = 10  # 25 * 60
        pomodoro_time = max_time - (time.time() - self.start_time)

        if pomodoro_time > 0:
            min = pomodoro_time // 60
            sec = pomodoro_time % 60
        # Call this function to update the clock every 200 ms
            self.clock.after(200, self.__draw_clock)
        if pomodoro_time <= 0:
            min = 0
            sec = 0
            self.out_of_time()
        t = "%02d:%02d" % (min, sec)
        self.clock.config(text=t)

    def out_of_time(self):
        '''
        User is out of time. Displays sound and changes color of the canvas
        and clock
        '''
        self.master.deiconify()


if __name__ == "__main__":
    root = Tk()
    PomodoroUI(root)
    root.mainloop()
