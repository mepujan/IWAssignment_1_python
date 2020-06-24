# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

def main():
    sample_dict={n:n**2 for n in range(1,16)}
    print(sample_dict)

if __name__ == '__main__':
    main()