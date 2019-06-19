# 8.
# Pizza Party

from inputplus import input_int

print("How many people?")
people = input_int()
print("How many pizzas do you have?")
pizzas = input_int()

slices = 8 * pizzas // people
leftovers = 8 * pizzas % people

if people == 1 & pizzas > 1:
    print(f"""{people} person with {pizzas} pizzas.
She or he gets {slices} pieces of pizza.
There are {leftovers} leftover pieces.""")
elif people > 1 & pizzas == 1:
    print(f"""{people} people with {pizzas} pizza.
Each person gets {slices} pieces of pizza.
There are {leftovers} leftover pieces.""")
elif people == 1 & pizzas == 1:
    print(f"""{people} person with {pizzas} pizza.
She or he gets {slices} pieces of pizza.
There are {leftovers} leftover pieces.""")
else:
    print(f"""{people} people with {pizzas} pizzas.
Each person gets {slices} pieces of pizza.
There are {leftovers} leftover pieces.""")
