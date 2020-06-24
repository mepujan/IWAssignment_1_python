# Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

def main():
    num1=int(input("number1="))
    num2=int(input("number2="))
    result= lambda num: num + 15
    product= lambda x,y: x * y
    print("Number 1 + 15 = ",result(num1))
    print("Product of numbers=",product(num1,num2))

if __name__ == "__main__":
    main()