from contextlib import contextmanager

def result1(result): print(f'Answer for part 1: {result}')
def result2(result): print(f'Answer for part 2: {result}')

@contextmanager
def open_input(day):
    with open(f'day{day}.txt', 'r') as f:
        yield f
