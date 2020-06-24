# Write a Python program to check whether all dictionaries in a list are empty or
# not.

def main():
    sample_list1=[{},{},{}]
    sample_list2=[{1,2},{},{}]

    print(all(not val for val in sample_list1))
    print(all(not val for val in sample_list2))



if __name__ == '__main__':
    main()