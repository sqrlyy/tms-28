dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(dict1):
    key1 = f'{key}{len(key)}'
    dict1[key1] = dict1.pop(key)
print(dict1)
