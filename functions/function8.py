# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def unique_list(data):
    return list(set(data))

def main():
    sample_list=[1,2,3,3,3,3,4,5]
    print("unique list=",unique_list(sample_list))

if __name__ == "__main__":
    main()