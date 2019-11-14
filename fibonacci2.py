#!/home/kuntal/anaconda3/bin/python
import timeit
mycode = '''
import Fibonacci_module
Fibonacci_module.Fibonacci(20)
'''
print("Time required to exicute the code for once is =",(timeit.timeit(setup = 'pass' , stmt = mycode,number = 50))/50)

