def simple_function(self):
    """ This is a docstring that I'm playing with """
    pass
# this is a comment
class simple_class():
    """ This is a simple class """
    def __init__(self):
        self.object = self

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

SO_THI_IS_A_CONSTANT = 123

def tryout():


Yes: if foo.startswith('bar'):
No:  if foo[:3] == 'bar':

Yes: if isinstance(obj, int):
No:  if type(obj) is type(1):
