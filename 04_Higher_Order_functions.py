#### Higher Order Functions ###

def sum_one(value):
    return value + 1

def sum_two_values_and_one(first_values, second_values):
    return sum_one(first_values+second_values)

print(sum_two_values_and_one(5, 2))