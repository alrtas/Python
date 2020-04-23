print("\n New Exercises \n ")
cars = ['bmw', 'mercedes', 'ford', 'subaru', 'toyota', 'audi']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


#Usando if em listas
print("\n New Exercises \n ")
request = []

if request:
    print('A fila não esta vazia')
else:
    print('A fila está vazia')

print("\n New Exercises \n ")
ingredientes_disponiveis = ['queijo', 'calabresa', 'massa', 'pepperoni', 'cebola', 'atum']
ingredientes_requeridos = ['massa', 'molho de tomate', 'calabresa', 'cebola']

for ing_req in ingredientes_requeridos:
    if ing_req in ingredientes_disponiveis:
        print("Adicionando: "+ing_req+".")
    else:
        print("O ingrediente "+ing_req+ " está indisponivel no momento.")
print("Pizza pronta!!")


print("\n New Exercises \n ")
users = ['admin', 'thiago', 'stevan', 'vitor', 'matheus', 'cristian']

if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user.title() + ", do you want to see the dashboard?")
        else:
            print("Hello "+user.title() + ", how are you?")
else:
    print("Precisamos encontrar alguns usuarios...")



print("\n New Exercises \n ")
users = ['admin', 'thiago', 'stevan', 'vitor', 'matheus', 'cristian']
new_users = ['admin', 'thIAgo', 'jose', 'ricardo', 'valmir', 'mathias']

if new_users:
    for new_user in new_users:
        if new_user.lower() in users:
            print("Usuario " + new_user.title() + ", já existe cadastro no sistema")
        else:
            print("Usuario " + new_user.title() + ", cadastrado com sucesso")
else:
    print('Nenhum usuario novo para ser adicionado')
