# ​ Write a Python program to count the occurrences of each word in a given
# sentence.
def num_of_words(string):
    words_num={}
    word_list=string.split(' ')

    for words in word_list:
        if words in words_num:
            words_num[words] += 1
        else:
            words_num[words] = 1
    return words_num



def main():
    string= input("Enter the string:")
    print(num_of_words(string))

if __name__=='__main__':
    main()