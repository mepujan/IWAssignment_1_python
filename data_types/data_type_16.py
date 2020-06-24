# Write a Python program to multiplies all the items in a list.
from functools import reduce

def main():
    list_item= list(map(int,input('enter the numbers: ').split(' ')))
    print('Multiple of list is : ',reduce(lambda x,y: x*y,list_item))

if __name__ == '__main__':
    main()