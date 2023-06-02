# Becoming familiar with lists

print("Lists")
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Enter the middle number: "))

# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)

print("Test lists methods")
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
print("Creating lists with FOR")
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

print("Use of LENGTH in FOR loop")
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

print("Better use of FOR loop through a list")
my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)

print("Swap elements in list")
my_list = [10, 1, 8, 3, 5]
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)

print("Beatles lineup")
# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(input("Add member: "))
print("Step 3:", beatles)

# step 4
del beatles[4]
del beatles[3]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list length
print("The Fab", len(beatles))

print("Accessing elements in lists of lists")
my_list = [1, 'a', ["list", 64, [0, 1], False]]
print(my_list[2][2][1])

print("Mechanical bubble sort")
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

print("Python sort")
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

print("List copy")

# Copying the entire list
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# IN / NOT IN
print("Query the list")
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

# Largest element
print("Largest element in a list")

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)

# Lottery
print("Lottery hits")
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)

# Remove duplicates in list
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp_list = []
temp_list.append(my_list[0])

for i in range(1, len(my_list)):
    if my_list[i] not in my_list[:i]:
        temp_list.append(my_list[i])

my_list = temp_list[:]
print("The list with unique elements only:")
print(my_list)

# List comprehension

# Produces a ten-element list filled with squares of ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
squares = [x ** 2 for x in range(10)]
 
# Creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)
twos = [2 ** i for i in range(8)]

# Makes a list with only the odd elements of the squares list.
odds = [x for x in squares if x % 2 != 0 ]

# Creates a chessboard with a few elements (matrix)
board = [["" for i in range(8)] for j in range(8)]
board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"
board[4][2] = "KNIGHT"
board[3][4] = "PAWN"

print(board)