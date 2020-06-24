# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

def string_manipulate(string):
    if 'not' in string and 'poor' in string:
        index_not=string.find("not")
        index_poor=string.find("poor")
        if index_not < index_poor:
            return string.replace(string[index_not:],"good")
    return string
    


def main():
    string=input('Enter string: ')
    print(string_manipulate(string))

if __name__ == '__main__':
    main()