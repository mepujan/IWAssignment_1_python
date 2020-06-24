# Write a Python program to sum all the items in a dictionary.


def main():
    sample_dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    sum=0
    for values in sample_dict.values():
        sum+=values
    print("The sum of values is : ",sum)


if __name__ == '__main__':
    main()