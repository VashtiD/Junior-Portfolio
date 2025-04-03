#Vashti Dalchand
#Period 1-2
#April 2nd, 2025



# Function to return the first letter of the word
# This function takes a string and returns the first character of the string.
def first_letter(word):
    return word[0] if word else ""

# Function to return the last letter of the word
# This function takes a string and returns the last character of the string.
def last_letter(word):
    return word[-1] if word else ""

# Function to return the middle part of the word
# This function takes a string and returns the substring that excludes the first and last characters.
def middle_part(word):
    return word[1:-1] if len(word) > 2 else ""

# Function to check if a word is a palindrome
# This function recursively checks if a word is a palindrome.
# Base case: If the word is empty or has one letter, it is considered a palindrome.
# Recursive case: The function compares the first and last letters of the word.
# If they match, it recursively checks if the middle part of the word is also a palindrome.
# If the first and last letters don't match, the word is not a palindrome.
def is_palindrome(word):
    if len(word) <= 1:  # Base case
        return True
    if word[0] == word[-1]:  # Comparing first and last letters
        return is_palindrome(middle_part(word))  # Recursive case
    return False  # Not a palindrome

# Test cases
# These tests are used to verify that the is_palindrome function works correctly:
# - The first test checks if "noon" is a palindrome (expected output: True).
# - The second test checks if "redivider" is a palindrome (expected output: True).
# - The third test checks if "hello" is a palindrome (expected output: False).
# - The fourth test checks if a single letter "a" is a palindrome (expected output: True).
# - The fifth test checks if an empty string is a palindrome (expected output: True).
def run_tests():
    test_cases = ["noon", "redivider", "hello", "a", ""]
    expected_outputs = [True, True, False, True, True]
    
    for test, expected in zip(test_cases, expected_outputs):
        result = is_palindrome(test)
        print(f"Testing '{test}': Expected {expected}, Got {result}")

if __name__ == "__main__":
    run_tests()  # Start the tests
