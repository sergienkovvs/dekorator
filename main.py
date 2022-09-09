from datetime import datetime
import random

def dec(f):

    def wrapper(*args):
        stat = datetime.now()
        res = f(*args)
        finish = datetime.now()
        print(finish - stat)
        return res
    return wrapper

@dec
def spam():
    return [random.randint(0,1000) for _ in range(0,1000)]

@dec
def Hat():
    return (_ for _ in range(0,1000000))

spam()
Hat()