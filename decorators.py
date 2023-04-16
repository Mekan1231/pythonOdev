


def display_info(func):
    def inner():
        print("Exacuting",func.__name__,"function")
        func()
        print("Finished exacution".upper())
    return inner

@display_info
def printer():
    print("hello world")


printer()