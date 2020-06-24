# Write a Python program to multiply all the items in a dictionary.


def main():
    sample_dict={1: 1, 2: 4, 3: 9,4:10}
    product=1
    for values in sample_dict.values():
        product*=values
    print("The product of values is : ",product)


if __name__ == '__main__':
    main()