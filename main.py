
# marksheet
# 5 subjects take input
# if > 90 = Excellent
# list = [multiple data types]
# tuple = (constant)
# dictionary = {key:value}
#
#











#Marksheet
# Marksheet using if-elif-and-arthmatic operations

sub1 = int(input("Enter Marks"))
sub2 = int(input("Enter Marks"))
sub3 = int(input("Enter Marks"))
sub4 = int(input("Enter Marks"))
sub5 = int(input("Enter Marks"))
sub6 = int(input("Enter Marks"))
sub7 = int(input("Enter Marks"))

totalmarks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7
percentage = (totalmarks/700)*100

if percentage >= 90 and percentage <= 100:
    print("A1-Grade")
elif percentage >= 80 and percentage < 90:
    print("A-Grade")
elif percentage >= 70 and percentage < 80:
    print("B-Grade")
elif percentage >= 60 and percentage < 70:
    print("C-Grade")
elif percentage >= 50 and percentage < 60:
    print("D-Grade")
elif percentage < 50 and percentage >= 0:
    print("Fail")


# Using Power..
x = 3**2  # using as power value after 2 stars will be considered as power.
print(x)  # Output (3*3) = 9
x = 3**6
print(x)  # Output (3*3*3*3*3*3)= 729


#Backslash     \n(Space sensitive after this.)
print("Hunain \nSurahio")
Nested if(Two Ways)
age = int(input("Enter age : "))
gender = input("Enter Gender : ")

# Way 1:
if age > 18 and (gender == "male" or gender == "female"):
    print("Allow")
else:
    print("Do not allow")

# Way 2:
if age > 18:
    if gender == "male":
        print("Allow")
    elif gender == "female":
        print("Allow")
    else:
        print("Do not Allow")


# camel case(hunainMunir)   Extra Knowledge

arr = ['Hunain', 'Aman', 'Wasiq', 'wasay', 18]
print(arr[0]) #print the list through index
print(arr) #printing full list

#function of append is used to add something.
arr.append("Kashif")
print(arr)

# To insert something into a desire index.

arr.insert(4, "Asshad")
print(arr)

#                           Slicing
if u want to extract some part of the list into another list
arr2 = arr[0:3]  # 0 to 3-1 = 0,1,2
print("Trio : ")
print(arr2)

# delete through index
del arr[4]
print("Deletion")
print(arr)

# remove through the value
arr.remove(18)
print("After removing")
print(arr)

# last value removing
arr.pop(2)     # which element you want to pop(2) second element will be popped out
print(arr)

# To change the value in a list
arr[4] = "Awais"
print(arr)


# Tupples = immutable (Once it created it can not update, delete, insert etc)
# used for constant elements.
# whole tupple can be deleted.
# tupples can be used as 2d array

# we use round brackets in tupples
# or we can write multiple elements without round brackets it can also be tupple

a = (12,43,21,65)  #tupple
print(a)
b = 1,2,3,4        #tupple
print(b)
c = (12,)
print(c)           #tupple
d = 12,
print(d)           #tupple
del d              #tupple of 'd' is deleted

# tupple as 2d array
d = ((1,2,3,4,5),("a","b","c","d","e"))
print(d)

# For Loops (mainly used to traverse list, dictionaries)

# for in Loop(majorly targeting lists)
lst = [1,2,3,4,5,6,7,8,9]
for i in lst:       # 4 spaces py jo bhi hoga for loop ka hissa hoga
    print(i)

# printing index of the list or length of the list
for i in range(len(lst)):
    print(i)       #It will print the length of the list.
    print(lst[i])  #It will print the values of the list.

# nested for loop

a = [1,2,3,4,5,6]
b = [4,5,6,7,8,9]
c = []
#
for i in a:
    for j in b:
        if (i == j):
            c.append(i)
print(c)

a = [1,2,3,4,5,6]
b = [4,5,6,7,8,9]
c = []

for i in range(len(a)):
    for j in range(len(b)):
        if(a[i] == b[j]):
            c.append(a[i])
print(c)

# uppercase / lowercase / title

name = "Hunain Munir Surahio"
print(name.upper())
print(name.lower())
print(name.title())


# List Comprehension

# It will shorten the line of code
# syntax
# expression for var in itterator
# here expression means what to do.

h = [letter for letter in "hunain"]
print(h)

f = [num*2 for num in range(1,11)]
print(f)

k = [num for num in range(1,1001) if num % 8==0]
print(k)

f = [x for x in range(1,21) if x%2==0]
print(f)

# List comprehension by taking input

x = int(input("Enter number"))
h = [i*x for i in range(1,11)]
print(h)

# Transpose
matrix = [[1,2,3,4],[5,6,7,8]]
transpose = []
for i in range(len(matrix[0])):
    row = []
    for j in matrix:
        row.append(j[i])
        transpose.append(row)
print(transpose)


matrix = [[1,2,3,4],[5,6,7,8]]
transpose = [[row[i] for row in matrix]for i in range(len(matrix[0]))]
print(transpose)

