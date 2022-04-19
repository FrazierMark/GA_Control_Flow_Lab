# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):


# 2. Then prompts the user to enter the input_day of the month:
#      Enter the input_day of the month:


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
# the input_day number falls within a certain range.


input_month = input('Enter the month of the year (Jan - Dec):')

input_day = int(input('Enter the day of the month:'))

winter = {'Dec': 21, 'Jan': 0, 'Feb': 0, 'Mar': 19}
spring = {'Mar': 20, 'Apr': 0, 'May': 0, 'Jun': 20}
summer = {'Jun': 21, 'Jul': 0, 'Aug': 0, 'Sep': 21}
fall = {'Sep': 22, 'Oct': 0, 'Nov': 0, 'Dec': 20}

def checkSeason(month, day):
    season = ''
    if input_month in winter.keys():
        season = winter
        if (input_month == 'Dec' and input_day >= winter['Dec']) or (input_month == 'Mar' and input_day <= winter['Mar']):
            return 'winter'

    if input_month in spring.keys():
        season = 'spring'
        if (input_month == 'Mar' and input_day >= spring['Mar']) or (input_month == 'Jun' and input_day <= spring['Jun']):
            return 'spring'

    if input_month in summer.keys():
        season = 'summer'
        if (input_month == 'Jun' and input_day >= summer['Jun']) or (input_month == 'Jun' and input_day <= summer['Sep']):
            return 'summer'

    if input_month in fall.keys():
        season = 'fall'
        if (input_month == 'Sep' and input_day >= fall['Sep']) or (input_month == "Dec" and input_day <= fall['Dec']):
            return 'fall'
    return season

print(f'The season of {input_month} {input_day} is {checkSeason(input_month, input_day)}')
