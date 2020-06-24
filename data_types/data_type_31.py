# Write a Python program to iterate over dictionaries using for loops.

def main():
    dict1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    for key,value in dict1.items():
        print(key,'=>',value)

if __name__ == '__main__':
    main()