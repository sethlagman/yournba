from datetime import date as d
import customtkinter as ctk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules.nba_schedule import *
from modules.nba_statistics import *

class OutputFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, height=500, width=300)
        self.toplevel_window = None
        
        current_date = f'{d.today().month}/0{d.today().day}/{d.today().year}'
        schedules = NbaSchedule().fetch_shedule()

        for schedule in schedules[150:200]:
            for date, games in schedule.items():
                date_label = ctk.CTkLabel(self, text=date)
                date_label.grid()
                for game in games:
                    matchup = f'{game['Home']} vs {game['Away']}'
                    matchup_label = ctk.CTkLabel(self, text=matchup)
                    matchup_label.grid()
            
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.toplevel_window = None
        #self.protocol("WM_DELETE_WINDOW", self.exit_app)

        self.geometry("500x650")
        self.title('')
        self.iconbitmap(r'images\nbalogo.ico')
        self.grid_columnconfigure(0, weight=20)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        title = ctk.CTkLabel(self, text="YourNBA", font=('', 50, 'bold'))
        title.grid(pady=(20, 15), columnspan=2)

        search = ctk.CTkEntry(self, placeholder_text='Player, game id, schedule date, and etc.', height=30)
        search.grid(row=1, column=0, sticky='ew', padx=(20, 0))

        search_btn = ctk.CTkButton(self, text='Search', height=30)
        search_btn.grid(row=1, column=1, sticky='e', padx=(10, 20))
        
        self.output_frame = OutputFrame(self)
        self.output_frame.grid(row=2, columnspan=2, sticky='ew', pady=15, padx=15)

    def exit_app(self):
        confirm = messagebox.askyesno('', 'Are you sure you want to close the application?')
        if confirm:
            self.quit()
        

app = App()
app.mainloop()