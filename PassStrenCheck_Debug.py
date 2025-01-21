import re

def test_special_characters(password):
    match = re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/-]', password)
    return match.group() if match else None

# Test cases
print(test_special_characters("Q")) #Should return none
print(test_special_characters("12345")) #Should return none
print(test_special_characters("!@#$")) #Should return a match