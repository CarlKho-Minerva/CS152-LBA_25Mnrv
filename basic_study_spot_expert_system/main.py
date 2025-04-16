# main.py - Minimal CLI Study Spot Recommender using PySWIP
from pyswip import Prolog

ASKABLES = [
    ("free", "Do you need free access? (yes/no): "),
    ("food", "Do you want food available? (yes/no): "),
    ("seating", "Preferred seating (quiet/casual/outdoor): "),
    ("latenight", "Need late-night access? (yes/no): "),
    ("wifi", "Require WiFi? (yes/no): "),
    ("distance", "Preferred distance (short/medium/long): "),
    ("atmosphere", "Atmosphere (silent/lively/social/relaxed): "),
    ("power", "Need power outlets? (yes/no): ")
]

def main():
    prolog = Prolog()
    prolog.consult("study_spots.pl")
    answers = {}
    for key, question in ASKABLES:
        while True:
            ans = input(question).strip().lower()
            if ans:
                answers[key] = ans
                break
    query = f"study_spot(Spot, {answers['free']}, {answers['food']}, {answers['seating']}, {answers['latenight']}, {answers['wifi']}, {answers['distance']}, {answers['atmosphere']}, {answers['power']})"
    results = list(prolog.query(query))
    if results:
        print("\nRecommended study spot(s):")
        for r in results:
            print("-", r['Spot'].replace('_', ' ').title())
    else:
        print("\nNo matching study spot found. Try different preferences.")

if __name__ == "__main__":
    main()
