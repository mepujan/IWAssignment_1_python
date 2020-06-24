# Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def mul(num):
    unknown_num=10
    return num * unknown_num

def main():
    num = int(input('Number='))

    print("Product with unknown number = ",mul(num))

if __name__ == '__main__':
    main()