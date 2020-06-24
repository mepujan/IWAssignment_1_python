# Write a Python script to concatenate following dictionaries to create a new
# one.


def main():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    final_dict={**dic1,**dic2,**dic3}
    print(final_dict)
if __name__ == '__main__':
    main()