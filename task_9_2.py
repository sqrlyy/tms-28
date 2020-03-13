any_dict = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4
}


func = lambda result_dict: {k * 2: v for k, v in result_dict.items()}
print(func(any_dict))
