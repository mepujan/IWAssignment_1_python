# Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : 'google.com'

def number_of_chars(name):
    dict_letter_count={}
    for n in name:
        print(n)
        frequency=dict_letter_count.keys()
        print(frequency)
        if n in frequency:
            dict_letter_count[n] += 1
        else:
            dict_letter_count[n]=1
    return dict_letter_count
        
        
    return 0
def main():
    name=input("Enter any string: ")
    print(number_of_chars(name))

if __name__ == '__main__':
    main()