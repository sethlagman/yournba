from datetime import date as d
import customtkinter as ctk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules.nba_schedule import *
from modules.nba_statistics import *
from modules.filehandler import FileHandler

class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(column=0, row=0)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1), weight=0)

        title = ctk.CTkLabel(self, text='YourNBA', font=('', 50, 'bold'))
        title.grid(column=1, row=0, pady=(20, 15))
        
        entry = EntryFrame(self)
        output = OutputFrame(self)
        pagination = PaginationFrame(self, output_frame=output, current_page=output.current_page)
        sidebar = SideBarFrame(self, output_frame=output, pagination_frame=pagination)


class PaginationFrame(ctk.CTkFrame):
    def __init__(self, master, output_frame, current_page=0):
        super().__init__(master, fg_color='transparent')
        self.grid(column=1, row=3, sticky='ew', padx=(10, 0))
        self.grid_propagate(0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.output_frame = output_frame
        self.current_page = current_page

        self.next_btn = ctk.CTkButton(self, text='Next', height=30, width=210, command=self.next_page)
        self.next_btn.grid(row=0, column=1, pady=(0, 5))

        self.previous_btn = ctk.CTkButton(self, text='Previous', height=30, width=210, command=self.previous_page)
        self.previous_btn.grid(row=0, column=0, pady=(0, 5))

        self.update_nextbtn_state(self.output_frame.output)
        self.update_prevbtn_state()

    def get_length(self, data):
        if data == 'schedule':
            return len(NbaSchedule().fetch_shedule())
        
        if data == 'statistics':
            return len(NbaStatistics().statistics)
        
        if data == 'game_today':
            return 0

    def update_nextbtn_state(self, data):
        if self.output_frame.end_index <= self.get_length(data):
            self.next_btn.configure(state='normal')

        elif self.output_frame.end_index >= self.get_length(data):
            self.next_btn.configure(state='disabled')

    def update_prevbtn_state(self):
        if self.output_frame.current_page > 0:
            self.previous_btn.configure(state='normal')

        elif self.output_frame.current_page <= 0:
            self.previous_btn.configure(state='disabled')

    def next_page(self):
        self.output_frame.update_page(self.output_frame.current_page + 1)
        self.update_nextbtn_state(self.output_frame.output)
        self.update_prevbtn_state()

    def previous_page(self):
        self.output_frame.update_page(self.output_frame.current_page - 1)
        self.update_prevbtn_state()
        self.update_nextbtn_state(self.output_frame.output)


class SideBarFrame(ctk.CTkFrame):
    def __init__(self, master, output_frame, pagination_frame):
        super().__init__(master, width=250)
        self.grid(column=0, row=0, rowspan=4, sticky='nsew', padx=(10, 0), pady=(10, 10))
        self.grid_propagate(0)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.output_frame = output_frame
        self.pagination_frame = pagination_frame

        title = ctk.CTkLabel(self, text='Menu', font=('', 30, 'bold'))
        title.grid(column=0, row=0, sticky='n', pady=(30, 15))

        schedules_btn = ctk.CTkButton(self, text='Schedule', height=35, width=150, command=self.update_output_to_schedule)
        schedules_btn.grid(column=0, row=1, pady=(30, 30))

        statistics_btn = ctk.CTkButton(self, text='Statistics', height=35, width=150, command=self.update_output_to_statistics)
        statistics_btn.grid(column=0, row=2, pady=(20, 30))

    def update_output_to_schedule(self):
        self.output_frame.update_output('schedule')
        self.pagination_frame.update_nextbtn_state(self.output_frame.output)
        self.pagination_frame.update_prevbtn_state()

    def update_output_to_statistics(self):
        self.output_frame.update_output('statistics')
        self.pagination_frame.update_nextbtn_state(self.output_frame.output)
        self.pagination_frame.update_prevbtn_state()


class EntryFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='transparent')
        self.grid(column=1, row=1, sticky='new')
        self.grid_propagate(0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.grid_columnconfigure(2, weight=1)

        self.optionmenu = ctk.CTkOptionMenu(self, values=['Date', 'Player', 'Game Id'], height=31, command=self.optionmenu_callback)
        self.optionmenu.grid(row=1, column=0)

        self.search = ctk.CTkEntry(self, placeholder_text=f'Search for {self.optionmenu.get()}', height=30)
        self.search.grid(row=1, column=1, sticky='ew', padx=(0, 10))

        search_btn = ctk.CTkButton(self, text='Search', height=30, width=50, command=self.get_entry)
        search_btn.grid(row=1,column=2, sticky='ew', padx=(5, 20))
    
    def get_entry(self):
        return {'entry': self.search.get(), 'option': self.optionmenu.get()}

    def optionmenu_callback(self, choice):
        self.search.configure(placeholder_text=f'Search for {choice}')


class OutputFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, items_per_page=10, current_page=0):
        super().__init__(master, height=650, width=545)
        self.grid(column=1, row=2, sticky='ew', padx=(10, 10), pady=(10, 10))
        self.grid_columnconfigure(0, weight=1)
        
        self.output = 'game_today'
        self.items_per_page = items_per_page
        self.current_page = current_page
        self.start_index = self.current_page * self.items_per_page
        self.end_index = self.start_index + self.items_per_page

        self.load_page_data()

    def update_output(self, output):
        self.output = output
        self.clear_content()
        self.load_page_data()

    def load_page_data(self):
        if self.output == 'game_today':
            current_date = d.today().strftime('%m/%d/%Y')
            schedules = NbaSchedule().fetch_date_schedule(current_date)
            for schedule in schedules:

                for date, games in schedule.items():
                    date_label = ctk.CTkLabel(self, text=date, font=('', 18, 'bold', 'underline'))
                    date_label.grid(sticky='w', padx=(20, 0), pady=(10, 10))

                    for game in games:
                        if game['Home'].strip() and game['Away'].strip():
                            matchup = f'{game['Home']} vs {game['Away']} | {game['gameTime']}'
                            matchup_label = ctk.CTkLabel(self, text=matchup, font=('', 17))
                            matchup_label.grid(sticky='w', padx=(20, 0))
                            
                        else:
                            matchup_label = ctk.CTkLabel(self, text='No matchup for this date', font=('', 17))
                            matchup_label.grid(sticky='w', padx=(20, 0))
                            break

        elif self.output == 'schedule':
            schedules = NbaSchedule().fetch_shedule()[self.start_index:self.end_index]
            for schedule in schedules:

                for date, games in schedule.items():
                    date_label = ctk.CTkLabel(self, text=date, font=('', 18, 'bold', 'underline'))
                    date_label.grid(sticky='w', padx=(20, 0), pady=(10, 10))

                    for game in games:
                        if game['Home'].strip() and game['Away'].strip():
                            matchup = f'{game['Home']} vs {game['Away']} | {game['gameTime']}'
                            matchup_label = ctk.CTkLabel(self, text=matchup, font=('', 17))
                            matchup_label.grid(sticky='w', padx=(20, 0))

                        else:
                            matchup_label = ctk.CTkLabel(self, text='No matchup for this date', font=('', 17))
                            matchup_label.grid(sticky='w', padx=(20, 0))
                            break

        elif self.output == 'statistics':
            statistics = NbaStatistics().statistics[self.start_index:self.end_index]
            for statistic in statistics:

                player, team, position = statistic['name'],  statistic['team'], statistic['position']
                pointspergame, assistspergame = statistic['ppg'], statistic['apg']
                stealspergame, blockspergame, turnoverspergame = statistic['spg'], statistic['bpg'], statistic['tpg']

                player_label = ctk.CTkLabel(self, text=player, font=('', 15, 'bold'))
                team_label = ctk.CTkLabel(self, text=f'   Team: {team}')
                position_label = ctk.CTkLabel(self, text=f'   Position: {position}')
                ppg_label = ctk.CTkLabel(self, text=f'   Points per game: {pointspergame}')
                apg_label = ctk.CTkLabel(self, text=f'   Assists per game: {assistspergame}')
                spg_label = ctk.CTkLabel(self, text=f'   Steals per game: {stealspergame}')
                bpg_label = ctk.CTkLabel(self, text=f'   Blocks per game: {blockspergame}')
                tpg_label = ctk.CTkLabel(self, text=f'   Turnovers per game: {turnoverspergame}')

                player_label.grid(sticky='w')
                team_label.grid(sticky='w')
                position_label.grid(sticky='w')
                ppg_label.grid(sticky='w')
                apg_label.grid(sticky='w')
                spg_label.grid(sticky='w')
                bpg_label.grid(sticky='w')
                tpg_label.grid(sticky='w')

    def update_page(self, current_page):
        self.current_page = current_page
        self.start_index = self.current_page * self.items_per_page
        self.end_index = self.start_index + self.items_per_page
        self.clear_content()
        self.load_page_data()

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{850}x{700}')
        self.iconbitmap(r'images\nbalogo.ico')
        self.resizable(False, False)
        self.title('')
        #self.protocol('WM_DELETE_WINDOW', self.exit_app)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        mainframe = MainFrame(self)

    def exit_app(self):
        confirm = messagebox.askyesno('', 'Are you sure you want to close the application?')
        if confirm:
            self.quit()


app = App()
app.mainloop()