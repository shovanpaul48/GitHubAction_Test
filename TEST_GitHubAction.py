def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def CheckPrime(n)

    if n <= 1:
        return "Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Factorial of", num, "is", factorial(num))
    print(num, "is ", CheckPrime(num))
