def switch_decor(func):
    def wrapper(x, y, z):
        return func(z, y, x)
    return wrapper


@switch_decor
def any_func(a, b, c):
    print(f'a = {a}, b = {b}, c = {c} ')


any_func(1, 2, 3)


