from itertools import permutations

knowns = input("Enter numbers: ")

numbers = list(map(int, knowns.split()))

possibilities = permutations(numbers)

for i in list(possibilities):
    print(i)

#know that 1234 have been pressed but code requires 5 numbers 
#output all permutations where each number repeats once 

numbers.append(numbers[0])  

possibilities2 = set(permutations(numbers))

for i in possibilities2:
    print(i)