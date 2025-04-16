
Dove Log – Session Summary

Date: April 15, 2025

Actions Taken:
- Explained how to use Prolog logic in Python for a study spot recommendation expert system.
- Provided a basic Prolog knowledge base and example queries for study spots.
- Updated main.py to use an interactive, menu-based system that asks the user a series of questions (askables) about their preferences (free access, food, seating, open late, WiFi, distance, vibe, power outlets).
- Implemented a function to prompt the user for each askable and build a Prolog query based on their responses.
- Ensured the system displays matching study spots or a message if no matches are found.
- Confirmed the code is ready to run in both terminal and Jupyter notebook environments.

Outcome:
main.py now provides an interactive expert system for recommending study spots based on user preferences, fulfilling the assignment requirements for an interactive, menu-driven expert system using Prolog and Python.

# Development Log – Study Spot Recommender Expert System

**Date:** April 15, 2025

<div>
    <a href="https://www.loom.com/share/5a930c028a5f4400b34ef31bfa8f4812">
      <p>Python - Study Spot Recommender - 15 April 2025 - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/5a930c028a5f4400b34ef31bfa8f4812">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/5a930c028a5f4400b34ef31bfa8f4812-e955458295995afe-full-play.gif">
    </a>
  </div>

## Session Summary

### Initial Setup
- Created a Python project using PySWIP (Prolog-Python bridge) and tkinter for the GUI.
- Defined a Prolog knowledge base with several study spot facts and attributes.
- Implemented a basic Python script to query the Prolog knowledge base.

### Interactive CLI & GUI
- Added an interactive command-line interface to ask users a series of questions (askables) about their preferences.
- Extended the system to a tkinter-based GUI, presenting one question at a time and collecting user input via radio buttons.
- Enabled keyboard controls: number keys for option selection and Enter to proceed.
- Added a "Restart" button to allow users to retake the questionnaire.

### Natural Language & UX Improvements
- Replaced technical values (e.g., 'short_ride') with natural language equivalents (e.g., 'A short ride') throughout the interface.
- Capitalized all displayed values for clarity and professionalism.
- Displayed a running list of user choices in the GUI, updating in real time as selections are made.
- Removed redundant summary blurbs and ensured all output is user-friendly and conversational.

### Testing & Validation
- Verified that the system works in both terminal and GUI modes.
- Ensured that all user choices and recommendations are displayed in clear, natural language.

## Next Steps / To-Do
- Expand the Prolog knowledge base with more real-world study spots and attributes.
- Optionally, add more advanced filtering or a map integration.
- Collect user feedback for further UX improvements.

---

**End of Dev Log**
