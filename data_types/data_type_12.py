# Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.


def upper_and_lower_case(string):
    print("Uppercase= ",string.upper())
    print("Lowercase= ",string.lower())

def main():
    string=input("Enter the string: ")
    upper_and_lower_case(string)

if __name__ == '__main__':
    main()