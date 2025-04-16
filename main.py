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
    root.geometry("520x350")

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
        if answers or var.get():
            chosen = []
            for i, ans in enumerate(answers):
                label = askables[i][0]
                val = ans.replace("short_ride", "a short ride").replace("walk", "walking distance").replace("far", "far from residence")
                val = val.replace("yes", "Yes").replace("no", "No")
                chosen.append(f"{label} {val}")
            if current[0] < len(askables):
                if var.get():
                    label = askables[current[0]][0]
                    val = var.get().replace("short_ride", "a short ride").replace("walk", "walking distance").replace("far", "far from residence")
                    val = val.replace("yes", "Yes").replace("no", "No")
                    chosen.append(f"{label} {val}")
            selected_label.config(text="Choices so far:\n" + "\n".join(chosen))
        else:
            selected_label.config(text="")

    def show_question(idx):
        question_label.config(text=askables[idx][0])
        for widget in options_frame.winfo_children():
            widget.destroy()
        var.set("")
        option_buttons.clear()
        for i, opt in enumerate(askables[idx][1]):
            b = ttk.Radiobutton(options_frame, text=f"{i+1}. {opt}", variable=var, value=opt, command=update_selected_label)
            b.pack(anchor="w", padx=20, pady=2)
            option_buttons.append(b)
        update_selected_label()

    def next_question(event=None):
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
            tk.Label(root, text="Your choices:", font=("Arial", 11, "bold")).pack(pady=2)
            tk.Label(root, text="\n".join([
                f"{askables[i][0]} {answers[i].replace('short_ride', 'a short ride').replace('walk', 'walking distance').replace('far', 'far from residence').replace('yes', 'Yes').replace('no', 'No')}"
                for i in range(len(answers))]), font=("Arial", 11), fg="gray").pack(pady=2)
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
        # Number key selection
        if event.char.isdigit():
            idx = int(event.char) - 1
            if 0 <= idx < len(option_buttons):
                var.set(askables[current[0]][1][idx])
                update_selected_label()
        # Enter key to proceed
        if event.keysym == "Return":
            next_question()

    next_btn = ttk.Button(root, text="Next", command=next_question)
    next_btn.pack(pady=10)

    show_question(0)
    root.bind("<Key>", on_key)
    root.mainloop()

if __name__ == "__main__":
    run_expert_system_gui()
