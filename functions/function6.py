# Write a Python function to check whether a number is in a given range.

def check_range(number,rnge):
    if number in range(rnge):
        return "number in range"
    return "number not in range"
    

def main():
    num=int(input("number="))
    range=int(input("Range 0 to ? "))
    print(check_range(num,range))

if __name__ == '__main__':
    main()
