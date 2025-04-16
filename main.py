from pyswip import Prolog

def ask_menu(prompt, options):
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        try:
            choice = int(input("Enter option number: "))
            if 1 <= choice <= len(options):
                return options[choice-1]
        except ValueError:
            pass
        print("Invalid input. Please enter a number from the list.")

prolog_kb = """
study_spot(library, yes, no, indoor, yes, yes, walk, quiet, yes).
study_spot(cafe, yes, yes, indoor, no, yes, short_ride, lively, yes).
study_spot(park, yes, no, outdoor, no, no, walk, lively, no).
study_spot(student_center, yes, yes, indoor, yes, yes, walk, lively, yes).
"""

def consult_kb(prolog, kb_str):
    for line in kb_str.strip().split('\n'):
        if line:
            prolog.assertz(line.strip('.'))

def main():
    prolog = Prolog()
    consult_kb(prolog, prolog_kb)

    # Askables and options
    free = ask_menu("Do you want free access?", ["yes", "no"])
    food = ask_menu("Do you want coffee or food available?", ["yes", "no"])
    seating = ask_menu("Do you want indoor or outdoor seating?", ["indoor", "outdoor"])
    open_late = ask_menu("Do you need it open late (after 8pm)?", ["yes", "no"])
    wifi = ask_menu("Do you need strong and reliable WiFi?", ["yes", "no"])
    distance = ask_menu("How far are you willing to travel from residence?", ["walk", "short_ride", "far"])
    vibe = ask_menu("Do you prefer a quiet or lively environment?", ["quiet", "lively"])
    power = ask_menu("Do you need power outlets available?", ["yes", "no"])

    query = f"study_spot(Name, {free}, {food}, {seating}, {open_late}, {wifi}, {distance}, {vibe}, {power})"
    print("\nRecommended study spots:")
    found = False
    for sol in prolog.query(query):
        print(f"- {sol['Name']}")
        found = True
    if not found:
        print("No matching study spots found.")

if __name__ == "__main__":
    main()
