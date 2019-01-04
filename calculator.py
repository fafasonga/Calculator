import calendar

def addition(x, y):
    return x + y


def substraction(x, y):
    return x - y


def division(x, y):
    if y > x:
        return y / x
    else:
        return x / y


def multiply(x, y):
    return x * y


def lcm(x, y):
    ''' smallest positive integer that is perfectly divisible
    by the two given numbers '''

    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if(greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


def gcm(x, y):
    ''' This function implements the Euclidian Algorithm
   to find G.C.D. of two numbers '''

    if x < y:
        smaller = x
    else:
        smaller = y

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            gcm = i

    return gcm


def recur_factorial(n):
    ''' The factorial of a number is the product of all the integers from 1 to that number,
     Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1 '''

    if n == 1:
        return n
    else:
        fact = n * recur_factorial(n-1)
        return fact


print("\n*** List of Operations ***")
print("\n 1 for Addition\n 2 for Substraction\n 3 for Division\n 4 for Multiplication\n 5 for Least Common Multiple"
      "\n 6 for Least Common Multiple\n 7 for Prime Number\n 8 for Fibonacci Series\n 9 for ASCII"
      "\n 10 for Factorial\n 11 Check if Leap Year\n 12 Find Armstrong Number"
      "\n 13 Converting to Decimal, Binary, Octal and Hexadecimal\n 14 Converting Celsius and Fahrenheit"
      "\n 15 Convert Kilometers to Miles\n 16 Display given month of Calendar"
      "\n 17 Calculate Number of Days between dates\n 18 Discount Percentage calculator \n\n")

choice = input(" Select Operation: ")

if choice == '1':
    x = int(input("\nEnter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x, " + ", y, " = ", addition(x, y))

elif choice == '2':
    x = int(input("\nEnter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x, " - ", y, " = ", substraction(x, y))

elif choice == '3':
    x = int(input("\nEnter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x, " / ", y, " = ", division(x, y))

elif choice == '4':
    x = int(input("\nEnter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x, " * ", y, " = ", multiply(x, y))

elif choice == '5':
    x = int(input("\nEnter First Number: "))
    y = int(input("Enter Second Number: "))
    print("The L.C.M. of", x, "and", y, "is", lcm(x, y))

elif choice == '6':
    x = int(input("\nEnter First Number: "))
    y = int(input("Enter Second Number: "))
    print("The G.C.M. of", x, "and", y, "is", gcm(x, y))

elif choice == '7':
    x = int(input("\nEnter First Number: "))
    y = int(input("Enter Last Number: "))
    ''' Program to print all the Prime Numbers within an Interval '''

    print("\nPrime numbers between", x, "and", y, "are: ")
    for num in range(x, y + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

elif choice == '8':
    ''' Program to  the Prime Numbers within an Interval '''
    nterms = int(input("\nEnter Numbers to be Displayed: "))

    # First two numbers
    n1 = 0
    n2 = 1
    count = 0

    # Check if the Numbers of terms are valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence upto", nterms, ":")
        while count < nterms:
            print(n1, end=' , ')
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

elif choice == '9':
    ''' ASCII stands for American Standard Code for Information Interchange
     It is a numeric value given to different characters and symbols, 
     for computers to store and manipulate. For example: ASCII value of the letter 'A' is 65.'''

    char = input("\nEnter a digit or character: ")
    if char.isdigit():
        print("\nThe ASCII value of '" + char + "' is", chr(int(char)))
    else:
        print("\nThe ASCII value of '" + char + "' is", ord(char))

elif choice == '10':
    num = int(input("\nEnter a number: "))

    if num < 0:
        print("\nSorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("\nThe factorial of 0 is 1")
    else:
        print("\nThe factorial of", num, "is", recur_factorial(num))

elif choice == '11':
    ''' Program to check if the input year is a leap year or not,
     A leap year is exactly divisible by 4 except for century years (years ending with 00). 
     The century year is a leap year only if it is perfectly divisible by 400 '''

    year = int(input("\nEnter a year: "))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("\n{0} is a leap year".format(year))
            else:
                print("\n{0} is not a leap year".format(year))
        else:
            print("\n{0} is a leap year".format(year))
    else:
        print("\n{0} is not a leap year".format(year))

elif choice == '12':
    ''' A positive integer is called an Armstrong number of order n if abcd... = an + bn + cn + dn + ...,
     For example: 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number '''

    lower = int(input("\nEnter Lower Range: "))
    upper = int(input("Enter Upper Range: "))

    for num in range(lower, upper + 1):

        # order of number
        order = len(str(num))

        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)

elif choice == '13':

    dec = input("\nEnter Number: ")
    print("Entered Number is: ", dec, "\nIn binary is: ", bin(dec), "\nIn octal is: ", oct(dec),
          "\nIn hexadecimal is: ", hex(dec))

elif choice == '14':
    ''' Convert Celsius and Fahrenheit, celsius * 1.8 = fahrenheit - 32 '''

    print("\n*** List of Temperature Unit ***")
    print("\n 1 for Degree Celsius\n 2 for Degree Fahrenheit\n ")

    ch = input("\nEnter your Choice: ")

    if ch == '1':
        celsius = input("\nEnter Temperature in Celsius: ")
        # celsius = 37.5

        fahrenheit = (float(celsius) * 1.8) + 32
        print('\n%0.3f degree Celsius is equal to %0.3f degree Fahrenheit' % (float(celsius), float(fahrenheit)))

    elif ch == '2':
        fahrenheit = input("\nEnter Temperature in Celsius: ")
        # fahrenheit = 99.5

        celsius = (float(fahrenheit) - 32) / 1.8
        print('\n%0.3f degree Fahrenheit is equal to %0.3f degree Celsius' % (float(fahrenheit), float(celsius)))

    else:
        print("Invalid Input")

elif choice == '15':
    ''' Convert Kilometers to Miles, kilometers = miles / conv_fac '''

    print("\n*** List of Units ***")
    print("\n 1 for Kilometers\n 2 for Miles\n ")

    choi = input("\nEnter your Choice: ")
    if choi == '1':
        kilometers = float(input("Enter value in kilometers: "))
#         kilometers = 5.5

        # conversion factor
        conv_fac = 0.621371

        # calculate miles
        miles = kilometers * conv_fac
        print('%0.3f kilometers is equal to %0.3f miles' % (float(kilometers), float(miles)))

    elif choi == '2':
        miles = float(input("Enter value in kilometers: "))
#         miles = 3.418

        # conversion factor
        conv_fac = 0.621371

        # calculate miles
        kilometers = miles / conv_fac
        print('%0.3f Miles is equal to %0.3f Kilometers' % (float(miles), float(kilometers)))

    else:
        print("Invalid Input")

elif choice == '16':
    # yy = 2018
    # mm = 12

    # To ask month and year from the user
    yy = int(input("\nEnter year: "))
    mm = int(input("Enter month: "))

    # display the calendar
    print("\n", calendar.month(yy, mm))

elif choice == '17':
    print("\nPlease Enter highest date by the requested order :")
    x = input("Please Enter the Year: ")
    y = input("Please Enter the Month: ")
    z = input("Please Enter the Day: ")
    st_date = [str(z + "." + y + "." + x)]
    print("Your Date is: " + str(st_date))

    print("\nPlease Enter a 2nd date by the same order: ")
    a = input("Please Enter the Year: ")
    b = input("Please Enter the Month: ")
    c = input("Please Enter the Day: ")
    nd_date = [str(c + "." + b + "." + a)]
    print("Your Date is: " + str(nd_date))

    maths = int(x) * 365 + int(y) * 12 + int(z)
    mathss = int(a) * 365 + int(b) * 12 + int(c)
    result = int(maths - mathss)
    print("\nNumber of Days between", str(st_date), "and", str(nd_date), "is", result)

elif choice == '18':
    print("\n*** List of Operations ***")
    print("\n 1 To Calculate The Discount Price\n 2 To Calculate the Discount Percentage \n ")

    chois = input("\nEnter your Choice: ")
    if chois == '1':
        orig_amount = float(input("\nPlease Enter Original Price: "))
        disc_perc = float(input("Please Enter Discount Percentage: "))

        conv = float(disc_perc / 100)
        disc_rate = float(orig_amount * conv)

        disc_value = orig_amount - disc_rate

        print("\nThe Original Price is = ", orig_amount, "\nThe Percentage rate Discount is = ", disc_perc, "%",
              "\nSales Price after Discount = ", disc_value, "\nYou Saved = ", disc_rate)
    elif chois == '2':
        orig_amount = float(input("\nPlease Enter Original Price: "))
        disc_rate = float(input("Please Enter Discounted Price: "))

        result = float((1 - float(disc_rate / orig_amount)) * 100)
        print("\nThe Original Price is = ", orig_amount, "\nThe Discounted Price is = ", disc_rate,
              "\nThe Discount Percentage is = ", result, "%")
    else:
        print("Invalid Input")

else:
    print("Invalid Input")
