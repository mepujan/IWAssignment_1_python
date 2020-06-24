# Write a Python program to sort a list of tuples using Lambda.

def main():
    sample_tuples_list=[(1,2,4),[5,8,7],(9,10,11)]
    sample_tuples_list.sort(key= lambda x: x[1])
    print(sample_tuples_list)

if __name__ == '__main__':
    main()