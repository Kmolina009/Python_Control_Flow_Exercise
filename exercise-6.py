# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
monthDays ={
    "Jan": 31
}
print(monthDays)
Winter = ["Jan","Feb","Dec"]
Spring = ["Mar","Apr","May"]
Summer = ["Jun","Jul","Aug"]
Fall = ["Sept","Oct","Nov"]

months = ["Jan","Feb","Dec","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov"]

month = input("What month were you born in?")
print(month)
while month not in months:
	month = input("What month were you born in?")
  
day = input("What day of were you born in?")
day = int(day)

while day > 0 and day <= monthDays[day]:
	day = int(input("What day of were you born in?"))
season = ""

#Note to self, conditionals CAN NOT BE STORED in a variable.

if (month == "Dec" and day >= 21) or (month == "Jan") or (month == "Feb") or (month == "Mar" and day <= 19):	
	season = "Winter"
if (month == "Mar" and day >= 20) or (month == "April") or (month == "May") or (month == "Jun" and day <= 20):
	season = "Spring"
if (month == "Jun" and day >= 21) or (month == "Jul") or (month == "Aug") or (month == "Sep" and day <= 21):
	season = "Summer"
if (month == "Sep" and day >= 22) or (month == "Oct") or (month == "Nov") or (month == "Dec" and day <= 20):
	season = "Fall"

print("{} {} is in {}".format(month, day, season))
