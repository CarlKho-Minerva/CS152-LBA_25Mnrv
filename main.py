from pyswip import Prolog

# Prolog knowledge base for study spots
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
    # Example query: free, food, indoor, open late, wifi, walk, quiet, power
    print("Study spots matching: free, food, indoor, open late, wifi, walk, quiet, power")
    query = "study_spot(Name, yes, yes, indoor, yes, yes, walk, quiet, yes)"
    found = False
    for sol in prolog.query(query):
        print(f"- {sol['Name']}")
        found = True
    if not found:
        print("No matching study spots found.")

if __name__ == "__main__":
    main()
