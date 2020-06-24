# Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.

def manipulate_string(string):
    if len(string) < 2:
        return 'Empty String'
    else:
        return string[:2]+string[-2::1]

def main():
    string=input("Enter string: ")
    print(manipulate_string(string))


if __name__=='__main__':
    main()