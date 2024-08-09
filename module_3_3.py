def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(1, 2)
print_params(c=[1, 2, 3])

values_list = [1, 'list', False]
values_dict = {'a': 2, 'b': "name", 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [45, 'noname']
print_params(*values_list_2, 42)