def delete_even(function):
    def wrapper(arg):
        arg = [i for i in arg if i % 2 != 0]
        return function(arg)
    return wrapper


@delete_even
def print_arg(any_list):
    for i in any_list:
        print(i)


list_of_numbers = [int(input()) for i in range(7)]
print_arg(list_of_numbers)
