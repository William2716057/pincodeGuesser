from itertools import permutations

knowns = input("Enter numbers: ")

def space_add(number):
    return ' '.join(str(number))

def process_input(values):
    if ' '  in values:
        return values
    else:
        return space_add(values)
    
result = process_input(knowns)
numbers = list(map(int, result.split()))

possibilities = permutations(numbers)

for i in list(possibilities):
    print(i)
    
#iterations
for index in range(len(numbers)):
    #Copy numbers 
    modified = numbers.copy()
    # Append each number
    modified.append(modified[index])
    
    # Generate permutations using modified
    possibilities = set(permutations(modified))
    
    print(f"Possibilities with {modified[index]}: ")
    for i in possibilities:
        print(i)
    print() 