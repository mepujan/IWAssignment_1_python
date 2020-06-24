# ​ Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

def unique_words(string):
    return sorted(set(string))


def main():
    comma_seperated_words=input("Enter values: ").split(',')
    result=unique_words(comma_seperated_words)
    print(','.join(result))

if __name__ == '__main__':
    main()