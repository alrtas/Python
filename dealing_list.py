magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())



print("\n New Exercises \n ")

pizzas = ('bacon', 'chese', 'pepperoni')

for pizza in pizzas:
    print("I like " + pizza.title() +" pizza")
print("I really like this " + str(len(pizzas)) + " pizzas")


print("\n New Exercises \n ")

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for value in range (1,11):
    squares.append(value**2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#makes a for inside a range and append automatic, same code as line 25
squares1 = [value**2 for value in range(1,11)]
print(squares1)
print("\n New Exercises \n ")
twenty = list(range(1,21))
print(twenty)

milion = list(range(1,1000000))
print(min(milion))
print(max(milion))
print(sum(milion))

even_numbers_3 = list(range(3,31,3))
print(even_numbers_3)

cubes = [value**3 for value in range(1,10)]
print(cubes)
print("\n New Exercises \n ")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Printing players: '+str(players))
print("Printing 3 firsts players: " + str(players[0:3]))

print("\n New Exercises \n ")

myFoods = ['pizza', 'falafel', 'carrot cake']
friendFood = myFoods[:] # This copy one list to another
# friendFood = myFood -> this connect this two, if one changes, others changes to

print('My favorites foods are: '+ str(myFoods))
print('My friends favorites foods are: '+ str(friendFood))

#tuplas sao  listas imutaveis

dimensions = (250, 50)

