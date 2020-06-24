# ​ Write a Python program to remove duplicates from a list.

def unique_list(items):
    return set(items)


def main():
    list_with_duplicates=['abc','xyz','pqr','abc','pqr']
    print(list(unique_list(list_with_duplicates)))

if __name__ == '__main__':
    main()