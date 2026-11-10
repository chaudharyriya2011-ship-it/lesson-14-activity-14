def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
print("The factorial of 5 is :",factorial(5))
print("The factorial of 6 is :",factorial(6))
print("The factorial of 7 is :",factorial(7))