# ​ Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def new_string(string):
    if len(string) > 1:
        return string[-1] + string[1:-1]+string[0]
    return string



def main():
    string=input("enter the string: ")
    print(new_string(string))

if __name__ == '__main__':
    main()
