def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True

forbidden_letters = input("Enter a string of forbidden letters: ")
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon"]

count = 0
for word in words:
    if avoids(word, forbidden_letters):
        count += 1

print(f"The number of words that do not contain any of the forbidden letters is: {count}")
