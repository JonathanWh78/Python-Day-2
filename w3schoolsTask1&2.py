#Task 1

for i in range (1500, 2700):
    if (i % 7) == 0 and (i % 5) == 0:
        print(i)

#Task2
print ("Please Select an Conversion method: ")
print ("Option 1: Convert to Celsius")
print  ("Option 2: Convert to Farenheit")
choice = int(input("Enter Option"))
if choice == 1:
    TempF = int(input("Please Enter the temperature: "))
    #F = C×(9/5)+32
    AnsF = round(TempF * 1.8 + 32)
    print(AnsF)
elif choice == 2:
    TempC = int(input("Please Enter the temperature: "))
    # Subtract 32 from this figure (e.g., 100 - 32 = 68).
    #Divide your answer by 1.8 (e.g., 68 / 1.8 = 37.78)
    AnsC = round((TempC - 32) / 1.8)
    print(AnsC)
else:
    print ("Please Enter a valid option")