'''
--------------------------- Iterator ---------------------------------
'''

print('-------------------example1-------------------')
try:
    s = 'abc'
    it = iter(s)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print('StopIteration occured')


print('-------------------example2-------------------')
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('hello')
for i in rev:
    print(i)

