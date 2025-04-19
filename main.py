from pyswip import Prolog
import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from utils import ICONS, format_option, get_attribute_from_question
from gui import (
    create_progress_bar, 
    create_question_card, 
    create_review_panel, 
    create_navigation_buttons,
    show_results_view
)

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

def get_next_question(current_idx, answers, prolog):
    """Determine the next relevant question based on previous answers"""
    if current_idx >= len(askables) - 1:
        return None
    
    next_idx = current_idx + 1
    attribute = get_attribute_from_question(next_idx)
    
    # Example dynamic logic based on previous answers:
    # If user selected "none" for food, skip the seating question
    if attribute == "seating" and any(ans.startswith("none") for ans in answers):
        return get_next_question(next_idx, answers, prolog)
    
    # If user selected "very_close", skip the wifi question (assuming they can go home if wifi is poor)
    if attribute == "wifi" and any(ans.startswith("very_close") for ans in answers):
        return get_next_question(next_idx, answers, prolog)
    
    # If user selected "outdoor_seating", skip the outlets question
    if attribute == "outlets" and any("outdoor_seating" in ans for ans in answers):
        return get_next_question(next_idx, answers, prolog)
    
    return next_idx

def run_expert_system_gui():
    """Main function to run the expert system with GUI"""
    prolog = Prolog()
    
    # Load the knowledge base from the external file
    consult_kb(prolog)

    # Use ttkbootstrap for modern styling
    root = ttk.Window(themename="cosmo")
    root.title("Study Spot Recommender")
    root.geometry("800x600")

    answers = []
    skipped = set()  # Keep track of skipped questions
    current = [0]

    # Create main container
    main_container = ttk.Frame(root, padding="20")
    main_container.pack(fill=tk.BOTH, expand=True)

    # Create UI components
    progress_var = tk.DoubleVar(root)
    progress_frame, progress_label = create_progress_bar(main_container, progress_var)
    
    card_frame, icon_label, question_label = create_question_card(main_container, askables[0][0])
    
    var = tk.StringVar(root)
    options_frame = ttk.Frame(card_frame, padding=20)
    options_frame.pack(fill=tk.BOTH, expand=True)

    review_frame, selections_text = create_review_panel(main_container)

    def update_progress():
        """Update progress bar and label"""
        progress = (current[0] / len(askables)) * 100
        progress_var.set(progress)
        progress_label.config(text=f"Question {current[0] + 1}/{len(askables)}")

    def update_review_panel():
        """Update the review panel with current selections"""
        selections_text.config(state=tk.NORMAL)
        selections_text.delete(1.0, tk.END)
        
        chosen = []
        for i, ans in enumerate(answers):
            if i not in skipped:
                formatted_ans = format_option(ans)
                chosen.append(f"{ICONS.get(get_attribute_from_question(i), '•')} {askables[i][0]}\n   ➜ {formatted_ans}")
        
        if current[0] < len(askables) and var.get():
            formatted_current = format_option(var.get())
            chosen.append(f"{ICONS.get(get_attribute_from_question(current[0]), '•')} {askables[current[0]][0]}\n   ➜ {formatted_current}")
        
        selections_text.insert(tk.END, "\n\n".join(chosen))
        selections_text.config(state=tk.DISABLED)

    def show_question(idx):
        """Display a question with modern styling"""
        # Update progress
        update_progress()
        
        # Update question and icon
        question_label.config(text=askables[idx][0])
        icon_label.config(text=ICONS.get(get_attribute_from_question(idx), "❓"))
        
        # Clear and update options
        for widget in options_frame.winfo_children():
            widget.destroy()
        
        var.set("")
        for i, opt in enumerate(askables[idx][1]):
            option_frame = ttk.Frame(options_frame)
            option_frame.pack(fill=tk.X, pady=2)
            
            formatted_opt = format_option(opt)
            rb = ttk.Radiobutton(
                option_frame,
                text=formatted_opt,
                variable=var,
                value=opt,
                style='TRadiobutton',
                command=update_review_panel
            )
            rb.pack(side=tk.LEFT, padx=5)
            
            # Add tooltip
            ToolTip(rb, text=f"Option {i+1}: {formatted_opt}")
        
        update_review_panel()

    def back_question():
        """Go back to the previous question"""
        if current[0] > 0:
            current[0] -= 1
            if len(answers) > current[0]:
                answers.pop()
            show_question(current[0])

    def next_question(event=None):
        """Proceed to next question with validation"""
        sel = var.get()
        if not sel:
            messagebox.showwarning(
                "Input Required",
                "Please select an option or click Skip if this criterion is not important.",
                parent=root
            )
            return
        
        # Extract just the Prolog atom from the selected option
        val = sel.split()[0]
        answers.append(sel)  # Store full text for display
        
        # Get the attribute name based on the current question
        attribute = get_attribute_from_question(current[0])
        
        # Assert the user's answer as a fact in Prolog
        prolog.assertz(f"answered({attribute}, {val})")
        
        if current[0] < len(askables) - 1:
            current[0] += 1
            show_question(current[0])
        else:
            show_results()

    def show_results():
        """Show recommendations with modern styling"""
        results = list(prolog.query("recommend(ID, Name)"))
        spot_names = [sol['Name'] for sol in results]
        
        show_results_view(main_container, answers, askables, spot_names, restart)

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

    def restart():
        """Restart the application"""
        root.destroy()  # Destroy the current window
        list(prolog.query("clear_test"))  # Clear Prolog facts
        run_expert_system_gui()  # Start a new instance

    # Create navigation buttons
    create_navigation_buttons(main_container, back_question, skip_question, next_question)

    # Key bindings
    root.bind("<Return>", next_question)
    root.bind("<Escape>", lambda e: skip_question())
    root.bind("<Left>", lambda e: back_question())
    root.bind("<Right>", lambda e: next_question())

    # Initialize first question
    show_question(0)
    root.mainloop()

if __name__ == "__main__":
    run_expert_system_gui()
