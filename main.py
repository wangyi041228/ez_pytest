from time import perf_counter as perf
from statistics import mean, stdev
import timeit

g = 0


r"""
py -3.7 -m pyperf timeit -s "global i" "for i in range(100_000_000): pass" --rigorous
py -3.8 -m pyperf timeit -s "global i" "for i in range(100_000_000): pass" --rigorous
py -3.9 -m pyperf timeit -s "global i" "for i in range(100_000_000): pass" --rigorous
py -3.10 -m pyperf timeit -s "global i" "for i in range(100_000_000): pass" --rigorous
py -3.11 -m pyperf timeit -s "global i" "for i in range(100_000_000): pass" --rigorous
pypy -m pyperf timeit -s "global i" "for i in range(100_000_000): pass" --rigorous

py -3.7 -m timeit -s "global i" "for i in range(100_000_000): pass"
py -3.8 -m timeit -s "global i" "for i in range(100_000_000): pass"
py -3.9 -m timeit -s "global i" "for i in range(100_000_000): pass"
py -3.10 -m timeit -s "global i" "for i in range(100_000_000): pass"
py -3.11 -m timeit -s "global i" "for i in range(100_000_000): pass"
pypy -m timeit -s "global i" "for i in range(100_000_000): pass"

py -3.7 -m timeit -p -s "global i" "for i in range(100_000_000): pass"
py -3.8 -m timeit -p -s "global i" "for i in range(100_000_000): pass"
py -3.9 -m timeit -p -s "global i" "for i in range(100_000_000): pass"
py -3.10 -m timeit -p -s "global i" "for i in range(100_000_000): pass"
py -3.11 -m timeit -p -s "global i" "for i in range(100_000_000): pass"
pypy -m timeit -p -s "global i" "for i in range(100_000_000): pass"

py -3.7 D:\1.py
py -3.8 D:\1.py
py -3.9 D:\1.py
py -3.10 D:\1.py
py -3.11 D:\1.py
pypy D:\1.py
"""


def example_1():
    start = perf()
    global g
    for g in range(100_000_000):
        pass
    end = perf()
    return end - start


def example_1it(repeat=50):
    it = timeit.Timer("global g\nfor g in range(100_000_000): pass").repeat(repeat=repeat, number=1)
    # it = timeit.Timer("for g in range(100_000_000): pass", globals={'g': g}).repeat(repeat=repeat, number=1)
    # it = timeit.Timer("for g in range(100_000_000): pass", setup="global g").repeat(repeat=repeat, number=1)
    return it


"""
py -3.7 -m pyperf timeit "for i in range(100_000_000): pass" --rigorous
py -3.8 -m pyperf timeit "for i in range(100_000_000): pass" --rigorous
py -3.9 -m pyperf timeit "for i in range(100_000_000): pass" --rigorous
py -3.10 -m pyperf timeit "for i in range(100_000_000): pass" --rigorous
py -3.11 -m pyperf timeit "for i in range(100_000_000): pass" --rigorous
pypy -m pyperf timeit "for i in range(100_000_000): pass" --rigorous

py -3.7 -m timeit "for i in range(100_000_000): pass"
py -3.8 -m timeit "for i in range(100_000_000): pass"
py -3.9 -m timeit "for i in range(100_000_000): pass"
py -3.10 -m timeit "for i in range(100_000_000): pass"
py -3.11 -m timeit "for i in range(100_000_000): pass"
pypy -m timeit "for i in range(100_000_000): pass"

py -3.7 -m timeit -p "for i in range(100_000_000): pass"
py -3.8 -m timeit -p "for i in range(100_000_000): pass"
py -3.9 -m timeit -p "for i in range(100_000_000): pass"
py -3.10 -m timeit -p "for i in range(100_000_000): pass"
py -3.11 -m timeit -p "for i in range(100_000_000): pass"
pypy -m timeit -p "for i in range(100_000_000): pass"
"""


def example_2():

    start = perf()
    for i in range(100_000_000):
        pass
    end = perf()
    return end - start


"""
py -3.7 -m pyperf timeit "for i in range(100_000_000): j = i" --rigorous
py -3.8 -m pyperf timeit "for i in range(100_000_000): j = i" --rigorous
py -3.9 -m pyperf timeit "for i in range(100_000_000): j = i" --rigorous
py -3.10 -m pyperf timeit "for i in range(100_000_000): j = i" --rigorous
py -3.11 -m pyperf timeit "for i in range(100_000_000): j = i" --rigorous
"""


def example_3():
    start = perf()
    for i in range(100_000_000):
        j = i
    end = perf()
    return end - start


