#!/home/kuntal/anaconda3/bin/python
def Fibonacci(n):
    if n<0:
        print("Please enter a positive integer")
    elif n==1:       
        print("F(1)=",f1)
    elif n==0:       
        print("F(0)=",f0)
    elif n>1:
        f0=0
        f1=1
        for i in range(n-1):
            sf0=f1
            f1=f0+f1
            f0=sf0
        print("F(",n,")=",f1)   



