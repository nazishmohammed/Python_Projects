#This is a python program which if run would create a fun pattern with stars 

def main():
    n=num()
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()

def num():
    print("Please note that the number of stars in each row will correspond to the row number")
    user_in = int(input("Enter the number of rows in which you wanted stars\n"))
    return user_in

main()