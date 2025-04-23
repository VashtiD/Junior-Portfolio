#Vashti Dalchand
#April 23, 2025
#Period 1-2
#Python Challenge 23



def is_abecedarian(word):
    # Compare the original word to its sorted version
    return list(word) == sorted(word)

# Test the function with a few examples
words_to_test = ["abc", "aegilops", "art", "loop", "banana"]

for word in words_to_test:
    result = is_abecedarian(word)
    print(f"{word}: {result}")

# Challenge: Count how many abecedarian words exist
word_list = ["abc", "aegilops", "art", "loop", "banana", "a", "b", "c", "de", "ee", "ff", "ghi", "mnop"]
abecedarian_count = sum(1 for word in word_list if is_abecedarian(word))

print(f"Total abecedarian words: {abecedarian_count}")
