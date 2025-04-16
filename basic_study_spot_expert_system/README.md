# Basic Study Spot Expert System

This is a minimal, professor-checkable version of the Study Spot Recommender expert system. It uses a simple Python CLI (PySWIP) and a small Prolog knowledge base.

## Features
- 8 askable attributes (free, food, seating, late-night, wifi, distance, atmosphere, power)
- 4 example study spots
- Command-line interface only

## How to Run
1. Install requirements:
   ```
   pip install -r requirements.txt
   ```
2. Run the recommender:
   ```
   python main.py
   ```
3. Answer the 8 questions. The system will recommend a study spot or notify if no match is found.

## Files
- `main.py`: Python CLI script
- `study_spots.pl`: Prolog knowledge base
- `requirements.txt`: Python dependency (PySWIP)
- `test_cases.md`: Example runs and real-life reflection

---
