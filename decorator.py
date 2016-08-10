'''
Essentially, decorators work as wrappers, modifying the behavior of the code before and after a target function execution, without the need to modify the function itself, augmenting the original functionality, thus decorating it.
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
