def count_vowels(word):
    return sum(1 for c in word.lower() if c in 'aeiou')

def count_letters(word):
    return len([c for c in word if c.isalpha()])
