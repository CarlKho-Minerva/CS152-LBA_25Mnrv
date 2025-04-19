from pyswip import Prolog
import tkinter as tk
from tkinter import ttk, messagebox
import os

# List of questions and options to display in the GUI
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


def consult_kb(prolog):
    """Load the knowledge base from kb.pl file"""
    kb_path = os.path.join(os.path.dirname(__file__), 'kb.pl')
    prolog.consult(kb_path)


def run_expert_system_gui():
    """Main function to run the expert system with GUI"""
    prolog = Prolog()
    
    # Load the knowledge base from the external file
    consult_kb(prolog)

    root = tk.Tk()
    root.title("Study Spot Recommender")
    root.geometry("520x450")  # Made slightly taller for the Skip button

    answers = []
    skipped = set()  # Keep track of skipped questions
    current = [0]

    instructions = tk.Label(root, text="Answer each question to get a study spot recommendation.\nUse number keys or mouse to select, Enter to continue, or skip if not important.", font=("Arial", 11), fg="gray")
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
            if i not in skipped:  # Only show non-skipped answers
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

    def skip_question():
        """Skip the current question and move to the next one"""
        # Mark this question as skipped
        skipped.add(current[0])
        answers.append("SKIPPED")  # Placeholder in answers list
        
        if current[0] < len(askables) - 1:
            current[0] += 1
            show_question(current[0])
        else:
            show_results()

    def show_results():
        """Show the recommendation results"""
        # Query the recommended spots
        results = list(prolog.query("recommend(ID, Name)"))
        spot_names = [sol['Name'] for sol in results]
        
        # Display results
        for widget in root.winfo_children():
            widget.destroy()
        
        tk.Label(root, text="Your choices:", font=("Arial", 11, "bold")).pack(pady=2)
        
        # Show only non-skipped choices
        choices = []
        for i, ans in enumerate(answers):
            if i not in skipped:
                choices.append(f"{askables[i][0]} {ans}")
        
        choices_text = "\n".join(choices) if choices else "No specific criteria selected"
        tk.Label(root, text=choices_text, font=("Arial", 11), fg="gray").pack(pady=2)
        
        if spot_names:
            tk.Label(root, text="Recommended study spots:", font=("Arial", 14)).pack(pady=10)
            for name in spot_names:
                tk.Label(root, text=f"- {name}", font=("Arial", 12)).pack(anchor="w")
        else:
            tk.Label(root, text="No matching study spots found.", font=("Arial", 14)).pack(pady=10)
        
        # Add restart button
        def restart():
            # Clear asserted answers
            list(prolog.query("clear_test"))
            root.destroy()
            run_expert_system_gui()
        
        ttk.Button(root, text="Restart", command=restart).pack(pady=20)

    def next_question(event=None):
        sel = var.get()
        if not sel:
            messagebox.showwarning("Input required", "Please select an option or click Skip if this criterion is not important.")
            return
        
        # Extract just the Prolog atom from the selected option
        val = sel.split()[0]
        answers.append(val)
        
        # Get the attribute name based on the current question
        attribute = get_attribute_from_question(current[0])
        
        # Assert the user's answer as a fact in Prolog
        prolog.assertz(f"answered({attribute}, {val})")
        
        if current[0] < len(askables) - 1:
            current[0] += 1
            show_question(current[0])
        else:
            show_results()

    def get_attribute_from_question(question_idx):
        """Map question index to the corresponding Prolog attribute name"""
        attributes = [
            "location", "cost", "food", "seating", 
            "closing_time", "wifi", "noise", "outlets"
        ]
        return attributes[question_idx]

    def on_key(event):
        if event.char.isdigit():
            idx = int(event.char) - 1
            if 0 <= idx < len(askables[current[0]][1]):
                var.set(askables[current[0]][1][idx])
                update_selected_label()
        if event.keysym == "Return":
            next_question()
        if event.keysym == "Escape":
            skip_question()

    # Create button frame to hold Next and Skip buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    
    next_btn = ttk.Button(button_frame, text="Next", command=next_question)
    next_btn.pack(side=tk.LEFT, padx=5)
    
    skip_btn = ttk.Button(button_frame, text="Skip this question", command=skip_question)
    skip_btn.pack(side=tk.LEFT, padx=5)

    # Add buttons for test cases
    def run_test_case(case_num):
        # Clear previous answers
        for widget in root.winfo_children():
            widget.destroy()
        
        # Clear any previous answers in Prolog
        list(prolog.query("clear_test"))
        
        # Get test case description
        result = list(prolog.query(f"test_case({case_num}, Description)"))
        description = result[0]['Description'] if result else f"Test Case {case_num}"
        
        # Run the test case
        list(prolog.query(f"test_case({case_num}, _)"))
        
        # Get recommendations
        results = list(prolog.query("recommend(ID, Name)"))
        spot_names = [sol['Name'] for sol in results]
        
        # Display results
        tk.Label(root, text=f"Test Case {case_num}: {description}", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Get and display the criteria used
        criteria = list(prolog.query("answered(Attribute, Value)"))
        tk.Label(root, text="Test Criteria:", font=("Arial", 12, "bold")).pack(pady=5, anchor="w", padx=20)
        for c in criteria:
            tk.Label(root, text=f"- {c['Attribute']}: {c['Value']}", font=("Arial", 11)).pack(anchor="w", padx=40)
        
        tk.Label(root, text="\nRecommendations:", font=("Arial", 12, "bold")).pack(pady=5, anchor="w", padx=20)
        if spot_names:
            for name in spot_names:
                tk.Label(root, text=f"- {name}", font=("Arial", 11)).pack(anchor="w", padx=40)
        else:
            tk.Label(root, text="No matching study spots found.", font=("Arial", 11)).pack(anchor="w", padx=40)
        
        # Add buttons to return to main menu or try other test cases
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="Run Normal Mode", command=lambda: restart()).pack(side=tk.LEFT, padx=5)
        for i in range(1, 4):
            if i != case_num:  # Don't show button for current test case
                ttk.Button(btn_frame, text=f"Test Case {i}", 
                          command=lambda i=i: run_test_case(i)).pack(side=tk.LEFT, padx=5)

    def show_test_menu():
        """Show menu of test cases"""
        for widget in root.winfo_children():
            widget.destroy()
        
        tk.Label(root, text="Study Spot Recommender Tests", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Label(root, text="Select a test case to run:", font=("Arial", 12)).pack(pady=10)
        
        test_frame = tk.Frame(root)
        test_frame.pack(pady=10)
        
        test_cases = [
            "Test Case 1: Quiet, free, near campus",
            "Test Case 2: Lively cafe, outlets needed, Mission",
            "Test Case 3: Outdoor, food available, any cost"
        ]
        
        for i, test in enumerate(test_cases, 1):
            ttk.Button(test_frame, text=test, 
                      command=lambda i=i: run_test_case(i)).pack(anchor="w", pady=5, padx=20)
        
        ttk.Button(root, text="Start Normal Mode", 
                  command=lambda: restart()).pack(pady=20)

    # Add test mode button
    test_btn = ttk.Button(root, text="Run Tests", command=show_test_menu)
    test_btn.pack(pady=5)

    def restart():
        # Clear asserted answers
        list(prolog.query("clear_test"))
        root.destroy()
        run_expert_system_gui()

    show_question(0)
    root.bind("<Key>", on_key)
    root.mainloop()


if __name__ == "__main__":
    run_expert_system_gui()
