#!/home/kuntal/anaconda3/bin/python
for i in range (5):
    try:
        print("(1/",i, ")=" ,1/i)
    except ZeroDivisionError:
        print("Indeterminate")






