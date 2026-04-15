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
        self.root.geometry("1250x870")

        self.label_leaderboard = tk.Label(self.root, text="Participants", font=("Arial", 16))
        self.label_leaderboard.pack(pady=10)
    
        # Navigation bar
        self.nav_bar = tk.Frame(self.root)
        self.nav_bar.pack(side="top", pady=20)
        #buttons themself in nav bar
        self.btn_event = tk.Button(self.nav_bar, text="Event", command=self.show_event_screen, width=15, font=("Arial", 20))
        self.btn_participants = tk.Button(self.nav_bar, text="Participants", command=self.show_participants_screen, width=15, font=("Arial", 20))
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

        self.label_leaderboard = tk.Label(self.team_rank_frame, text="Rank", font=("Arial", 10, "bold"))
        self.label_leaderboard.grid(row=0, column=0)
        self.label_team_name = tk.Label(self.team_rank_frame, text="Team Name", font=("Arial", 10, "bold"))
        self.label_team_name.grid(row=0, column=1, padx=10)
        self.label_team_score = tk.Label(self.team_rank_frame, text="Score", font=("Arial", 10, "bold"))
        self.label_team_score.grid(row=0, column=2)

        #Indiv ranking
        self.indiv_rank_frame = tk.LabelFrame(self.tables_container, text=" Individual Standings ", font=("Arial", 13, "bold"), padx=10, pady=10)
        self.indiv_rank_frame.pack(side="left", fill="both", expand=True, padx=10)

        self.label_indiv_rank = tk.Label(self.indiv_rank_frame, text="Rank", font=("Arial", 10, "bold"))
        self.label_indiv_rank.grid(row=0, column=0)
        self.label_indiv_name = tk.Label(self.indiv_rank_frame, text="Name", font=("Arial", 10, "bold"))
        self.label_indiv_name.grid(row=0, column=1,padx=10)
        self.label_indiv_score = tk.Label(self.indiv_rank_frame, text="Score", font=("Arial", 10, "bold"))
        self.label_indiv_score.grid(row=0, column=2)

        self.show_events_screen()

    #upcoming events
    def show_events_screen(self):
        
        self.title_label = tk.Label(self.main, text="UPCOMING EVENTS", font=("Arial", 17, "bold"))
        self.title_label.pack(pady=20)

        self.events_frame = tk.Frame(self.main)
        self.events_frame.pack(fill="x", padx=50)

        self.event1_box = tk.LabelFrame(self.events_frame, text=" Event #1 ", padx=15, pady=15)
        self.event1_box.pack(fill="x", pady=10)

        tk.Label(self.event1_box, text="Event Name:").grid(row=0, column=0, sticky="w")
        self.event1_name = tk.Entry(self.event1_box, width=45)
        self.event1_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.event1_box, text="Date Time:").grid(row=1, column=0, sticky="w")
        self.event1_date = tk.Entry(self.event1_box, width=45)
        self.event1_date.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.event1_box, text="Type:").grid(row=2, column=0, sticky="w")
        ttk.Combobox(self.event1_box, values=["Team", "Individual"]).grid(row=2, column=1)

        self.event2_box = tk.LabelFrame(self.events_frame, text=" Event #2 ", padx=15, pady=15)
        self.event2_box.pack(fill="x", pady=10)

        tk.Label(self.event2_box, text="Event Name:").grid(row=0, column=0, sticky="w")
        self.event2_name = tk.Entry(self.event2_box, width=45)
        self.event2_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.event2_box, text="Date Time:").grid(row=1, column=0, sticky="w")
        self.event2_date = tk.Entry(self.event2_box, width=45)
        self.event2_date.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.event2_box, text="Type:").grid(row=2, column=0, sticky="w")
        ttk.Combobox(self.event2_box, values=["Team", "Individual"]).grid(row=2, column=1)


    def show_event_screen(self):
        #destroy previous frame and make new one
        self.main.destroy()
        self.main = tk.Frame(self.root, bg="#f0f0f0")
        self.main.pack(fill="both", expand=True, padx=20, pady=20)

        #using canvas for scroling
        canvas = tk.Canvas(self.main)
        scrollbar = tk.Scrollbar(self.main, orient="vertical", command=canvas.yview)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.scroll_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        self.scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.configure(yscrollcommand=scrollbar.set)

        btn_frame = tk.Frame(self.main)
        btn_frame.pack(fill="x", side="bottom")

        tk.Button(btn_frame, text="Add Event", command=self.add_event_box).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delte").pack(side="right", padx=5)
        tk.Button(btn_frame, text="Update").pack(side="right", padx=5)


    def show_participants_screen(self):
        #destroy previous frame and make new one
        self.main.destroy()
        self.main = tk.Frame(self.root)
        self.main.pack(fill="both", expand=True)

        tk.Label(self.main, text="PAticipants", font=("Arial", 18, "bold")).pack(pady=10)

        wrap = tk.Frame(self.main)
        wrap.pack(fill="both", expand=True)

        #table for and indiv particip
        indiv = tk.LabelFrame(wrap, text="Individuals")
        indiv.pack(side="left", fill="both", expand=True, padx=5)

        self.indiv_tree = ttk.Treeview(indiv, columns=("№", "name", "points"), show="headings")
        self.indiv_tree.heading("№", text="№")
        self.indiv_tree.heading("name", text="Name")
        self.indiv_tree.heading("points", text="Points")
        self.indiv_tree.pack(fill="both", expand=True)

        entry_i = tk.Frame(indiv)
        entry_i.pack(pady=5)

        self.indiv_name_entry = tk.Entry(entry_i)
        self.indiv_name_entry.pack(side="left", padx=5)

        self.indiv_points = tk.Entry(entry_i, width=5)
        self.indiv_points.pack(side="left")

        self.indiv_add_points = tk.Entry(entry_i, width=5)
        self.indiv_add_points.pack(side="left")
        #buttons for add points andd add particip
        tk.Button(entry_i, text="Add", command=self.add_individual).pack(side="left")
        tk.Button(entry_i, text="+", command=self.add_points_indiv).pack(side="left")
        #delete or update indiv particip info buttons
        tk.Button(indiv, text="Update", command=self.update_indiv).pack(side="left", padx=5)
        tk.Button(indiv, text="Delete", command=self.delete_indiv).pack(side="left", padx=5)

        #table for and teams
        team = tk.LabelFrame(wrap, text="Teams")
        team.pack(side="left", fill="both", expand=True, padx=5)

        self.team_tree = ttk.Treeview(team, columns=("№", "team", "p1", "p2", "p3", "p4", "p5", "points"), show="headings")
        self.team_tree.heading("№", text="№")
        self.team_tree.heading("team", text="Team")
        self.team_tree.heading("p1", text="P1")
        self.team_tree.heading("p2", text="P2")
        self.team_tree.heading("p3", text="P3")
        self.team_tree.heading("p4", text="P4")
        self.team_tree.heading("p5", text="P5")
        self.team_tree.heading("points", text="Points")
        self.team_tree.pack(fill="both", expand=True)

        entry_t = tk.Frame(team)
        entry_t.pack(pady=5)

        self.team_name_entry = tk.Entry(entry_t, width=8)
        self.team_name_entry.pack(side="left")
        #boxes for team participants in adding
        self.p1 = tk.Entry(entry_t, width=6); self.p1.pack(side="left")
        self.p2 = tk.Entry(entry_t, width=6); self.p2.pack(side="left")
        self.p3 = tk.Entry(entry_t, width=6); self.p3.pack(side="left")
        self.p4 = tk.Entry(entry_t, width=6); self.p4.pack(side="left")
        self.p5 = tk.Entry(entry_t, width=6); self.p5.pack(side="left")

        self.team_points = tk.Entry(entry_t, width=5)
        self.team_points.pack(side="left")

        self.team_add_points = tk.Entry(entry_t, width=5)
        self.team_add_points.pack(side="left")
