# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:

# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length

# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

aSide = input("Enter the length of a triangle:")
bSide = input("Enter the length of a triangle:")
cSide = input("Enter the length of a triangle:")

def calculateTriangleType(a, b, c):
    if a == b and b == c and a == c:
        return "equalateral"
    elif a != b and b != c and c != a:
        return "scalene"
    else:
        return "isosceles"

print(
    f"A triangle with sides of {aSide}, {bSide}, and {cSide} is a {calculateTriangleType(aSide, bSide, cSide)} triangle")
