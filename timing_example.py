from time import time
def time_func(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()

        print(f"Time Taken: {end - start}s")
        return 
    return wrapper

@time_func
def dummy_func():
    for i in range(100000000000):
        pass

dummy_func()