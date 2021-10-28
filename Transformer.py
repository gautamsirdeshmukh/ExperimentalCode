Type1_object = [[1,3,5],[]]
Type2_object = [[],[2,4,6]]

def Type1(Type2_object):
    object = Type2_object
    object[0] = object[1]
    object[1] = []
    return object

def Type2(Type1_object):
    object = Type1_object
    object[1] = object[0]
    object[0] = []
    return object

print(f'Version 1: {Type1_object}')
new = Type2(Type1_object)
print(f'Version 2: {new}')
new = Type1(new)
print(f'Version 3: {new}')
