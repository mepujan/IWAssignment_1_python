# Write a Python function that takes a number as a parameter and check the
# number is prime or not

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        else:
            for num in range(2,number):
                if number % num == 0:
                    return False
            return True
    else:
        return False


def main():
    num = int(input('Enter number:'))
    print("prime = ",is_prime(num))

if __name__ == "__main__":
    main()