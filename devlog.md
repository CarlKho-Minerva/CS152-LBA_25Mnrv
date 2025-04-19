# Dev Log – Session Summary

**Date:** April 15, 2025

### Actions Taken:
- Built a study spot recommendation expert system integrating Prolog logic with Python
- Created a comprehensive Prolog knowledge base containing study spot facts and attributes
- Developed an interactive menu-based system that prompts users for preferences including:
    - Free access requirements
    - Food availability
    - Seating options
    - Late-night access
    - WiFi connectivity
    - Distance considerations
    - Atmosphere/vibe
    - Power outlet availability
- Implemented a preference-gathering function that constructs Prolog queries based on user input
- Ensured the system provides appropriate feedback, whether displaying matching study spots or notifying when no matches exist
- Verified functionality in both terminal and Jupyter notebook environments

### Outcome:
Successfully delivered main.py as an interactive expert system that recommends study spots based on user preferences, meeting all assignment requirements for a menu-driven expert system utilizing Prolog and Python integration.

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

**Date:** April 15, 2025 - Dice, Prolog Implementation (This is overview, more documentation below)

This branch implements the Prolog logic for the Study Spot Recommender system, focusing on the core knowledge base and recommendation rules.

## Files

- `kb.pl`: The Prolog knowledge base containing facts about study spots and the recommendation rules
- `main.py`: The GUI application using tkinter and PySwip to interact with the Prolog engine
- `test_prolog.py`: Test module for documenting and verifying the Prolog recommendation logic

## Implementation Details

### Prolog Knowledge Base

The knowledge base (`kb.pl`) is structured with the following predicates:

- `spot(ID, 'Name')`: Maps spot IDs to their names
- `location(ID, Distance)`: Distance from Minerva residence
- `cost(ID, CostLevel)`: Cost level (free, low, medium, high)
- `food(ID, FoodOption)`: Food options (none, coffee_only, snacks_only, full_menu)
- `seating(ID, SeatingType)`: Types of seating available (multiple per spot)
- `closing_time(ID, ClosingTime)`: Closing times
- `wifi(ID, WifiQuality)`: WiFi quality (none, poor, good)
- `noise(ID, NoiseLevel)`: Noise levels (silent, low, moderate, high)
- `outlets(ID, OutletAvailability)`: Outlet availability (none, few, many, every_seat)

The core recommendation rule `recommend/2` handles matching the user's criteria with the available study spots.

### Test Cases

Three distinct test cases are implemented:

1. **Quiet, free, near campus**: Tests finding spots that are silent, low cost, and close to campus
2. **Lively cafe, outlets needed, Mission**: Tests finding spots that are in the Mission (far), have high noise level, good WiFi, and many outlets
3. **Outdoor, food available, any cost**: Tests finding spots with outdoor seating and full food menu options

## Running the Application

1. Install required packages:
   ```
   pip install pyswip tabulate
   ```

2. Run the GUI application:
   ```
   python main.py
   ```

3. Run the tests:
   ```
   python test_prolog.py
   ```

## Notes

- The Prolog recommendation system uses a flexible approach that can handle optional criteria
- Test cases are designed to verify different combinations of criteria
- The GUI allows interactive selection of criteria and displays matching spots

**End of Dev Log**

# More details about the Documentation (Dice)

This document provides detailed information about the Prolog logic implementation for the Study Spot Recommender system.

## Knowledge Base Structure

The knowledge base (`kb.pl`) is organized as a collection of facts that describe study spots based on various attributes:

```prolog
% Basic structure
spot(ID, 'Name').
location(ID, Distance).
cost(ID, CostLevel).
food(ID, FoodOption).
seating(ID, SeatingType).
closing_time(ID, ClosingTime).
wifi(ID, WifiQuality).
noise(ID, NoiseLevel).
outlets(ID, OutletAvailability).
```

### Design Decisions:
- **ID-based Relations**: Each spot has a unique ID (1-19) that connects all of its attributes.
- **Normalized Structure**: Each attribute is stored in its own predicate for better maintenance.
- **Multiple Seating Types**: Seating is the only attribute that can have multiple values per spot.

## Recommendation Algorithm

The core of the system is the `recommend/2` rule, which uses a flexible algorithm to match user preferences with study spots:

```prolog
recommend(SpotID, Name) :-
    % Get the spot's name
    spot(SpotID, Name),
    
    % Check if all answered criteria match
    (answered(location, Loc) -> location(SpotID, Loc) ; true),
    (answered(cost, Cost) -> cost(SpotID, Cost) ; true),
    (answered(food, Food) -> food(SpotID, Food) ; true),
    (answered(seating, Seat) -> seating(SpotID, Seat) ; true),
    (answered(closing_time, Close) -> closing_time(SpotID, Close) ; true),
    (answered(wifi, Wifi) -> wifi(SpotID, Wifi) ; true),
    (answered(noise, Noise) -> noise(SpotID, Noise) ; true),
    (answered(outlets, Outlet) -> outlets(SpotID, Outlet) ; true).
```