def example_4():
    """
    py -3.7 -m pyperf timeit "for i in range(10_000):" "  for j in range(10_000):" "    pass" --rigorous
    """
    start = perf()
    for i in range(10_000):
        for j in range(10_000):
            pass
    end = perf()
    return end - start


def example_5():
    """
    py -3.7 -m pyperf timeit "[[0] * 10_000 for _ in range(10_000)]" --rigorous
    py -3.8 -m pyperf timeit "[[0] * 10_000 for _ in range(10_000)]" --rigorous
    py -3.9 -m pyperf timeit "[[0] * 10_000 for _ in range(10_000)]" --rigorous
    py -3.10 -m pyperf timeit "[[0] * 10_000 for _ in range(10_000)]" --rigorous
    py -3.11 -m pyperf timeit "[[0] * 10_000 for _ in range(10_000)]" --rigorous
    """
    start = perf()
    [[0] * 10_000 for _ in range(10_000)]
    end = perf()
    return end - start


def example_6():
    """
    py -3.7 -m pyperf timeit -s "from itertools import product" "for _,_,_,_ in product(range(100),range(100),range(100),range(100)):pass" --rigorous

    """
    from itertools import product
    start = perf()
    for _, _, _, _ in product(range(100), range(100), range(100), range(100)):
        pass
    end = perf()
    return end - start


def example_7():
    """
    py -3.11 -m pyperf timeit "res=0 / for i in range(10_000_000): res += i ** 2 /n; res %= 1_000_000_007" --rigorous

    """
    start = perf()
    res = 0
    for i in range(10_000_000):
        res += i ** 2
        res %= 1_000_000_007
    end = perf()
    return end - start


def example_8():
    """
    py -3.11 -m pyperf timeit "res=0 / for i in range(10_000_000): res += i ** 2 /n; res %= 1_000_000_007" --rigorous
    """
    def fab(n):
        return 1 if n in [1, 2] else fab(n - 1) + fab(n - 2)

    start = perf()
    fab(35)
    end = perf()
    return end - start


def example_9():

    from random import randint
    start = perf()
    count = 0
    s = {randint(0, 10_000_000) for _ in range(10_000)}
    for _ in range(5_000_000):
        n = randint(0, 10_000_000)
        if n in s:
            count += 1
    end = perf()
    return end - start


def example_9_1():
    """
    py -3.11 -m pyperf timeit -s "s = set(range(10_000_000))" "for i in range(10_000_000):" " if i in s:" "  count += 1" --rigorous
    """
    count = 0
    s = set(range(10_000_000))
    start = perf()
    for i in range(10_000_000):
        if i in s:
            count += 1
    end = perf()
    return end - start


def example_10():
    """
    py -3.11 -m pyperf timeit "list(range(0, 100_000_000))" --rigorous
    """
    start = perf()
    list(range(0, 100_000_000))
    end = perf()
    return end - start


def example_11():
    """
    py -3.11 -m pyperf timeit -s "lst = list(range(0, 100_000_000))" "lst.reverse()" --rigorous
    """
    lst = list(range(0, 100_000_000))
    start = perf()
    lst.reverse()
    end = perf()
    return end - start


def example_12():
    from random import randint
    start = perf()
    lst = [randint(1, 100_000_000) for _ in range(1_000_000)]
    lst.sort()
    end = perf()
    return end - start


def example_12_1():
    """
    py -3.11 -m pyperf timeit -s "lst = list(range(0, 100_000_000))" -s "lst.reverse()" "lst.sort()" --rigorous
    """
    lst = list(range(0, 100_000_000))
    lst.reverse()
    start = perf()
    lst.sort()
    end = perf()
    return end - start


def example_13():
    """
    py -3.11 -m pyperf timeit -s "lst = [0] * 200_000" "while lst: lst.pop(0)" --rigorous
    """
    start = perf()
    lst = [0] * 200_000
    while lst:
        lst.pop(0)
    end = perf()
    return end - start


def example_14():
    from random import randint, choice
    start = perf()
    for _ in range(1000):
        line = str(randint(1, 100))
        for __ in range(1000):
            line += choice('+-*/') + str((randint(1, 100)))
        eval(line)
    end = perf()
    return end - start


def work(func, timeit_mode=False, repeat=50):
    if timeit_mode:
        results = func(repeat)
    else:
        results = []
        for _ in range(repeat):
            results.append(func())
    _std = str(stdev(results))[:6]
    _mean = str(mean(results))[:6]
    _max = str(max(results))[:6]
    _min = str(min(results))[:6]
    print(f'{_mean} ± {_std} s\n[{_min}, {_max}]')


if __name__ == '__main__':
    work(example_1)
    work(example_1it, True)

