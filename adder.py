def adder(x,y):
    return(x+y)

#adding two strings
s1="Hello"
s2="World"
print(adder(s1,s2))  #yes we need a print statement to see the results

#adding two lists
L1=["kuntal","kanti","swar"]
L2=["2014","@","gmail",".com"]
print(adder(L1,L2))     #yes we need a print statement to see the results


#adding two floatimg point numbers

print(adder(.12345,1.2345))
#adder for arbitory number of arguments

def adder(*l):
    sum=0
    for arg in l:
        sum=sum+arg
    return sum

print(adder(6,4,5,1,3))


#adder with default keyword argument

def adder(good=1,bad=2,ugly=3):
    return (good+bad+ugly)
print(adder(ugly=1,good=5))

#arbitrary number of keyword arguments
def adder(**arg):
    L=list(arg.values())
    return sum(L)   #or we can go through elements of the list using loops


print(adder(may=5,jun= 6,january= 1,march= 3))