# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

dogAge= input("Enter your Dog's age")
if int(dogAge) <= 2:
    print(f"The dog's age in dog years is {int(dogAge) * 10}")
else:
    print(f"The dog's age is dog years is {20 + ((int(dogAge) - 2 ) * 7)}")

         