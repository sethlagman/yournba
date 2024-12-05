from datetime import date as d
import customtkinter as ctk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules.nba_schedule import *
from modules.nba_statistics import *

class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(column=0, row=0)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2), weight=1)
        self.grid_columnconfigure((0, 1), weight=0)

        title = ctk.CTkLabel(self, text="YourNBA", font=('', 50, 'bold'))
        title.grid(column=1, row=0, pady=(20, 15))

        sidebar = SideBarFrame(self)
        entry = EntryFrame(self)
        output = OutputFrame(self)


class SideBarFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=250)
        self.grid(column=0, row=0, rowspan=3, sticky='nsew', padx=(10, 0), pady=(10, 10))
        self.grid_propagate(0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(self, text='Menu', font=('', 30, 'bold'))
        title.grid(column=0, row=0, sticky='n', pady=(10, 15))


class EntryFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        self.grid(column=1, row=1, sticky='new')
        self.grid_propagate(0)

        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)

        search = ctk.CTkEntry(self, placeholder_text='Player, game id, schedule date, and etc.', height=30)
        search.grid(row=1, column=0, sticky='ew', padx=(20, 5))

        search_btn = ctk.CTkButton(self, text='Search', height=30)
        search_btn.grid(row=1,column=1, sticky='ew', padx=(5, 20))


class OutputFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, height=650, width=545)
        self.grid(column=1, row=2, sticky='ew', padx=(10, 10), pady=(10, 10))
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
        self.geometry(f'{850}x{650}')
        self.iconbitmap(r'images\nbalogo.ico')
        self.resizable(False, False)
        self.title('')
        self.protocol('WM_DELETE_WINDOW', self.exit_app)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        mainframe = MainFrame(self)

    def exit_app(self):
        confirm = messagebox.askyesno('', 'Are you sure you want to close the application?')
        if confirm:
            self.quit()


app = App()
app.mainloop()