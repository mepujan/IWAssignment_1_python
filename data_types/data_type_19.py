# Write a Python program to get the smallest number from a list.


def main():
    number_list=list(map(int,input('Enter the numbers:').split(' ')))
    print('minimum value= ',min(number_list))

if __name__ == '__main__':
    main()
