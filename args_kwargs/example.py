
def total(arr):
    t = 0
    for v in arr:
        t += v
    return t


def total_args(value, *args):
    t = value
    for v in args:
        t += v
    return t


def kwargs_example(**kwargs):
    for element in kwargs:
        print(element, kwargs[element])


print(total([1, 2, 3, 4, 5, 6, 7]))
print(total_args(10, 1, 2, 3, 4, 5, 6, 7))

kwargs_example(font='Arial', size='23px', color='blue')
