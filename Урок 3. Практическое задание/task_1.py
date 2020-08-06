"""
Мучался очень долго, во всех случаях словарь заполняется дольше!
"""
import time


def time_dec(funk):
    t = time.time()
    funk()
    print(time.time() - t)


@time_dec
def lis():
    my_list = [i for i in range(0, 10000000)]


@time_dec
def di():
    my_dict = {}
    for key in range(0, 10000000):
        my_dict[key] = key
