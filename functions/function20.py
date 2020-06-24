# Write a Python program to find intersection of two given arrays using
# Lambda.

def main():
    array1=[1,2,3,4,5,6]
    array2=[3,4]
    intersection= list(filter(lambda x: x in array1,array2))
    print(intersection)

if __name__ == '__main__':
    main()