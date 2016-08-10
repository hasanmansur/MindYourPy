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


'''
--------------------------- Generator ---------------------------------
# Generators are a simple and powerful tool for creating iterators.
# They are written like regular functions but use the yield statement whenever they want to return data. 
# Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last 
  executed).
# What makes generators so compact is that the __iter__() and __next__() methods are created automatically.
'''
print('-------------------example3-------------------')
def reverse(data):
    for i in range(len(data)-1, -1, -1):
            print('sending data in %dth position' % i)
            yield data[i]

for j in reverse('hello'):
    print(j)
