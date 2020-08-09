# 
# Highest Score
# 
# - Given a string of words, you need to find the highest scoring word.
# - Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# - You need to return the highest scoring word as a string.
# - If two words score the same, return the word that appears earliest in the original string.
# - All letters will be lowercase and all inputs will be valid.

def high(x):
    # Code here
    current_score = 0
    highest_score = 0
    winning_word = ''
    letters = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
        "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
        "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, 
        "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
        "z": 26
    }
    
    words = x.split(" ")
    for word in words:
        current_score = 0
        for letter in word: 
            current_score += letters[letter]
        if current_score > highest_score:
            highest_score = current_score
            winning_word = word
    # print("Score for %s is %s" %(word, current_score))
    # print("Winning word is %s" % winning_word)
    return winning_word
print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
