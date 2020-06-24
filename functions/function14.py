# Write a Python program to sort a list of dictionaries using Lambda

def main():
    sample_dict=[{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}]

    sample_dict.sort(key=lambda x: x['model'])
    print(sample_dict)

if __name__ == '__main__':
    main()