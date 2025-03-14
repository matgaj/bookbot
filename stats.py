def count_words(text):
    words = text.split()
    return len(words)

def count_char_appearances(text):
    text = text.lower()
    num_appearances = {}
    for char in text:
        if char in num_appearances:
            num_appearances[char] += 1
        else:
            num_appearances[char] = 1
    return num_appearances