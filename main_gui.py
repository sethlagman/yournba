from datetime import date as d
import customtkinter as ctk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules.nba_schedule import *
from modules.nba_statistics import *

class EntryFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=50, width=300, fg_color='transparent')
        self.grid_propagate(0)

        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)

        search = ctk.CTkEntry(self, placeholder_text='Player, game id, schedule date, and etc.', height=30)
        search.grid(row=1, column=0, sticky='ew', padx=(20, 5))

        search_btn = ctk.CTkButton(self, text='Search', height=30)
        search_btn.grid(row=1,column=1, sticky='ew', padx=(5, 20))


class OutputFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, height=500, width=300)
        
        self.grid_columnconfigure(0, weight=1)

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
        self.title('')
        self.geometry("500x650")
        self.iconbitmap(r'images\nbalogo.ico')
        self.protocol('WM_DELETE_WINDOW', self.exit_app)
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(self, text="YourNBA", font=('', 50, 'bold'))
        title.grid(row=0, pady=(20, 15))

        entry_frame = EntryFrame(self)
        entry_frame.grid(row=1, sticky='new')

        output_frame = OutputFrame(self)
        output_frame.grid(row=2, sticky='ew', padx=(10, 10), pady=(0, 10))

    def exit_app(self):
        confirm = messagebox.askyesno('', 'Are you sure you want to close the application?')
        if confirm:
            self.quit()


app = App()
app.mainloop()