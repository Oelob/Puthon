import random

def RandomList(number, edge_of_random):
    list = []
    for i in range(number):
        list.append(random.randint(0, edge_of_random))
    return list

def RandomFloatList(number, edge_of_random):
    list = []
    for i in range(number):
        list.append(random.uniform(0, edge_of_random))
    return list

