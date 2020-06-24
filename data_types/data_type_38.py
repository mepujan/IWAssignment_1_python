# Write a Python program to remove a key from a dictionary.

def main():
    sample_dict={1: 1, 2: 4, 3: 9,4:10}
    key=1
    if key in sample_dict:
        del sample_dict[key]
    print(sample_dict)

if __name__ == '__main__':
    main()