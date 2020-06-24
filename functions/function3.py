# Write a Python function to multiply all the numbers in a list.

def product_items(items):
    product=1
    for item in items:
        product*=item
    return product

def main():
    items=list(map(int,input('Enter numbers: ').split(' ')))
    print("The sum is : ",product_items(items))

if __name__ == '__main__':
    main()
