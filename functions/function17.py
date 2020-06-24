# Write a Python program to find if a given string starts with a given character
# using Lambda.

def main():
    string=input('String= ')
    char=input('char= ')
    check=lambda x,y: x in y[0]
    print(check(char,string))
if __name__ == '__main__':
    main()