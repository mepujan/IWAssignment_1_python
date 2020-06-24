# Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_str_in_middle(braces,string):
    mid_value= len(braces)//2
    return braces[:mid_value] + string + braces[mid_value:]

def main():
    braces=input("Enter the braces: ")
    string=input('Enter the string: ')
    print(insert_str_in_middle(braces,string))

if __name__ == '__main__':
    main()