# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.


def factorial(num):
    if num < 0:
        return "No factorial of negative number"
    else:
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num-1)

def main():
    num=int(input('Enter number to calculate factorial: '))
    print('factorial = ',factorial(num))

if __name__ == '__main__':
    main()