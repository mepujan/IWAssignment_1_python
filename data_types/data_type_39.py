# Write a Python program to unpack a tuple in several variables.

def main():
    tuple_sample=(1,2,3,4)
    t1,t2,t3,t4=tuple_sample
    print("t1=%d,t2=%d,t3=%d,t4=%d"%(t1,t2,t3,t4))

if __name__=='__main__':
    main()