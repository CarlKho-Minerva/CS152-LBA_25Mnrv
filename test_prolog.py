#!/usr/bin/env python3
"""
Test module for the Study Spot Recommender Prolog system
This documents the test cases for the knowledge base and recommendation system
"""

from pyswip import Prolog
import os
import sys
from tabulate import tabulate

def load_kb():
    """Load the knowledge base from the kb.pl file"""
    prolog = Prolog()
    kb_path = os.path.join(os.path.dirname(__file__), 'kb.pl')
    prolog.consult(kb_path)
    return prolog

def run_test_case(prolog, case_num):
    """Run a test case and return the results"""
    # Clear any previous answers
    list(prolog.query("clear_test"))
    
    # Get test case description
    result = list(prolog.query(f"test_case({case_num}, Description)"))
    description = result[0]['Description'] if result else f"Test Case {case_num}"
    
    # Run the test case
    list(prolog.query(f"test_case({case_num}, _)"))
    
    # Get criteria used
    criteria = list(prolog.query("answered(Attribute, Value)"))
    criteria_dict = {c['Attribute']: c['Value'] for c in criteria}
    
    # Get recommendations
    results = list(prolog.query("recommend(ID, Name)"))
    recommendations = [sol['Name'] for sol in results]
    
    return {
        'case_num': case_num,
        'description': description,
        'criteria': criteria_dict,
        'recommendations': recommendations
    }

def print_test_results(test_results):
    """Print test results in a nice format"""
    print(f"\n{'=' * 80}")
    print(f"TEST CASE {test_results['case_num']}: {test_results['description']}")
    print(f"{'-' * 80}")
    
    # Print criteria
    print("INPUT CRITERIA:")
    criteria_table = []
    for attr, val in test_results['criteria'].items():
        criteria_table.append([attr, val])
    print(tabulate(criteria_table, headers=["Attribute", "Value"], tablefmt="grid"))
    
    # Print recommendations
    print("\nRECOMMENDATIONS:")
    if test_results['recommendations']:
        for i, rec in enumerate(test_results['recommendations'], 1):
            print(f"  {i}. {rec}")
    else:
        print("  No matching study spots found.")
    
    # Analysis of results
    print("\nANALYSIS:")
    if test_results['case_num'] == 1:
        print("  This test case focuses on finding quiet, low-cost study spots near campus.")
        print("  Expected to match spots like SF Public Library which is silent, low cost, and close.")
        if 'SF Public Library' in test_results['recommendations']:
            print("  ✓ SF Public Library correctly recommended")
        else:
            print("  ✗ SF Public Library missing from recommendations")
    
    elif test_results['case_num'] == 2:
        print("  This test case looks for a lively cafe in the Mission area with good WiFi and many outlets.")
        print("  Expected to match spots that are far (Mission), have high noise, good WiFi, and many outlets.")
        expected = ["Spro Mission", "Sanas Coffee"] 
        found = [spot for spot in expected if spot in test_results['recommendations']]
        if found:
            print(f"  ✓ Found expected spots: {', '.join(found)}")
        else:
            print(f"  ✗ None of the expected spots were found: {', '.join(expected)}")
    
    elif test_results['case_num'] == 3:
        print("  This test case seeks outdoor seating options with full food menus.")
        print("  Expected to match multiple spots with outdoor seating and full menu options.")
        if len(test_results['recommendations']) >= 3:
            print(f"  ✓ Found {len(test_results['recommendations'])} spots matching criteria")
        else:
            print(f"  ✗ Found fewer spots than expected ({len(test_results['recommendations'])})")
    
    print(f"{'=' * 80}\n")

def run_all_tests():
    """Run all three test cases and print results"""
    prolog = load_kb()
    
    print("\nSTUDY SPOT RECOMMENDER - TEST RESULTS")
    print("====================================\n")
    
    for case_num in range(1, 4):
        results = run_test_case(prolog, case_num)
        print_test_results(results)
    
    print("All tests completed.\n")

if __name__ == "__main__":
    try:
        run_all_tests()
    except Exception as e:
        print(f"Error running tests: {e}")
        sys.exit(1) 