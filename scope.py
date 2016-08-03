'''

Facts to remember:
-----------------------
# If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
# If there is a global statement for that variable in a function, it is a global variable.
# Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
# But if the variable is not used in an assignment statement, it is a global variable.
# The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals. 
# The global statement causes the listed identifiers to be interpreted as globals.

'''

print("--------------------example1-------------------")

def train():
	vehicle = "train"
	print("In train:", vehicle)


def car():
	global vehicle
	vehicle = "car"
	print("In car:", vehicle)

def bus():
	print("In bus:", vehicle)

vehicle = "test vehicle"
train()
car()
bus()
print("In global:", vehicle)

print("--------------------example2-------------------")
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
