#### Higher Order Functions ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5
def sum_two_values_and_one(first_values, second_values,sum_one):
    return sum_one(first_values+second_values)

print(sum_two_values_and_one(5, 2,sum_one))
print(sum_two_values_and_one(5, 2,sum_five))

### Closures ###


def sum_tem(original_value):
    def add(value):
        return value + 10 +original_value
    return add   

add_closure = sum_tem(1)
print(add_closure(5))