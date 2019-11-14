L=[1, 2, 4, 8, 16, 32, 64]
X = 5
print(L)
if 2**X in L:
    print('at index',L.index(2**X))
else:
    print(X,'not found')
for n in L:
    if n==2**X:
        print('at index',L.index(n))
        break
    else:
        print(X,'not found')
i = 0
for i in range(len(L)):
    if  L[i]==2**X :
        print('at index',i)
        break
    else:
        print(X,'Not found')
i=0
while i < len(L)  and L[i]!=2**X:
    i=i+1 
    if i==(len(L)-1):
        print(X, 'not found')
        break
else:
    print('at index', i)