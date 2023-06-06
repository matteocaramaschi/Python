# Parameterless function
def message():
	print("A message")
	
message()

# Parameterized function
def intro(a="James Bond", b="Bond"):
     print("My name is", b + ".", a + ".")
 
intro()

# Function with default parameters
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")
 
intro("Susan")

# Function with a list as parameter
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

# Leap/Normal year
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
		
# How many days in couple year/month
def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if is_year_leap(year):
            return 29
        else:
            return 28

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Days in a year
def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))

# Find the prime numbers along the first 20 numbers
def is_prime(num):
    if(num <= 1): return False
    
    prime = True
    divide = 2
    while(divide <= num):
        if(num % divide == 0 and num != divide):
            prime = False
            break
        divide += 1
    return prime

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# Litre/100km to mpg conversion
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

print("Litres/100km to miles/gallon and vice versa")
def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

print("Test editing lists in functions")
def my_list_func(my_list):
	my_list[0] = 3
	
my_list_2 = [2,5]
my_list_func(my_list_2)
print(my_list_2)

# BMI
print("Calculating BMI with support functions")

# Conversion from ft a/o inch to meters
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
# Conversion lb to kg
def lb_to_kg(lb):
    return lb * 0.4535923
 
# BMI calculation
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2

print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

# Triangles
print("Triangles operations")

# Check if is a triangle (sum of two sides greater than third side)
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

# Check if is a right triangle (sum of two sides to the power of two equal to hypotenuse to the power of two (longest side)
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

# Fibonacci without recursion

print("Fibonacci without recursion")
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10): # testing
    print(n, "->", fib(n))
	
# Fibonacci with recursion

print("Fibonacci with recursion")
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
	
for n in range(1, 10): # testing
    print(n, "->", fib(n))
