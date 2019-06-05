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
a = input("input triangle sides a")
b = input("input triangle sides b")
c = input("input triangle sides c")
if int(a) == int(b) == int(c):
    print("This is an equalateral triangle")
elif int(a) != int(b) != int(c):
    print("This is an scalene triangle")
else:
    print("This is an isosceles triangle")