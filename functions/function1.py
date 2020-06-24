# Write a Python function to find the Max of three numbers.

def max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
def main():
    num1=int(input("First Number : "))
    num2=int(input("Second Number : "))
    num3=int(input("Third Number : "))
    print("Max number is : ",max(num1,num2,num3))

if __name__ == '__main__':
    main()