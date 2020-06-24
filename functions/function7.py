# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.

def count_uppercase_lowercase(string):
    count_upper=0
    count_lower=0
    for char in string:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower +=1
        else:
            pass
    print("No of uppercase=",count_upper)
    print("No of lowercase=",count_lower)



def main():
    string=input('String= ')
    count_uppercase_lowercase(string)

if __name__ == '__main__':
    main()