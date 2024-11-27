import time

def log_calls(func):

    def wrapper(*args, **kwargs):
        now = time.time()
        print(f"Calling {func.__name__} with {args} and {kwargs}")

        return_value = func(*args, **kwargs)

        print(f"Executed {func.__name__} in {time.time()-now}")

        return return_value
    return wrapper

def test1(a,b,c):
    print("test1 function called")

def test2(a, b):
    print("test2 function called")

def test3(a, b):
    print("test3 function called")
    time.sleep(1)

if __name__ == "__main__":

    test1(1,2,3)
    test2(4,5)
    test3(6,7)

    # decorated functions dinamically
    test1 = log_calls(test1)
    test2 = log_calls(test2)
    test3 = log_calls(test3)

    test1(1,2,c=3)
    test2(4,b=5)
    test3(6,7)

    test1(8,9,10)
    test2(11,12)
    test3(13,b=14)


