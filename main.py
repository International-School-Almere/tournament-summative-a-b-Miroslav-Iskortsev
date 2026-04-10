from logging import root
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

root = tk.Tk()
# Load and save data functions
def load_data():
    file = "data.json"
    if not os.path.exists(file):
        return {"teams": [], "individuals": [], "events": []}
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f) 
    
def save_data(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
# GUI functions

class TournamentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tournament Management System")
        self.root.geometry("800x870")

        self.label_leaderboard = tk.Label(self.root, text="Participants", font=("Arial", 16))
        self.label_leaderboard.pack(pady=10)
    
        # Navigation bar
        self.nav_bar = tk.Frame(self.root)
        self.nav_bar.pack(side="top", pady=20)
        #buttons themself in nav bar
        self.btn_event = tk.Button(self.nav_bar, text="Event", width=15, font=("Arial", 20))
        self.btn_participants = tk.Button(self.nav_bar, text="Participants", width=15, font=("Arial", 20))
        self.btn_overview = tk.Button(self.nav_bar, text="Overview",command=self.show_overview_screen, width=15, font=("Arial", 20))
        #packaging buttons in nav bar
        self.btn_event.pack(side="left", padx=10)
        self.btn_participants.pack(side="left", padx=10)
        self.btn_overview.pack(side="left", padx=10)
        
        self.main=tk.Frame(self.root)
        self.main.pack(fill="both", expand=True)
        self.main.config(bg="#f0f0f0", padx=20, pady=20)

    def main_loop(self):    
        self.root.mainloop()



    def show_overview_screen(self):
        self.main.destroy()
        self.main = tk.Frame(self.root)
        self.main.pack(fill="both", expand=True)
        #title
        self.title_label = tk.Label(self.main, text="Top Rankings", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=20)

        #Box for tables
        self.tables_container = tk.Frame(self.main)
        self.tables_container.pack(fill="both", expand=True)

        #team ranking
        self.team_rank_frame = tk.LabelFrame(self.tables_container, text=" Team Standings ", font=("Arial", 13, "bold"), padx=10, pady=10)
        self.team_rank_frame.pack(side="left", fill="both", expand=True, padx=10)

        #Head for teams
        self.label_leaderboard = tk.Label(self.team_rank_frame, text="Rank", font=("Arial", 10, "bold"))
        self.label_leaderboard.grid(row=0, column=0)
        self.label_team_name = tk.Label(self.team_rank_frame, text="Team Name", font=("Arial", 10, "bold"))
        self.label_team_name.grid(row=0, column=1, padx=10)
        self.label_team_score = tk.Label(self.team_rank_frame, text="Score", font=("Arial", 10, "bold"))
        self.label_team_score.grid(row=0, column=2)

        #Indiv ranking
        self.indiv_rank_frame = tk.LabelFrame(self.tables_container, text=" Individual Standings ", font=("Arial", 13, "bold"), padx=10, pady=10)
        self.indiv_rank_frame.pack(side="left", fill="both", expand=True, padx=10)

        # Head for indiv
        self.label_indiv_rank = tk.Label(self.indiv_rank_frame, text="Rank", font=("Arial", 10, "bold"))
        self.label_indiv_rank.grid(row=0, column=0)
        self.label_indiv_name = tk.Label(self.indiv_rank_frame, text="Name", font=("Arial", 10, "bold"))
        self.label_indiv_name.grid(row=0, column=1,padx=10)
        self.label_indiv_score = tk.Label(self.indiv_rank_frame, text="Score", font=("Arial", 10, "bold"))
        self.label_indiv_score.grid(row=0, column=2)
        show_events_screen(self)

        #UPCOMING EVENTS SCREEN
def show_events_screen(self):
        
        #title
        self.title_label = tk.Label(self.main, text="UPCOMING EVENTS", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=20)

        #box for events
        self.events_frame = tk.Frame(self.main)
        self.events_frame.pack(fill="x", padx=50)

        #ev1
        self.event1_box = tk.LabelFrame(self.events_frame, text=" Event #1 ", font=("Arial", 12, "bold"), padx=15, pady=15)
        self.event1_box.pack(fill="x", pady=10)

        self.label_event1_name = tk.Label(self.event1_box, text="Event Name:").grid(row=0, column=0, sticky="w")
        self.event1_name = tk.Entry(self.event1_box, width=45)
        self.event1_name.grid(row=0, column=1, padx=10, pady=5)
        

        self.label_event1_date = tk.Label(self.event1_box, text="Datr Time:").grid(row=1, column=0, sticky="w")
        self.event1_date = tk.Entry(self.event1_box, width=45)
        self.event1_date.grid(row=1, column=1, padx=10, pady=5)

        #ev2
        self.event2_box = tk.LabelFrame(self.events_frame, text=" Event #2 ", font=("Arial", 12, "bold"), padx=15, pady=15)
        self.event2_box.pack(fill="x", pady=10)

        self.label_event2_name = tk.Label(self.event2_box, text="Event Name:").grid(row=0, column=0, sticky="w")
        self.event2_name = tk.Entry(self.event2_box, width=45)
        self.event2_name.grid(row=0, column=1, padx=10, pady=5)
        
        self.label_event2_date = tk.Label(self.event2_box, text="Date Time:").grid(row=1, column=0, sticky="w")
        self.event2_date = tk.Entry(self.event2_box, width=45)
        self.event2_date.grid(row=1, column=1, padx=10, pady=5)


# def show_participants_screen():


# def show_events_screen():




# def make_participants_table():


# def update_participants_data():


# def delete_entry(item_id):


# def make_events_list():


# def add_new_event():


# def save_event_changes(event_id):


# def calculate_team_scores():


# def get_sorted_leaderboard():


def confirm_action(message):
    return messagebox.askyesno("Confirmation", message)


app = TournamentApp(root)
#app.show_overview_screen()
app.main_loop()
