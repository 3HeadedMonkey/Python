the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'qyartiers']

for number in the_count:
    print(f"this is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    # list.append(i) adds 'i' to the end of the list
    elements.append(i)
for i in elements:
    print(f"Element was: {i}")
