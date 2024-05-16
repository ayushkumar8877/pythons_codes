num = int(input("enter any number"))
factorial = 1
if num < 0:
    print("factorial is not defined for negative number")
elif num == 0:
    print("the factorial of 0 is 1.")
else:
    for i in range (1 ,num + 1):
        factorial*= i
    print("the factorial of",num,"is",factorial)    
        
            