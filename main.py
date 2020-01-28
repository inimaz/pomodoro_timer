import time
from tkinter import Tk, Label, Button
from winsound import *


WIDTH = 120
HEIGHT = 50


class PomodoroUI():
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro timer")
        master.minsize(width=WIDTH, height=HEIGHT)
        master.iconbitmap('images/favicon.ico')
        # This window on top of any other Windows' window
        master.wm_attributes("-topmost", 1)
        self.clock = Label(master)
        self.clock.grid(row=0, column=1, padx=10, pady=10)

        self.main_button = Button(
            master, text="Start", fg='#fdf7de',
            bg="#22AB32", command=self.start_timer)
        self.main_button.grid(row=0, column=7, padx=20, pady=10)

        self.paused = False

    def start_timer(self):

        self.times_up = False
        self.pause_time_in_sec = 0  # Seconds that the pomodoro has been paused
        PlaySound("sounds/start_timer.wav", SND_FILENAME)
        self.start_time = time.time()
        self.main_button.config(
            text="Pause", bg='#ce2c2c', command=self.__pause)
        self.__draw_clock()

    def __pause(self):
        '''

        '''
        self.paused = True
        self.start_paused_time = time.time()
        self.main_button.config(
            text="Resume", bg='#22AB32', command=self.__resume)

    def __resume(self):
        '''
        '''
        self.end_paused_time = time.time()
        self.pause_time_in_sec = self.pause_time_in_sec + \
            self.end_paused_time - self.start_paused_time
        self.paused = False
        self.main_button.config(
            text="Pause", bg='#ce2c2c', command=self.__pause)

    def __draw_clock(self):
        '''
        Draw the time that is passing by.
        The time of the pomodoro is a countdown starting in 25 min
        '''
        max_time = 10  # 25 * 60
        pomodoro_time = max_time - \
            (time.time() - self.start_time) + self.pause_time_in_sec

        if not(self.paused):
            if pomodoro_time > 0:
                min = pomodoro_time // 60
                sec = pomodoro_time % 60

            if pomodoro_time <= 0:
                min = 0
                sec = 0
                self.out_of_time()
            t = "%02d:%02d" % (min, sec)
            self.clock.config(text=t)

        if not(self.times_up):
                # Call this function to update the clock every 200 ms
            self.clock.after(200, self.__draw_clock)

    def out_of_time(self):
        '''
        User is out of time. Displays sound and changes color of the button
        and clock
        '''
        self.master.deiconify()
        PlaySound("sounds/start_timer.wav", SND_FILENAME)
        PlaySound("sounds/clock_alarm_electronic_beep.wav", SND_FILENAME)
        self.main_button.config(
            text="Restart", bg="#22AB32", command=self.start_timer)
        self.times_up = True


if __name__ == "__main__":
    root = Tk()
    PomodoroUI(root)
    root.mainloop()
