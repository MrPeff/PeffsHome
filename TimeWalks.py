import time;
import datetime
from time import mktime
from datetime import timedelta
from tkinter import *
from tkinter import ttk

#Layout:
# Start:        ______
# Arbetsid:     ______
# Lunch etc:    ______
# Start         Slut
# ______        ______
# Passerat      Kvar
# ______        ______
#_______________________________________________________________________________
class GuiApp2:
    def PetersCB(self, blaha):
        print("Calling PetersCB")
        self.Text_Start.delete('1.0', END)
        self.Text_Start.insert(END, self.Start_h.get())
        self.Text_Slut.delete('1.0', END)
        self.Text_Past.delete('1.0', END)
        self.Text_Left.delete('1.0', END)

        today = datetime.datetime.now()
        print(today)
        try:
            today_date = today.date()
            time_start = time.strptime(self.Start_h.get(),       "%H.%M")
            today_time = datetime.time(hour=time_start.tm_hour, minute=time_start.tm_min)
            self.dt_start = datetime.datetime.combine(today_date, today_time)

            time_wt = time.strptime(self.WorkTime_h.get(),       "%H.%M")
            self.dt_delta_wt = datetime.timedelta(hours=time_wt.tm_hour, minutes=time_wt.tm_min)

            time_nwt = time.strptime(self.NonWorkTime_h.get(),   "%H.%M")
            self.dt_delta_nwt = datetime.timedelta(hours=time_nwt.tm_hour, minutes=time_nwt.tm_min)
        except:
            print("Arne Weizing")

        dt_end = self.dt_start + self.dt_delta_wt + self.dt_delta_nwt
        dt_end_str = str(dt_end.hour) + "." + str(dt_end.minute)
        self.Text_Slut.insert(END, dt_end_str)

        dt_Past = today - self.dt_start
        hours, remainder = divmod(dt_Past.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        dt_Past_str = str(hours) + "." + str(minutes)
        self.Text_Past.insert(END, dt_Past_str)
        dt_Left = dt_end - today
        hours, remainder = divmod(dt_Left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        dt_Left_str = str(hours) + "." + str(minutes)
        self.Text_Left.insert(END, dt_Left_str)
        self.root.after(20000, self.PetersCB, blaha)

    def __init__(self):
        self.root = Tk()
        self.root.title("Time Walker")
        FrameUpper = ttk.Frame(self.root, padding=(3, 3, 12, 12), borderwidth=3)
        FrameUpper.grid           (column=0, row=0, sticky=(N, W, E, S))
        FrameUpper.columnconfigure(0, weight=1)
        FrameUpper.rowconfigure   (0, weight=1)
        FrameUpper['relief'] = 'sunken'

        FrameLower = ttk.Frame(self.root, padding=(3, 3, 12, 12), relief = 'sunken')
        FrameLower.grid           (column=0, row=1, sticky=(N, W, E, S))
        FrameLower.columnconfigure(0, weight=1)
        FrameLower.rowconfigure   (0, weight=1)
        #FrameLower['relief'] = 'sunken'
        #FrameLower.config(relief = 'sunken')

        ttk.Label(FrameUpper, text="Start:").   grid(column=0, row=0)
        self.Start_h = StringVar()
        Start_m = StringVar()
        WT_Start_entry = ttk.Entry(FrameUpper, width=7, textvariable=self.Start_h)
        WT_Start_entry.grid(                           column=1, row=0, sticky=(W, E))
        WT_Start_entry.insert(END, "7.0")

        ttk.Label(FrameUpper, text="Arbetstid:").   grid(column=0, row=1)
        self.WorkTime_h = StringVar()
        WorkTime_m = StringVar()
        WT_entry = ttk.Entry(FrameUpper, width=7, textvariable=self.WorkTime_h)
        WT_entry.grid(                                 column=1, row=1, sticky=(W, E))
        WT_entry.insert(END, "8.0")

        ttk.Label(FrameUpper, text="Lunch etc:").   grid(column=0, row=2)
        self.NonWorkTime_h = StringVar()
        NonWorkTime_m = StringVar()
        NWT_entry = ttk.Entry(FrameUpper, width=7, textvariable=self.NonWorkTime_h)
        NWT_entry.grid(                                column=1, row=2, sticky=(W, E))
        NWT_entry.insert(END, "0.30")

        ttk.Label(FrameLower, text="Start").   grid(column=0, row=0)
        ttk.Label(FrameLower, text="Slut").    grid(column=1, row=0)

        self.Text_Start = ttk.tkinter.Text(FrameLower, height=1, width=5)
        self.Text_Start.grid(column=0, row=1)
        self.Text_Start.insert(END, "Hej")
        self.Text_Slut  = ttk.tkinter.Text(FrameLower, height=1, width=5)
        self.Text_Slut.grid(column=1, row=1)
        self.Text_Slut.insert(END, "Hopp")

        ttk.Label(FrameLower, text="Passerat").grid(column=0, row=2)
        ttk.Label(FrameLower, text="Kvar").    grid(column=1, row=2)

        self.Text_Past = ttk.tkinter.Text(FrameLower, height=1, width=5)
        self.Text_Past.grid(column=0, row=3)
        self.Text_Past.insert(END, "Hej")
        self.Text_Left  = ttk.tkinter.Text(FrameLower, height=1, width=5)
        self.Text_Left.grid(column=1, row=3)
        self.Text_Left.insert(END, "Hopp")

        for child in FrameUpper.winfo_children(): child.grid_configure(padx=5, pady=5)
        self.root.bind('<Return>', self.PetersCB, self)
        blaha = 7
        self.PetersCB(blaha)
        self.root.mainloop()
#_______________________________________________________________________________
def main():
    GuiApp2()
    exit(-1)
#_______________________________________________________________________________
if __name__ == '__main__':
    main()
