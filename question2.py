#Write a recursive function to calculate the factorial of a number 
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    if num < 0:
        print("negative number.")
    else:
        print(f"The factorial of {num} is: {factorial(num)}")
