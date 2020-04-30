def say_hello(name=None):
    if name:
        return 'Hello {}!'.format(name)
    else:
        return 'Hello!'

print(say_hello('Kang'))