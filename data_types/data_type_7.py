# ​ Write a Python function that takes a list of words and returns the length of the
# longest one.
def length_of_longest_one(list_of_words):
    len_of_words=[];
    for n in list_of_words:
        len_of_words.append(len(n))
    len_of_words.sort()
    return len_of_words[-1]


def main():
    list_of_words=input('Enter list of words: ').split(' ')
    print(length_of_longest_one(list_of_words))
if __name__ == '__main__':
    main()