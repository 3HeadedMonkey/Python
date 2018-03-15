i = 0
# declare the table [numbers]
numbers = []

while i < 6:
    # we print current value of i
     print(f"At the top i is {i}")
     # we strech table by sticking a bracet to it with value of current 'i'
     numbers.append(i)
     # while stopping condition, growing 'i'
     i +=1
     #printing the whole table from start till the end.
     # python prints tables in [bracets]
     print('Numbers now:', numbers)
     # printing the currebt 'i' number, notice that this number is bigger than the final table value do to the .append function being set before 'i +=
     print(f'At  the bottom i is {i}')
# print [tabela] prints out a full list [a b c d (...)]
print('The numbers: ')

for num in numbers:
    print(num)
    #for values (naming them 'num') in table [numbers] pritnt those values
    #as there is no 'end = ' ' after each print we will go \n
