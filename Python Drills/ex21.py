def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a}/ {b}")
    return a/ b

print("Let's do some math with just functions!")

age = add(20, 5)
height = substract(90, 6)
weight = multiply(20, 4)
iq = divide(200, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, iq: {iq}")

print("\n\n Here' a puzzle.")

what = add(age, substract(height, multiply(weight,(divide(iq,2)))))
print ("That becomes: ", what,"\n Can you do it by hand?")
