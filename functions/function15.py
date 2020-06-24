# Write a Python program to filter a list of integers using Lambda.

def main():
    sample_list=[1,2,3,4,5-1,-3,-6,1.5,2.5,4.8,1.1]
    integer_list= filter(lambda x: isinstance(x,int) ,sample_list)
    print(list(integer_list))

if __name__ == '__main__':
    main()