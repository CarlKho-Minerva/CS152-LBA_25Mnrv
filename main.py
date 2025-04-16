# Import the PySWIP library
from pyswip import Prolog
import os # Import os to construct the path

# --- 1. Initialize Prolog Engine ---
prolog = Prolog()

# --- 2. Load the Knowledge Base from kb.pl ---
kb_path = os.path.join(os.path.dirname(__file__), 'kb.pl')
print(f"Loading knowledge base from: {kb_path}")
prolog.consult(kb_path)

# Check if the knowledge base was properly loaded
print("Checking if predicates were loaded correctly...")
try:
    # List all predicates in the knowledge base to verify loading
    predicates = list(prolog.query("current_predicate(Name/Arity)"))
    print(f"Found {len(predicates)} predicates in total.")
    print("Looking for recommend/2 predicate...")
    
    # Specifically check for recommend/2
    if list(prolog.query("current_predicate(recommend/2)")):
        print("✓ recommend/2 predicate found!")
    else:
        print("✗ recommend/2 predicate NOT found!")
        
    # Manually add the recommend rule to see if that helps
    print("Manually adding recommend/2 rule...")
    # Add as a single line with no extra whitespace - PySWIP can be very strict
    prolog.assertz("recommend(SpotID, Name) :- spot(SpotID, Name), answered(cost, ReqCost), cost(SpotID, ReqCost), answered(noise, ReqNoise), noise(SpotID, ReqNoise), answered(food, ReqFood), food(SpotID, ReqFood), answered(late, ReqLate), late(SpotID, ReqLate), answered(wifi, ReqWifi), wifi(SpotID, ReqWifi), answered(outlets, ReqOutlets), outlets(SpotID, ReqOutlets).")
    print("Rule added manually.")
    
    # Verify the rule was properly added
    if list(prolog.query("current_predicate(recommend/2)")):
        print("✓ recommend/2 predicate found after manual addition!")
    else:
        print("✗ recommend/2 predicate STILL NOT found after manual addition!")
except Exception as e:
    print(f"Error during Prolog predicate check: {e}")

# --- 3. Function to Ask Questions and Store Answers ---
def ask_question(attribute, prompt, allowed_answers):
    """Asks the user a question, allowing numeric input, and stores the answer as a Prolog fact."""
    while True:
        # Create numbered options string: "1. free / 2. purchase_required"
        options_str = " / ".join([f"{i+1}. {ans.replace('_', ' ')}" for i, ans in enumerate(allowed_answers)]) # Make options more readable
        print(f"{prompt} ({options_str})")
        raw_input = input("> ").strip()
        selected_answer = None

        # Try interpreting input as a number
        try:
            choice_index = int(raw_input) - 1 # Convert to 0-based index
            if 0 <= choice_index < len(allowed_answers):
                selected_answer = allowed_answers[choice_index]
        except ValueError:
            # Input wasn't a number, check if it's a valid string answer (case-insensitive, space to underscore)
            cleaned_input = raw_input.lower().replace(" ", "_")
            if cleaned_input in allowed_answers:
                selected_answer = cleaned_input

        # Check if a valid answer was selected
        if selected_answer:
            # Store the answer in Prolog: answered(attribute, answer).
            # Ensure the answer stored is the Prolog-compatible version (lowercase, underscores)
            prolog_answer = selected_answer.lower().replace(" ", "_")
            prolog.assertz(f"answered({attribute}, {prolog_answer})")
            print("-" * 20) # Separator
            break
        else:
            # Update error message to include numeric options and more readable text options
            readable_options = [f"{i+1} or '{ans.replace('_', ' ')}'" for i, ans in enumerate(allowed_answers)]
            valid_options_msg = ", ".join(readable_options)
            print(f"Invalid input. Please enter one of: {valid_options_msg}")

# --- 4. Ask the Questions Sequentially ---
# (Based on your askables, simplified options for demo)
ask_question('cost', 'Do you want free access (no purchase required)?', ['free', 'purchase_required'])
ask_question('food', 'Do you want coffee or food available?', ['yes', 'no'])
# ask_question('seating', 'Do you want indoor or outdoor seating?', ['indoor', 'outdoor', 'both']) # Add this later
ask_question('late', 'Do you need it open late (after 8pm)?', ['yes', 'no'])
ask_question('wifi', 'Do you need WiFi?', ['yes', 'no'])
# ask_question('distance', 'How far are you willing to travel?', ['walk', 'short_ride', 'far']) # Add this later
ask_question('noise', 'Do you prefer a quiet or lively environment?', ['quiet', 'lively'])
ask_question('outlets', 'Do you need power outlets available?', ['yes', 'no'])

print("Okay, looking for recommendations based on your answers...\n")

# --- 5. Query Prolog for Recommendations ---
query = "recommend(SpotID, Name)"
recommendations = list(prolog.query(query)) # Use list() to get all results

# --- 6. Print Results ---
if recommendations:
    print("Found Recommendations:")
    # Using a set to avoid printing duplicate names if the logic somehow allows it
    unique_recommendations = set()
    for rec in recommendations:
        unique_recommendations.add(rec['Name']) # Extract the 'Name' variable

    for name in unique_recommendations:
        print(f"- {name}")
else:
    print("Sorry, no spots found matching all your criteria with the current simple rules.")
    print("Consider relaxing some requirements or expanding the knowledge base!")