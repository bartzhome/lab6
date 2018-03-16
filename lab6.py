"""
this is a doc string

Now I will run blah:

>>> someMaths(434342343243)
1

>>> dayOfWeek(6)
'Saturday'

>>> dayOfWeek(1)
'Monday'


# trace main routine (scope) - Global
studentNumber | 000033686
calculatedNumber | 5
dayOne | 'Friday'
dayTwo | 'Monday'


# trace someMaths (scope)
aNumber | 000033686
newNumber | 33, 5

# trace dayOfWeek (scope)
dayNumber | 5
dayString | 'Friday'


# trace daysFrom (scope)
oldDayNumber | 5
howManyDays| 3
nextDay | 1
dayString | 'Monday'

# trace dayOfWeek (scope 2)
dayNumber | 1
dayString | 'Monday'


"""
import math


def some_maths(a_number):
    new_number = a_number // 1000
    new_number = new_number % 7
    return new_number

def someMaths( aNumber ):
    newNumber = aNumber // 1000
    newNumber = newNumber % 7
    return newNumber


def day_of_week(day_number):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    import pdb; pdb.set_trace()
    if day_number not in range(0, len(days)):
        return -1

    return days[day_number]


def dayOfWeek(day_number):
    import pdb;
    pdb.set_trace()
    if day_number == 0:
        dayString = "Sunday"
    elif day_number == 1:
        dayString = "Monday"
    elif day_number == 2:
        dayString = "Tuesday"
    elif day_number == 3:
        dayString = "Wednesday"
    elif day_number == 4:
        dayString = "Thursday"
    elif day_number == 5:
        dayString = "Friday"
    elif day_number == 6:
        dayString = "Saturday"
    return dayString


def daysFrom(oldDayNumber, howManyDays):
    nextDay = (oldDayNumber + howManyDays) % 7
    dayString = dayOfWeek(nextDay)
    return dayString

#
# # global scope
#
# studentNumber = int(input("Please enter your student number: "))
# calculatedNumber = someMaths(studentNumber)
#
# print(calculatedNumber)
#
# dayOne = dayOfWeek(calculatedNumber)
# print("The day of the week with that number is " + dayOne + ".")
#
# dayTwo = daysFrom(calculatedNumber, 3)
# print("3 days after it will be " + dayTwo + ".")
#
# # # if __name__ == "__main__":
# # import doctest
# # doctest.testmod()


def is_triple(a, b, c):
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return True
    return False

print(is_triple(3, 5, 4))



# print(math.pow(2, 4))
