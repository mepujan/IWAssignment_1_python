# Write a Python script to merge two Python dictionaries.

def main():
    dict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    dict2={6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    resultant_dict={**dict1,**dict2}
    print(resultant_dict)


if __name__== '__main__':
    main()