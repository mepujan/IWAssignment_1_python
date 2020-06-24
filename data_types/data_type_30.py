# Write a Python script to check whether a given key already exists in a
# dictionary.

def main():
    dic1={1:10, 2:20}
    key=int(input('enter the key:'))
    if key in dic1.keys():
        print('key exist')
    else:
        print('key doesnot exist')

if __name__ == '__main__':
    main()