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

print(sum_tem(5)(1))

#### built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 30]
# Map
def multiply_two(numbers):
  return numbers *2    

print(list(map(multiply_two,numbers)))
print(list(map(lambda number:number * 2,numbers)))

# Filter

def filter_greater_ten(number):
    if number>10:
        return True
    return False
    
print(list(filter(filter_greater_ten,numbers)))
print(list(filter(lambda number: number>10,numbers)))

# Reduce

reduce()
