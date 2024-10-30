#asking the user to enter the number of 1st n fibonacci numbers
x = int(input("please enter your number to generate the fibonacci numbers: "))

#these will be used to calculate the fibonacci numbers 
a = 0
b = 1

#calculating the fibonacci number and printing it
for i in range(0, x, +1):
    print(a)
    fibonacci = a + b
    a = b
    b = fibonacci