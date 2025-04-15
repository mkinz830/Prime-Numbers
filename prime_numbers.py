# Write a Python program to check the given number is prime number or not.

num = 2

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for x in range(2,num):
        if(num % x) == 0:
            print(num, "is not a prime number")
            print(x, "times", num // x, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")