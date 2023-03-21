import math

print("Welcome to the simple math helper.")
print("What would you like to calculate?")
print("1. Sqrt")
print("2. Log")
print("3. Factorial")

choice = int(input("> "))

if choice == 1:
    num = float(input("Enter the number to sqrt:\n"))
    result = math.sqrt(num)
    print(result)
    
elif choice == 2:
    num = float(input("Enter the number to take log:\n"))
    base = float(input("Enter the base of the log:\n"))
    result = math.log(num, base)
    print(result)
    
elif choice == 3:
    num = int(input("Enter the number to find factorial:\n"))
    result = 1
    for i in range(1, num+1):
        result *= i
    print(result)
    
else:
    print("Invalid choice")