# ----------------------------------------------------------------------------------------------------------------------
# Practice problems of list comprehension.

# Find all of the numbers from 1-1000 that are divisible by 7
A = [num for num in range(1,1001) if num%7==0]
print(A)


# Find all of the numbers from 1-1000 that have a 3 in them
three = [i for i in range(1,1001) if '3' in str(i)]
print(three)


# Count the number of spaces in a string
spc = [i for i in "Hunain Munir Surahio" if ' ' in i]
print(len(spc))


# Create a list of all the vowels in the string “Yellow Yaks like yelling and yawning and yesturday they yodled
# while eating yuky yams”

lst = ["Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"]
vowels = [i for i in lst if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or
              i == "O" or i == "u" or i == "U"]
print(vowels)


# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled
# while eating yuky yams”

lst = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonants = [i for i in lst if i not in 'a,e,i,o,u, " "']
print(consonants)

# ----------------------------------------------------------------------------------------------------------------------

# Dictionaries (Key and the value)
# Example Phone Book directory Name(key) number(Value)
# Syntax

# Way 1:
a = {'Hunain' : "03019384060"}
print(type(a))
print(a)

# Way 2: Through Constructor
a = dict([(1,'Hunain'),(2,'Aman'),(3,'Wasiq')])
print(a)

a = {
    'a':"apple",
    'b':"onion",
    'c':"Car",
    'D':"Bike"

print(a.get('f',"Not Found"))

# Traversing Keys :
for i in a.keys():
    print(i)

# Traversing Values :
for i in a.values():
    print(i)

# Traversing Keys & Values :
for i in a.keys(),a.values():
    print(i)

# Traversing Keys & Values :
for key, value in a.items():
    print(key,value)

# Update the value in dictionary :
H = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd'}
H[2] = 'B'
print(H)

# Insert the value in dictionary :
H = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd'}
H[4] = 'e'
print(H)

# Delete the value from the dictionary :
# There are three ways to delete :
# way 1 : pop function : It will return once and pop out from the dictionary
H = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd'}
print(H.pop(4))
print(H)

# way 2 : clear : It will clear all the items but dictionary will be there.
H = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd'}
H.clear()
print(H)

# Way 3 : del : It wil completely delete the items with the dictionary.
H = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd'}
del H
print(H) #it will give error that dictionary does'nt exists.


# List to Dictionaries:
# There are Two ways to convert list into dictionaries

# Way 1 : Through for Loop
List1 = [1,2,3,4,5,6,7] # Keys
List2 = ['a','b','c','d','e','f','g'] # Values
result = {}
#
# for key in List1:
for value in List2:
    result[key] = value
    List2.remove(value)
    break
print(result)

# Way 2 : Through dict(ZIP) Zip is used to combine
#           corrosponding values.

List1 = [1,2,3,4,5,6,7] # Keys
List2 = ['a','b','c','d','e','f','g'] # Values
result = {}
result = dict(zip(List1,List2))
print(result)


# # Question: Number of Phone numbers to be added
# #           Take name and number
# #           add it to the dictionary

a = int(input("Enter Number Of Names and Numbers You want to add : "))
list1 = []
list2 = []
for i in range(a):
    name = input("Enter Name : ")
    list1.append(name)
    number = input("Enter Number : ")
    list2.append(number)

PhoneBook_Directory = {}
PhoneBook_Directory = dict(zip(list1,list2))
print(PhoneBook_Directory)



# Functions : used for repition purpose :

# def is used to start function

# Example 1 :

def sum(a,b):    # Here a and b are the parameters of the function
    c = a+b
    print(c)
    we can also use return here but we have to print that when calling
    return a+b

sum(10,11)       # Here 10 and 11 are the arguments
print(sum(1,1))

# Classes
# Defined functions inside class are methods
# __init__ is known as constructor

class Employee:
    def __init__(self,first_name,last_name):  #here constructor is used to run first then others.
        self.fn = first_name
        self.ln = last_name

    def display_employee(self):
        print(f"Name : {self.fn} {self.ln} ")

emp1 = Employee("Hunain","Munir")
emp2 = Employee("Aman","Kumar")
emp1.display_employee()
emp2.display_employee()


# import datetime
now = datetime.datetime.now()
print("Current date & time is : ")
print(now.strftime("%d-%m-%y %H:%M"))


def dstnct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
print(dstnct([1,2,3,4,5,6]))
print(dstnct([1,2,3,4,5,5,6,7,8]))

# import random
char_list = ['A','E','I','O','U']
random.shuffle(char_list)
print(char_list)            # Shuffle but print as list
print(" ".join(char_list))  # Shuffle and will join the alphabets


n = 18
a = int(input("Guess the number : "))
if a < n:
    print("Guess a bit Higher")
    a = int(input("Guess the number : "))
elif a > n:
    print("Guess a bit Lower")
    a = int(input("Guess the number : "))
elif a == n:
    print("Guess is Perfect!!!")
































