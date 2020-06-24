# Write a Python program to add an item in a tuple.

def main():
    sample_tuple=(1,2,3)

    new_tuple= sample_tuple + (5,)
    print(new_tuple)

if __name__ == "__main__":
    main()