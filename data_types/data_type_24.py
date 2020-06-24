# ​ Write a Python program to clone or copy a list.


def main():
    list1=[1,2,3,4]
    list2=list1  #Method 1
    list3=list1.copy()  #method 2 using copy method
    print(list2)
    print(list3)

if __name__ == '__main__':
    main()