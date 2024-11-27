import time

def log_calls(func):

    def wrapper(*args, **kwargs):
        now = time.time()
        print(f"Calling {func.__name__} with {args} and {kwargs}")

        return_value = func(*args, **kwargs)

        print(f"Executed {func.__name__} in {time.time()-now}")

        return return_value
    return wrapper

# decorate the function when it is defined
@log_calls
def test1(a,b,c):
    print("test1 function called")

@log_calls
def test2(a, b):
    print("test2 function called")

@log_calls
def test3(a, b):
    print("test3 function called")
    time.sleep(1)

if __name__ == "__main__":

    test1(1,2,3)
    test2(4,5)
    test3(6,7)


