#get random in function
from random import randint

#Task3
ans = randint(1,9)
print(ans)
userguess =  int(input("Guess my number: "))
while ans != userguess:
    print("Wrong")
    userguess =  int(input("Guess again: "))
if userguess == ans:
    print("whoa good guess")