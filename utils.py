# Icons for different option types (emoji unicode for simplicity)
ICONS = {
    "location": "🗺️",
    "cost": "💰",
    "food": "🍽️",
    "seating": "💺",
    "closing_time": "⏰",
    "wifi": "📶",
    "noise": "🔊",
    "outlets": "🔌"
}

def get_attribute_from_question(question_idx):
    """Map question index to the corresponding Prolog attribute name"""
    attributes = [
        "location", "cost", "food", "seating", 
        "closing_time", "wifi", "noise", "outlets"
    ]
    return attributes[question_idx]

def format_option(option):
    """Format option text to be more human-readable"""
    # Extract the value part (before the parentheses if exists)
    value = option.split('(')[0].strip()
    # Get the description part (inside parentheses if exists)
    description = option[option.find('(')+1:option.find(')')] if '(' in option else ''
    
    # Format based on the type of option
    if 'very_close' in value:
        return f"Very Close ({description})"
    elif 'moderate_commute' in value:
        return f"Moderate Commute ({description})"
    elif 'coffee_only' in value:
        return f"Coffee Only ({description})"
    elif 'snacks_only' in value:
        return f"Snacks Only ({description})"
    elif 'full_menu' in value:
        return f"Full Menu ({description})"
    elif 'quiet_individual' in value:
        return f"Quiet Individual ({description})"
    elif 'shared_long_tables' in value:
        return f"Shared Long Tables"
    elif 'comfortable_lounge' in value:
        return f"Comfortable Lounge ({description})"
    elif 'outdoor_seating' in value:
        return f"Outdoor Seating"
    elif 'private_study_rooms' in value:
        return f"Private Study Rooms"
    elif 'closes_before_5pm' in value:
        return f"Before 5 PM"
    elif 'closes_before_8pm' in value:
        return f"Before 8 PM"
    elif 'closes_8_10pm' in value:
        return f"8 PM - 10 PM"
    elif 'open_until_midnight' in value:
        return f"Until Midnight"
    elif '24_hours' in value:
        return f"24 Hours"
    elif value == 'none':
        return "None"
    elif value == 'poor':
        return f"Poor ({description})"
    elif value == 'good':
        return f"Good ({description})"
    elif value == 'silent':
        return "Silent (library-quiet)"
    elif value == 'low':
        return "Low (soft background)"
    elif value == 'moderate':
        return "Moderate (normal cafe)"
    elif value == 'high':
        return "High (busy/crowded)"
    elif value == 'few':
        return "Few (scattered)"
    elif value == 'many':
        return "Many (multiple nearby)"
    elif value == 'every_seat':
        return "Every Seat (built-in)"
    else:
        return option 