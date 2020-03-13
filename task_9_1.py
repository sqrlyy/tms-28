list_of_strings = ['first', 'second', 'third', 'fourth', 'fifth']
print(list_of_strings)
list_of_strings = [f'{i} - {string}' for i, string in enumerate(list_of_strings)]
print(list_of_strings)
