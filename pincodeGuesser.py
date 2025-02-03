from itertools import permutations

knowns = input("Enter numbers: ")

numbers = list(map(int, knowns.split()))

possibilities = permutations(numbers)

for i in list(possibilities):
    print(i)