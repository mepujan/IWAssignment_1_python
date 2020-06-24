# Write a Python program to print the even numbers from a given list.


def main():
    sample_list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('Even List = ',list(filter(lambda x: x%2 == 0,sample_list)))
if __name__ == '__main__':
    main()