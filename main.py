from pyswip import Prolog

# Example Prolog knowledge base as a string
prolog_kb = """
parent(john, mary).
parent(mary, susan).
parent(susan, tom).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
"""

def consult_kb(prolog, kb_str):
    for line in kb_str.strip().split('\n'):
        if line:
            prolog.assertz(line.strip('.'))

def main():
    prolog = Prolog()
    try:
        consult_kb(prolog, prolog_kb)
        print("Ancestors of tom:")
        for sol in prolog.query("ancestor(X, tom)"):
            print(f"- {sol['X']}")
    except Exception as e:
        print(f"Prolog error: {e}")

if __name__ == "__main__":
    main()
