def methodception(another):
    return another()

def add_two_numbers():
    return 30 + 30

print(methodception(add_two_numbers))
print(methodception(lambda: 35 + 35))

my_list = [13,56,77,484]

def not_thirteen(x):
    return x != 13

print([x for x in my_list if x != 13])
