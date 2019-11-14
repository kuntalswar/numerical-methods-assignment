#!/home/kuntal/anaconda3/bin/python
f0=0
f1=1
print("First 10 Fibonacci No. are")
print("F(0)=",f0)
print("F(1)=",f1)
for i in range(8):
	sf0=f1
	f1=f0+f1
	print("F(",i+2,")=",f1)
	f0=sf0
    

