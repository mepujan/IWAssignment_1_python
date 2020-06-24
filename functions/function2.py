# Write a Python function to sum all the numbers in a list.

def sum_list(items):
    sum=0
    for item in items:
        sum+=item
    return sum

def main():
    items=list(map(int,input('Enter numbers: ').split(' ')))
    print("The sum is : ",sum_list(items))

if __name__ == '__main__':
    main()
