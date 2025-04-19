from pyswip import Prolog
import tkinter as tk
from tkinter import ttk, messagebox

prolog_kb = """
study_spot(salesforce_park,    close,            low,    none,               [outdoor_seating],              closes_8_10pm,     poor,     low,      none).
study_spot(capital_one_cafe,    close,            medium, full_menu,         [private_study_rooms,shared_long_tables], closes_before_8pm, good, moderate, many).
study_spot(sf_public_library,   close,            low,    snacks_only,       [quiet_individual,shared_long_tables,comfortable_lounge], closes_8_10pm, good, silent, every_seat).
study_spot(philz_coffee,        close,            medium, full_menu,         [comfortable_lounge,outdoor_seating,shared_long_tables,regular_tables], closes_before_8pm, good, moderate, few).
study_spot(haus_coffee,         far,              medium, full_menu,         [shared_long_tables,comfortable_lounge,outdoor_seating,regular_tables], closes_before_5pm, good, low, many).
study_spot(southeast_community, far,              low,    coffee_only,       [shared_long_tables,outdoor_seating], closes_before_5pm, good, moderate, few).
study_spot(delah_coffee,        moderate_commute, high,   full_menu,         [comfortable_lounge,regular_tables], closes_before_8pm, good, moderate, many).
study_spot(sanas_coffee,        moderate_commute, high,   full_menu,         [comfortable_lounge,regular_long_tables,shared_long_tables], open_until_midnight, good, high, many).
study_spot(ikea,                very_close,       low,    full_menu,         [shared_long_tables,regular_tables], closes_before_8pm, good, moderate, few).
study_spot(spro_mission,        far,              high,   full_menu,         [outdoor_seating,regular_tables], closes_before_5pm, good, high, many).
study_spot(progressive_grounds, far,              medium, full_menu,         [shared_long_tables,outdoor_seating,comfortable_lounge,regular_tables], closes_before_8pm, good, low, few).
study_spot(ucsf_library,        far,              low,    coffee_only,       [quiet_individual,shared_long_tables,comfortable_lounge,regular_tables], closes_before_8pm, good, silent, few).
study_spot(comptons_coffee,     far,              medium, full_menu,         [shared_long_tables,comfortable_lounge,outdoor_seating], closes_before_5pm, good, moderate, few).
study_spot(black_bird,          far,              medium, full_menu,         [comfortable_lounge,outdoor_seating], closes_before_8pm, none, moderate, few).
study_spot(home_coffee_roast,   close,            medium, full_menu,         [shared_long_tables,comfortable_lounge], closes_before_5pm, good, moderate, many).
study_spot(sight_glass,         close,            medium, full_menu,         [shared_long_tables],        closes_before_5pm, none, moderate, few).
study_spot(rise_and_grind,      far,              high,   full_menu,         [shared_long_tables],        closes_before_5pm, good, moderate, few).
study_spot(matching_half,       far,              high,   full_menu,         [regular_tables,comfortable_lounge], closes_before_5pm, poor, moderate, few).
study_spot(ballast_coffee,      far,              medium, full_menu,         [shared_long_tables],        closes_before_5pm, good, moderate, many).
"""

askables = [
    ("How close should it be?",
        ["very_close (<= 5 min walk)", 
         "close (6-15 min walk)", 
         "moderate_commute (16-30 min via walk/transit)", 
         "far (> 30 min commute)"]),

    ("What cost level can you afford?",
        ["free (no charge)", 
         "low (<= $5)", 
         "medium ($5-$15)", 
         "high (>= $15)"]),

    ("What food/coffee options do you need?",
        ["none (no food or drink)", 
         "coffee_only (just drinks)", 
         "snacks_only (light bites)", 
         "full_menu (meals & drinks)"]),

    ("Which seating type do you prefer? (multi-select)",
        ["quiet_individual (e.g. library carrel)", 
         "shared_long_tables", 
         "comfortable_lounge (sofas)", 
         "outdoor_seating", 
         "regular_tables", 
         "private_study_rooms"]),

    ("Which closing time works for you?",
        ["closes_before_5pm (before 5 PM)", 
         "closes_before_8pm (before 8 PM)", 
         "closes_8_10pm (8 PM-10 PM)", 
         "open_until_midnight (until 12 AM)", 
         "24_hours (always open)"]),

    ("What WiFi quality do you need?",
        ["none (no WiFi)", 
         "poor (< 5 Mbps)",
         "good (20-50 Mbps)"]),

    ("What noise level do you prefer?",
        ["silent (library-quiet)", 
         "low (soft background)", 
         "moderate (normal cafe)", 
         "high (busy/crowded)"]),

    ("What outlet availability do you need?",
        ["none", 
         "few (scattered)", 
         "many (multiple nearby)", 
         "every_seat (built-in)"]),
]


