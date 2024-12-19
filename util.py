from contextlib import contextmanager


def result1(result): print(f'Answer for part 1: {result}')


def result2(result): print(f'Answer for part 2: {result}')


@contextmanager
def open_input(day):
    with open(f'day{day}.txt', 'r') as f:
        yield f


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


def with_print(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join([f'{k}={v}' for k, v in kwargs.items()])
        print(f'{func.__name__}({args_str}, {kwargs_str}) -> {result}')

        return result

    return wrapper
