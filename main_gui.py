from datetime import date
import customtkinter as ctk

from modules import nba_schedule, nba_statistics

class OutputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=500, width=300)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x650")
        self.title('')
        self.iconbitmap(r'images\nbalogo.ico')
        self.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(self, text="YourNBA", font=('', 50, 'bold'))
        title.grid(pady=(20, 15), columnspan=2)

        search = ctk.CTkEntry(self, placeholder_text='Player, game id, schedule date, and etc.', height=30)
        search.grid(row=1, column=0, sticky='ew', padx=(20, 0))

        search_btn = ctk.CTkButton(self, text='Search', height=30)
        search_btn.grid(row=1, column=1, sticky='e', padx=(10, 20))
        
        self.output_frame = OutputFrame(self)
        self.output_frame.grid(row=2, pady=15, columnspan=2, sticky='ew', padx=20)
        
        
app = App()
app.mainloop()