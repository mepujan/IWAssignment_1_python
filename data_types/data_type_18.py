# Write a Python program to get the largest number from a list.

def main():
    number_list=list(map(int,input('Enter the numbers:').split(' ')))
    print('Max value= ',max(number_list))

if __name__ == '__main__':
    main()
