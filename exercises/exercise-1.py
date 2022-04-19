# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 

# 2. Write the code that determines whether the letter entered is a vowel

# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':d


alphaInput = input("Please enter a letter from the alphabet (a-z or A-Z):")


def isVowel(string):
    vowels = ['a', 'A', 'e', 'E' 'i', 'I', 'o', 'O', 'u', 'U']
    for c in string:
        if c not in vowels:
            return False
        else:
            return True

if isVowel(alphaInput):
    print(f'The letter {alphaInput} is a vowel')
else:
    print(f'The letter {alphaInput} is a consonant')
