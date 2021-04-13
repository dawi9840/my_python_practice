def printHello(func):
    def wrapper(arg):
        print('Hello')
        return func(arg)
    return wrapper

@printHello
def printArg(arg):
    print(arg)

printArg('World')
printArg('Kitty')