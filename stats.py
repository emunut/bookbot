# stats.py

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text:
        # Convert to lowercase for consistent counting
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars_by_count(char_dict):
    """
    Converts a character count dictionary into a sorted list of dictionaries.
    Skips non-alphabetical characters.
    """
    # Helper function to extract the 'num' key for sorting
    def sort_on(d):
        return d["num"]

    list_of_dicts = []
    for char, count in char_dict.items():
        # Skip non-alphabetical characters
        if char.isalpha():
            list_of_dicts.append({"char": char, "num": count})
    
    # Sort the list from greatest to least by the 'num' key
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    return list_of_dicts

