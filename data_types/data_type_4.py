# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.

def concat_swap_str(str1,str2):
    final_str= str1.replace(str1[:2],str2[:2]) + ' ' + str2.replace(str2[:2],str1[:2])
    return final_str
    
def main():
    str1= input("Enter first String: ")
    str2=input("Enter second String: ")
    print(concat_swap_str(str1,str2))
if __name__ == '__main__':
    main()