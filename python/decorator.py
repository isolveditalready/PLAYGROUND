import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("time : " , total)
        return rv
    return wrapper

#decorator declaration 
@timer
def test():
    for _ in range(1000000):
        pass
@timer
def test2():
    time.sleep(2)

test()
test2()