
def printer():
    print("hello world")

def display_info(func):
    def inner():
        print("Exacuting",func.__name__,"function")
        func()
        print("Finished exacution")
    return inner



result= display_info(printer)
result()