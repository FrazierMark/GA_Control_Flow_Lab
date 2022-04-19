# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
# each term of the sequence (beyond 0 and 1) is a function of the preceding terms.

def fibFifty():
    num0 = 0
    num1 = 1
    terms = 2

    print(f'term: 0 / number: {num0}')
    print(f'term: 1 / number: {num1}')

    while terms < 50:
        print(f'term: {terms} / number: {num0 + num1}')
        num0 = num1
        num1 = num0 + num1
        terms += 1

fibFifty()