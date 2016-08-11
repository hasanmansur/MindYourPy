'''
Essentially, decorators work as wrappers, modifying the behavior of the code before and after a target 
function execution, without the need to modify the function itself, augmenting the original functionality, thus decorating it.
'''

print('-----------------------------------Composition of Decorators------------------------------------')

def get_text(name):
    return 'hello ' + name

def p_decorate(func):
    def wrapper(name):
        return '<p>' + func(name) +'</p>'
    return wrapper

def bold_decorate(func):
    def wrapper(name):
        return '<b>' + func(name) +'</b>'
    return wrapper

def div_decorate(func):
    def wrapper(name):
        return '<div>' + func(name) +'</div>'
    return wrapper

get_text = div_decorate(p_decorate(bold_decorate(get_text)))
print(get_text('hasan'))


print('------------------------------------Pythons Decorator Syntax------------------------------------')

@div_decorate
@p_decorate
@bold_decorate
def say_bye(name):
    return 'bye ' + name

print(say_bye('hasan'))


'''
Decorators expect to receive a function as an argument, that is why we will have to build a function that 
takes those extra arguments and generate our decorator on the fly. In the example above tags, is our decorator generator.
'''

print('-------------------------------Passing Arguments to decorator------------------------------------')
def tags(tag):
    def tags_decorator(func):
        def func_wrapper(name):
            return '<{0}>{1}</{0}>'.format(tag, func(name))
        return func_wrapper
    return tags_decorator


@tags('div')
@tags('p')
@tags('b')
def hello(name):
    return 'hello ' + name

print(hello('hasan'))


print('--------------------------------------Decorating Methods------------------------------------------')

'''
In Python, methods are functions that expect their first parameter to be a reference to the current object. 
We can build decorators for methods the same way, while taking self into consideration in the wrapper function.
'''

def p_decorate(func):
    def func_wrapper(self):
        return '<p>{0}</p>'.format(func(self))
    return func_wrapper

class Person():
    def __init__(self):
        self.name = 'John'
        self.family = 'Doe'
    
    @p_decorate
    def get_name(self):
        return self.name + ' ' + self.family

test_person = Person()
print(test_person.get_name())

'''
A much better approach would be to make our decorator useful for functions and methods alike. 
This can be done by putting *args and **kwargs as parameters for the wrapper, then it can accept 
any arbitrary number of arguments and keyword arguments.
'''

def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return '<p>{0}</p>'.format(func(*args, **kwargs))
    return func_wrapper

class Person():
    def __init__(self):
        self.name = 'John'
        self.family = 'Doe'
    
    @p_decorate
    def get_name(self):
        return self.name + ' ' + self.family

test_person = Person()
print(test_person.get_name())


