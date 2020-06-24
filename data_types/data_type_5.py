# Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

def add_ing_or_ly(string):
    if len(string) < 3:
        return string
    else:
        if 'ing' in string:
            return string+'ly'
        else:
            return string + 'ing'

def main():
    string=input("Enter the string: ")
    print(add_ing_or_ly(string))

if __name__ == '__main__':
    main()