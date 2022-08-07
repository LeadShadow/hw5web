from time import time
from multiprocessing import Process, Pool, cpu_count


def factorize(*number):
    n = 0
    for num in number:
        list_for_result = []
        while n <= num:
            n += 1
            if num % n == 0:
                list_for_result.append(n)
            continue
        n = 0
        yield list_for_result


if __name__ == "__main__":
    time_before = time()
    a = Process(target=factorize, args=(128,))
    b = Process(target=factorize, args=(255,))
    c = Process(target=factorize, args=(99999,))
    d = Process(target=factorize, args=(10651060,))
    a.start()
    b.start()
    c.start()
    d.start()
    a.join()
    b.join()
    c.join()
    d.join()
    time_after = time()
    print(round(time_after-time_before, 4))

