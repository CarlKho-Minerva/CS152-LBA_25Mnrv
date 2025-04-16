from pyswip import Prolog
import tkinter as tk
from tkinter import ttk, messagebox

prolog_kb = """
study_spot(library, yes, no, indoor, yes, yes, walk, quiet, yes).
study_spot(cafe, yes, yes, indoor, no, yes, short_ride, lively, yes).
study_spot(park, yes, no, outdoor, no, no, walk, lively, no).
study_spot(student_center, yes, yes, indoor, yes, yes, walk, lively, yes).
"""

askables = [
    ("Do you want free access?", ["yes", "no"]),
    ("Do you want coffee or food available?", ["yes", "no"]),
    ("Do you want indoor or outdoor seating?", ["indoor", "outdoor"]),
    ("Do you need it open late (after 8pm)?", ["yes", "no"]),
    ("Do you need strong and reliable WiFi?", ["yes", "no"]),
    ("How far are you willing to travel from residence?", ["walk", "short_ride", "far"]),
    ("Do you prefer a quiet or lively environment?", ["quiet", "lively"]),
    ("Do you need power outlets available?", ["yes", "no"]),
]

def consult_kb(prolog, kb_str):
    for line in kb_str.strip().split('\n'):
        if line:
            prolog.assertz(line.strip('.'))

def run_expert_system_gui():
    prolog = Prolog()
    consult_kb(prolog, prolog_kb)

    root = tk.Tk()
    root.title("Study Spot Recommender")
    root.geometry("500x300")

    answers = []
    current = [0]  # mutable int for closure

    question_label = tk.Label(root, text=askables[0][0], font=("Arial", 14))
    question_label.pack(pady=20)

    var = tk.StringVar()
    options_frame = tk.Frame(root)
    options_frame.pack()

    def show_question(idx):
        question_label.config(text=askables[idx][0])
        for widget in options_frame.winfo_children():
            widget.destroy()
        var.set("")
        for opt in askables[idx][1]:
            b = ttk.Radiobutton(options_frame, text=opt, variable=var, value=opt)
            b.pack(anchor="w")

    def next_question():
        sel = var.get()
        if not sel:
            messagebox.showwarning("Input required", "Please select an option.")
            return
        answers.append(sel)
        if current[0] < len(askables) - 1:
            current[0] += 1
            show_question(current[0])
        else:
            # All questions answered, run query
            query = f"study_spot(Name, {', '.join(answers)})"
            results = [sol['Name'] for sol in prolog.query(query)]
            for widget in root.winfo_children():
                widget.destroy()
            if results:
                tk.Label(root, text="Recommended study spots:", font=("Arial", 14)).pack(pady=10)
                for name in results:
                    tk.Label(root, text=f"- {name}", font=("Arial", 12)).pack(anchor="w")
            else:
                tk.Label(root, text="No matching study spots found.", font=("Arial", 14)).pack(pady=10)

    next_btn = ttk.Button(root, text="Next", command=next_question)
    next_btn.pack(pady=10)

    show_question(0)
    root.mainloop()

if __name__ == "__main__":
    run_expert_system_gui()
