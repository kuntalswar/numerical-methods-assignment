#!/home/kuntal/anaconda3/bin/python
s="mumbai"
for i in range(6):
    print(s[i],"in unicode code is ",ord(s[i]))
sum=0
for i in s:
    sum=sum+ord(i)
print('sum of unicode numbers is:',sum)
    #list method

L=[]
for i in s:
    L.append(ord(i))
print(L)

#least comprehension
LC=[ord(x) for x in s]
print(LC)

#Using map

M=(map(ord,s))
print(list(M))


