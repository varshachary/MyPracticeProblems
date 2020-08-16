"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""
#hackerrank
def minion_game(string):
    # your code goes here
    vowel='AEIOU'
    stuart=0
    kevin=0
    for index in range(len(string)):
        if string[index] in vowel:
            kevin+=len(string)-index
        else:
            stuart+=len(string)-index
    if stuart > kevin:
        print("Stuart",stuart)
    elif kevin >stuart:
        print("Kevin",kevin)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
