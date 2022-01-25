#1. Write a Python function to find the Max of three numbers
def high():
    count = 0
    Highest = 0
    while count != 3:
        HNum = int(input("Please Enter a Number: "))
        if HNum > Highest:
            Highest = HNum
            count = count +1
        else:
             count = count +1
    return Highest

print("This app finds the highest of 3 numbers entered")
print ("The Highest Number entered was: " + str(high()))

#2. Write a Python function to sum all the numbers in a list
def addf():
    total = sum(w3list)
    return total

w3list = [8, 2, 3, 0, 7]
print (w3list)
print ("The total of the list: " + "is "+  str(addf()))

#3. Write a Python function to multiply all the numbers in a list
def multi():
    total2 = 1
    for i in w3list2:
        total2 = total2 * i
    return total2

w3list2 = [8, 2, 3, -1, 7]

print (w3list2)
print ("The Multiply total of the list is: " + str(multi()))

#4 Write a Python program to reverse a string.
def rvse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1

print(rvse('1234abcd'))

#5

