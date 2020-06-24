# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

def count_str_number(string):
    count=0
  
    for word in string:
        if len(word) >= 2:
            if word[0] == word[-1]:
                count+=1
            else:
                count=count
        else:
            count=count
    return count
        

def main():
    str_list=list(input('Enter list of strings: ').split(','))
    print(count_str_number(str_list))

if __name__ == '__main__':
    main()