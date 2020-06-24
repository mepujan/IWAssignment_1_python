# Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


def main():
    sample_data1=[1, 3, 5, 7, 9, 10]
    sample_data2=[2, 4, 6, 8]
    sample_data1[-1:]=sample_data2
    print(sample_data1)

if __name__ == '__main__':
    main()