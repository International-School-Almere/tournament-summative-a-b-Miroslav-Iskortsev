import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

def load_data():
    file = "data.json"
    if not os.path.exists(file):
        return {"teams": [], "individuals": [], "events": []}
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f) 
    
def save_data(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

root = tk.Tk()
root.title("Tournament Management System")
root.geometry("800x870")


# def show_participants_screen():


# def show_events_screen():


# def show_leaderboard_screen():


# def make_participants_table():


# def update_participants_data():


# def delete_entry(item_id):


# def make_events_list():


# def add_new_event():


# def save_event_changes(event_id):


# def calculate_team_scores():


# def get_sorted_leaderboard():


# def confirm_action(message):

root.mainloop()