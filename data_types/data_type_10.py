# ​ Write a Python program to remove the characters which have odd index
# values of a given string.

def remove_odd_index_char(string):
    result = "" 
    for i in range(len(string)):
        if i % 2 == 0:
            result = result + string[i]
    return result

def main():
    string=input("Enter string: ")
    print(remove_odd_index_char(string))

if __name__== '__main__':
    main()