# Vashti Dalchand
# Date: 4/9/25
# challenge 21 Python
# Description: Check if a word contains only specified allowed letters.

def uses_only(word, allowed_letters):
    for letter in word:
        if letter not in allowed_letters:
            return False
    return True

print(uses_only("hello", "abcdehlo"))
print(uses_only("hello", "abcde"))
print(uses_only("a chef of aloha", "acefhl"))
print(uses_only("hello", "helo"))
print(uses_only("world", "abcde"))
