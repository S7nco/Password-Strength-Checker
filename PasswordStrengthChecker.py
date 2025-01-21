# Password Strength Checker

# Define Password Strength Criteria
# At Least 15 characters
# Contains Upper and Lower case letters
# Contains special characters and numbers

# Pseudocode
# Get User Input
# Compare to Criteria
# Score Range depending on Criteria that are met
# Optional: Provide Feedback

# Later Improvements
# Graphical GUI
# API Implementation for Database Breaches

import re #Regular Expressions

def PassStrenCheck(password):
    #Criteria
    LengthCriteria = len(password) >= 15
    #print(f"LengthCriteria: {LengthCriteria}")
    UpperCriteria = bool(re.search(r'[A-Z]', password))
    #print(f"UpperCriteria: {UpperCriteria}")
    LowerCriteria = bool(re.search(r'[a-z]', password))
    #print(f"LowerCriteria: {LowerCriteria}")
    SpecialCriteria = bool(re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/-]', password))
    #print(f"SpecialCritiera: {SpecialCriteria}")
    NumberCriteria = bool(re.search(r'\d', password))
    #print(f"NumberCriteria: {NumberCriteria}")

    #Score Password and Provide Feedback on missing criteria
    score = 0
    feedback = [] 

    if LengthCriteria: 
        score +=1
        #print("LengthCriteria passed, score incremented.")
    else: 
        feedback.append("Password does not meet length requirement.\n")
    if UpperCriteria: 
        score +=1
        #print("UpperCriteria passed, score incremented.")
    else: 
        feedback.append("Password does not meet Uppercase Letter requirement.\n")
    if LowerCriteria: 
        score +=1
        #print("LowerCriteria passed, score incremented.")
    else:
        feedback.append("Password does not meet Lowercase Letter requirement.\n")
    if SpecialCriteria: 
        score +=1
        #print("SpecialCriteria passed, score incremented.")
    else:
        feedback.append("Password does not meet Special Character requirement.\n")
    if NumberCriteria: 
        score +=1
        #print("NumberCriteria passed, score incremented.")
    else:
        feedback.append("Password does not meet Number requirement.\n")
    
    #Rank Password
    if score == 5:
        feedback.append("Great Password\n")
    elif score >= 3 or score > 5:
        feedback.append("Average Password\n")
    elif score < 3:
        feedback.append("Bad Password\n")
    
   # print(f"Debug Final Score: {score}") # Confirm the score calculation
    return {"score": score, "feedback": feedback}


# Main Program
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    result = PassStrenCheck(user_password)
    print("Feedback:")
    print("".join(result["feedback"]).rstrip())
    print("Score: " + str(result["score"]))
    






