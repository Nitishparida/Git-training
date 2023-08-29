Num = int(input("Please enter one Number : "))
Reverse = 0
while Num != 0:
    Temp = Num % 10
    Reverse = Reverse*10 + Temp
    Num //= 10

print("Reverse Number is : ", Reverse )
