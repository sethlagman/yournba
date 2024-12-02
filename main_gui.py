import customtkinter as ctk

import nba_schedule, nba_statistics

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x650")
        self.title('Your NBA')
        
        title_label = ctk.CTkLabel(self, text="Your NBA", font=ctk.CTkFont(size=30, weight="bold"))
        title_label.pack(padx=10, pady=(20, 20))

app = App()
app.mainloop()