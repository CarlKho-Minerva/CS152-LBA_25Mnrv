import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from utils import ICONS, format_option, get_attribute_from_question

def create_progress_bar(container, progress_var):
    """Create and return a progress bar frame"""
    progress_frame = ttk.Frame(container)
    progress_frame.pack(fill=tk.X, pady=(0, 20))
    
    progress_bar = ttk.Progressbar(
        progress_frame,
        variable=progress_var,
        mode='determinate',
        style='info.Horizontal.TProgressbar'
    )
    progress_bar.pack(fill=tk.X)
    progress_label = ttk.Label(progress_frame, text="Question 1/8", style='info.TLabel')
    progress_label.pack(pady=(5, 0))
    return progress_frame, progress_label

def create_question_card(container, question_text):
    """Create and return a question card frame"""
    card_frame = ttk.Frame(container, style='Card.TFrame')
    card_frame.pack(fill=tk.BOTH, expand=True, pady=10)

    question_header = ttk.Frame(card_frame)
    question_header.pack(fill=tk.X, padx=20, pady=10)
    
    icon_label = ttk.Label(question_header, text="", font=("TkDefaultFont", 24))
    icon_label.pack(side=tk.LEFT, padx=(0, 10))
    
    question_label = ttk.Label(question_header, text=question_text, font=("TkDefaultFont", 14, "bold"))
    question_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

    ttk.Separator(card_frame, orient='horizontal').pack(fill=tk.X, padx=20)
    
    return card_frame, icon_label, question_label

def create_review_panel(container):
    """Create and return a review panel"""
    review_frame = ttk.LabelFrame(container, text="Your Selections So Far", padding=10)
    review_frame.pack(fill=tk.X, pady=10)
    
    selections_text = tk.Text(review_frame, height=6, font=("TkDefaultFont", 11))
    selections_text.pack(fill=tk.X, padx=5, pady=5)
    selections_text.config(state=tk.DISABLED)
    
    return review_frame, selections_text

def create_navigation_buttons(container, back_cmd, skip_cmd, next_cmd):
    """Create and return navigation buttons"""
    button_frame = ttk.Frame(container)
    button_frame.pack(fill=tk.X, pady=10)
    
    back_btn = ttk.Button(button_frame, text="← Back", command=back_cmd, style='info.TButton')
    back_btn.pack(side=tk.LEFT, padx=5)
    
    skip_btn = ttk.Button(button_frame, text="Skip", command=skip_cmd, style='secondary.TButton')
    skip_btn.pack(side=tk.LEFT, padx=5)
    
    next_btn = ttk.Button(button_frame, text="Next →", command=next_cmd, style='info.TButton')
    next_btn.pack(side=tk.LEFT, padx=5)
    
    return button_frame

def show_results_view(container, answers, askables, spot_names, restart_cmd):
    """Create and show the results view"""
    # Clear container
    for widget in container.winfo_children():
        widget.destroy()
    
    # Results header
    ttk.Label(
        container,
        text="Your Study Spot Recommendations",
        font=("TkDefaultFont", 18, "bold"),
        style='info.TLabel'
    ).pack(pady=20)
    
    # Your selections section
    selections_frame = ttk.LabelFrame(container, text="Your Preferences", padding=10)
    selections_frame.pack(fill=tk.X, padx=20, pady=10)
    
    for i, ans in enumerate(answers):
        formatted_ans = format_option(ans)
        selection_text = f"{ICONS.get(get_attribute_from_question(i), '•')} {askables[i][0]}: {formatted_ans}"
        ttk.Label(selections_frame, text=selection_text).pack(anchor=tk.W, pady=2)
    
    # Recommendations section
    recommendations_frame = ttk.LabelFrame(container, text="Recommended Spots", padding=10)
    recommendations_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    if spot_names:
        for name in spot_names:
            spot_frame = ttk.Frame(recommendations_frame)
            spot_frame.pack(fill=tk.X, pady=5)
            ttk.Label(spot_frame, text="📍", font=("TkDefaultFont", 14)).pack(side=tk.LEFT, padx=5)
            ttk.Label(spot_frame, text=name, font=("TkDefaultFont", 12)).pack(side=tk.LEFT)
    else:
        ttk.Label(
            recommendations_frame,
            text="No matching study spots found.\nTry adjusting your criteria.",
            style='info.TLabel'
        ).pack(pady=20)
    
    # Restart button
    ttk.Button(
        container,
        text="Start Over",
        style='info.TButton',
        command=restart_cmd
    ).pack(pady=20) 