#add points or add team button
        tk.Button(entry_t, text="Add", command=self.add_team).pack(side="left", padx=5)
        tk.Button(entry_t, text="+", command=self.add_points_team).pack(side="left")
#update or delete team buttons
        tk.Button(team, text="Update", command=self.update_team).pack(side="left", padx=5)
        tk.Button(team, text="Delete", command=self.delete_team).pack(side="left", padx=5)

#Add individuals
    def add_individual(self):
        name = self.indiv_name_entry.get()
        points = self.indiv_points.get() or 0
        if name:
            count = len(self.indiv_tree.get_children()) + 1
            self.indiv_tree.insert("", "end", values=(count, name, points))

#adding team with team participants and points for team
    def add_team(self):
        team = self.team_name_entry.get()
        if team:
            count = len(self.team_tree.get_children()) + 1
            self.team_tree.insert("", "end", values=(count, team, self.p1.get(), self.p2.get(), self.p3.get(), self.p4.get(), self.p5.get(), self.team_points.get() or 0))
    #adding points for indiv particip
    def add_points_indiv(self):
        sel = self.indiv_tree.selection()
        if sel:
            add = int(self.indiv_add_points.get() or 0)
            item = self.indiv_tree.item(sel)
            vals = list(item["values"])
            vals[2] = int(vals[2]) + add
            self.indiv_tree.item(sel, values=vals)
    #adding points for teams
    def add_points_team(self):
        sel = self.team_tree.selection()
        if sel:
            add = int(self.team_add_points.get() or 0)
            item = self.team_tree.item(sel)
            vals = list(item["values"])
            vals[7] = int(vals[7]) + add
            self.team_tree.item(sel, values=vals)

    #updating indiv particip
    def update_indiv(self):
        sel = self.indiv_tree.selection()
        if sel:
            name = self.indiv_name_entry.get()
            points = self.indiv_points.get()
            item = self.indiv_tree.item(sel)
            vals = list(item["values"])
            if name:
                vals[1] = name
            if points:
                vals[2] = points
            self.indiv_tree.item(sel, values=vals)
    #Updatin teams info
    def update_team(self):
        sel = self.team_tree.selection()
        if sel:
            item = self.team_tree.item(sel)
            vals = list(item["values"])

            if self.team_name_entry.get():
                vals[1] = self.team_name_entry.get()
            vals[2] = self.p1.get() or vals[2]
            vals[3] = self.p2.get() or vals[3]
            vals[4] = self.p3.get() or vals[4]
            vals[5] = self.p4.get() or vals[5]
            vals[6] = self.p5.get() or vals[6]

            if self.team_points.get():
                vals[7] = self.team_points.get()

            self.team_tree.item(sel, values=vals)
    #deleating indiv particip
    def delete_indiv(self):
        for i in self.indiv_tree.selection():
            self.indiv_tree.delete(i)
    #deleating team
    def delete_team(self):
        for i in self.team_tree.selection():
            self.team_tree.delete(i)

    #Adding event boxes for new events
    def add_event_box(self):
        box = tk.LabelFrame(self.scroll_frame, text="Event")
        box.pack(fill="x", padx=10, pady=5)

        tk.Label(box, text="Date:").grid(row=0, column=0)
        tk.Entry(box).grid(row=0, column=1)

        tk.Label(box, text="Type:").grid(row=0, column=2)
        ttk.Combobox(box, values=["Team", "Individual"], width=10).grid(row=0, column=3)

        tk.Label(box, text="Description:").grid(row=1, column=0)
        tk.Entry(box).grid(row=1, column=1, columnspan=3)

        tk.Label(box, text="Participants:").grid(row=2, column=0)
        tk.Entry(box).grid(row=2, column=1, columnspan=3)


def confirm_action(message):
    return messagebox.askyesno("Confirmation", message)


app = TournamentApp(root)
app.main_loop()