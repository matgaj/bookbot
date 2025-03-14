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

def sort_char_by_num_appearance(char_appearances):
    sorted_char_appearance = []
    for k in char_appearances:
        char_stats = {}
        char_stats["char"] = k
        char_stats["num"] = char_appearances[k]
        sorted_char_appearance.append(char_stats)
        sorted_char_appearance.sort(reverse=True, key=lambda x: x["num"])
    return sorted_char_appearance