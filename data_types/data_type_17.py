# Write a Python program to sum all the items in a list.

def main():
    numbers=list(map(int,input("enter the numbers: ").split(' ')))
    print("The sum of list is: ",sum(numbers))

if __name__ == '__main__':
    main()