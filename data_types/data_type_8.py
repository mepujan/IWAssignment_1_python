# Write a Python program to remove the n​ th​ index character from a nonempty
# string.

def remove_nth_index(string,index):
    if string and len(string) >= index:
        return string.replace(string[index],'')
    return string
    

def main():
    string=input('Enter the string: ')
    index=int(input('Enter index to remove character: '))
    print(remove_nth_index(string,index))

if __name__ == '__main__':
    main()


