n1 = range(10)
s = sum([x for x in n1])

print('Total Sum is using List comprehension ' + str(count))

Square = [x*2 for x in n1]
print(Square)

Square_even = [x*2 for x in n1 if x % 2 != 0]
print(Square_even)
