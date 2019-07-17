name = input("Type your name ")
if name.isnumeric():
    print("Somente letras..")
    exit()
else:
    print(name.title())

age = input("Type your age: ")
if age.isnumeric():
    print(age)
else:
    print("Somente numeros..")
    exit()


print("Hi, " +name+", you have "+age+" old")
