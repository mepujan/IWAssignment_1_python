# Write a Python program to remove an item from a tuple.

def main():
    sample_tuple=('hello','you','have','a','nice','day')
    tuple_to_list=list(sample_tuple)
    tuple_to_list.remove('hello')
    tuple_new=tuple(tuple_to_list)
    print(tuple_new)

if __name__ == '__main__':
    main()