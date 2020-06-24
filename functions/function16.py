# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

def main():
    sample_list=[2,3,4,5,6,7]
    square_list= map(lambda num: num **2 , sample_list)
    print("square of list = ",list(square_list))
    cube_list= map(lambda num: num **3 , sample_list)
    print("Cube of list = ",list(cube_list))

if __name__ == '__main__':
    main()