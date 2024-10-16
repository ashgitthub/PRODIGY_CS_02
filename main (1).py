import re  # Importing the re module for regular expression handling

def assess_password_strength(password):
    # Define the criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Check how many criteria are met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    # Assess strength based on the number of criteria met
    if criteria_met == 5:
        strength = "Strong"
    elif 3 <= criteria_met < 5:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Provide feedback on what is missing
    feedback = []
    if not length_criteria:
        feedback.append("Password must be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")
    
    # Output the result
    result = {
        "strength": strength,
        "feedback": feedback if feedback else ["Password is strong."]
    }
    
    return result

# Take password input from the user
password = input("Enter a password to assess its strength: ")

# Assess the password
assessment = assess_password_strength(password)

# Output the results
print("\nPassword Strength:", assessment["strength"])
print("Feedback:")
for fb in assessment["feedback"]:
    print("-", fb)