def consult_kb(prolog, kb_str):
    for line in kb_str.strip().split('\n'):
        if line:
            prolog.assertz(line.strip('.'))
    # add member/2 and valid_spot/9
    prolog.assertz("member(X,[X|_])")
    prolog.assertz("member(X,[_|T]) :- member(X,T)")
    prolog.assertz("valid_spot(Name, Loc, Cost, Food, Seat, Close, Wifi, Noise, Out) :- study_spot(Name, Loc, Cost, Food, Seats, Close, Wifi, Noise, Out), member(Seat, Seats)")


def run_expert_system_gui():
    prolog = Prolog()
    consult_kb(prolog, prolog_kb)

    root = tk.Tk()
    root.title("Study Spot Recommender")
    root.geometry("520x400")

    answers = []
    current = [0]

    instructions = tk.Label(root, text="Answer each question to get a study spot recommendation.\nUse number keys or mouse to select, Enter to continue.", font=("Arial", 11), fg="gray")
    instructions.pack(pady=5)

    question_label = tk.Label(root, text=askables[0][0], font=("Arial", 14))
    question_label.pack(pady=10)

    var = tk.StringVar()
    options_frame = tk.Frame(root)
    options_frame.pack()

    option_buttons = []
    selected_label = tk.Label(root, text="", font=("Arial", 11), fg="gray")
    selected_label.pack(pady=2)

    def update_selected_label():
        chosen = []
        for i, ans in enumerate(answers):
            chosen.append(f"{askables[i][0]} {ans}")
        if current[0] < len(askables) and var.get():
            chosen.append(f"{askables[current[0]][0]} {var.get()}")
        selected_label.config(text="Choices so far:\n" + "\n".join(chosen))

    def show_question(idx):
        question_label.config(text=askables[idx][0])
        for widget in options_frame.winfo_children():
            widget.destroy()
        var.set("")
        option_buttons.clear()
        for i, opt in enumerate(askables[idx][1]):
            ttk.Radiobutton(options_frame, text=f"{i+1}. {opt}", variable=var, value=opt, command=update_selected_label).pack(anchor="w", padx=20, pady=2)
        update_selected_label()

    def next_question(event=None):
        sel = var.get()
        if not sel:
            messagebox.showwarning("Input required", "Please select an option.")
            return
        answers.append(sel.split()[0])  # get just the Prolog atom
        if current[0] < len(askables) - 1:
            current[0] += 1
            show_question(current[0])
        else:
            # query using valid_spot instead of study_spot
            query = f"valid_spot(Name, {', '.join(answers)})"
            results = [sol['Name'] for sol in prolog.query(query)]
            for widget in root.winfo_children():
                widget.destroy()
            tk.Label(root, text="Your choices:", font=("Arial", 11, "bold")).pack(pady=2)
            tk.Label(root, text="\n".join([f"{askables[i][0]} {answers[i]}" for i in range(len(answers))]), font=("Arial", 11), fg="gray").pack(pady=2)
            if results:
                tk.Label(root, text="Recommended study spots:", font=("Arial", 14)).pack(pady=10)
                for name in results:
                    tk.Label(root, text=f"- {name}", font=("Arial", 12)).pack(anchor="w")
            else:
                tk.Label(root, text="No matching study spots found.", font=("Arial", 14)).pack(pady=10)
            def restart():
                root.destroy()
                run_expert_system_gui()
            ttk.Button(root, text="Restart", command=restart).pack(pady=20)

    def on_key(event):
        if event.char.isdigit():
            idx = int(event.char) - 1
            if 0 <= idx < len(option_buttons):
                var.set(askables[current[0]][1][idx])
                update_selected_label()
        if event.keysym == "Return":
            next_question()

    next_btn = ttk.Button(root, text="Next", command=next_question)
    next_btn.pack(pady=10)

    show_question(0)
    root.bind("<Key>", on_key)
    root.mainloop()

if __name__ == "__main__":
   	run_expert_system_gui()
