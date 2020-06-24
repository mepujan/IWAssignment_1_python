# Write a Python program to insert a given string at the beginning of all items in
# a list.

# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


def main():
    sample_list=[1,2,3,4]
    string='emp'
    result_list=[]
    for val in sample_list:
        result_list.append(string+str(val))
    print(result_list)


if __name__ == '__main__':
    main()