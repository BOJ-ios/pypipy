def addAll(*args):
    return sum(args)


def mulAll(*args):
    # default 1
    result = 1
    for i in range(len(args)):
        result *= args[i]
    return result


def aMinusB(a, b):
    return a - b


def info():
    print("나만의 패키지")