### How the Algorithm Works:

1. **Conditional Match**: For each attribute, the rule checks if the user has specified a preference (represented as an `answered/2` fact).
2. **If-Then-Else Pattern**: The `Condition -> Then ; Else` pattern is used to make criteria optional:
   - If a criterion has been answered: `(answered(attribute, Value) -> attribute(SpotID, Value) ; true)`
   - If answered, it must match the spot's attribute value
   - If not answered, it's skipped (via the `true` clause)
3. **All Conditions Must Match**: For a spot to be recommended, all the conditions that the user specified must match.

### Advantage of This Approach:
- **Flexibility**: Users don't need to specify every criterion.
- **Readable Code**: The structure makes it easy to understand how matching works.
- **Extensibility**: New criteria can be added by following the same pattern.

## Test Cases Implementation

Three distinct test cases are implemented to verify the system's effectiveness:

```prolog
% Test cases
test_case(1, "Quiet, free, near campus") :- 
    assert(answered(noise, silent)),
    assert(answered(cost, low)),
    assert(answered(location, close)).

test_case(2, "Lively cafe, outlets needed, Mission") :-
    assert(answered(noise, high)),
    assert(answered(outlets, many)),
    assert(answered(location, far)),
    assert(answered(wifi, good)).

test_case(3, "Outdoor, food available, any cost") :-
    assert(answered(seating, outdoor_seating)),
    assert(answered(food, full_menu)).
```

### Each Test Case Serves a Specific Purpose:

1. **Case 1 (Quiet, free, near campus)**:
   - Tests spots that meet all three criteria: noise=silent, cost=low, location=close
   - Expected result: SF Public Library

2. **Case 2 (Lively cafe, outlets needed, Mission)**:
   - Tests a different combination: noise=high, outlets=many, location=far, wifi=good
   - Expected results: Spro Mission (and potentially Sanas Coffee)

3. **Case 3 (Outdoor, food available, any cost)**:
   - Tests a minimal set of criteria: seating=outdoor_seating, food=full_menu
   - Expected to match multiple locations (6 in our tests)

### Test Handling:

- **Assertion Management**: We use `assert/1` to add facts and `clear_test/0` to clean up:
  ```prolog
  clear_test :-
      retractall(answered(_, _)).
  ```
- **Test Documentation**: `test_prolog.py` provides a detailed analysis of test results, including expected matches.

## Integration with Python

The Prolog knowledge base integrates with Python through PySwip:

1. **Loading the KB**: 
   ```python
   def consult_kb(prolog):
       kb_path = os.path.join(os.path.dirname(__file__), 'kb.pl')
       prolog.consult(kb_path)
   ```

2. **Asserting User Answers**:
   ```python
   prolog.assertz(f"answered({attribute}, {val})")
   ```

3. **Querying Recommendations**:
   ```python
   results = list(prolog.query("recommend(ID, Name)"))
   ```

## GUI Implementation

The GUI has been updated to allow users to skip questions they don't consider important, which aligns with the flexible recommendation algorithm in the Prolog knowledge base:

1. **Skip Button Added**: Users can skip any question they don't want to answer.
2. **Optional Criteria**: The system will only filter based on the criteria the user actually provides.
3. **Keyboard Shortcuts**: 
   - Enter key to proceed to the next question
   - Escape key to skip the current question
   - Number keys (1-N) to select options quickly

This approach ensures that the Prolog recommendation rule, which is designed to handle optional criteria, works in harmony with the user interface.

## Performance Considerations

- **Rule Structure**: The recommendation rule is designed to fail fast if any criterion doesn't match.
- **No Recursive Searches**: The algorithm avoids expensive recursive searches by using direct fact matching.
- **Optional Criteria**: The system handles optional criteria efficiently through conditional evaluation.

## Future Enhancements

Possible improvements to the Prolog logic:

1. **Weighted Recommendations**: Add weights to different criteria to rank results.
2. **Fuzzy Matching**: Allow partial matches (e.g., "close enough" to location).
3. **Negative Preferences**: Support "NOT" conditions (e.g., not noisy).
4. **Preference Ranking**: Return spots in order of how well they match preferences.

## Lessons Learned

- **Separation of Concerns**: Moving the knowledge base to a separate file improved maintainability.
- **Testing Structure**: Having predefined test cases saved debugging time.
- **Flexible Matching**: The conditional approach to criteria made the system more user-friendly.

This implementation successfully meets the requirements for the Prolog logic component, providing a robust and flexible recommendation system.