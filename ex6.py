types_of_people = 10
x = f"The are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who now {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")
# We are setting the value 'hilarious'
hilarious = False
# We are setting a string with a 'juncion'
joke_evaluation = "Isn't that joke so funny?! {}"
# We are formating the hilarious value into a string and we are adding it wo the
# joke evaluation string with the help of a junction?
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
