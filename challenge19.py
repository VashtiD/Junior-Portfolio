def has_no_e(word):
    for letter in word:
        if letter.lower() == 'e':
            return False
    return True

def filter_words_without_e(words):
    no_e_words = []
    for word in words:
        if has_no_e(word):
            no_e_words.append(word)
    return no_e_words

def calculate_percentage(total_words, no_e_words):
    total_count = len(total_words)
    no_e_count = len(no_e_words)
    if total_count == 0:
        percentage = 0.0
    else:
        percentage = (no_e_count / total_count) * 100
    return percentage

words = "apple", "banana", "grape", "kiwi", "orange", "plumb", "cherry", "fig", "pear"
no_e_words = filter_words_without_e(words)
print("Words without 'e':", no_e_words)
percentage = calculate_percentage(words, no_e_words)
print(f"Percentage of words without 'e': {percentage:.2f}%")
