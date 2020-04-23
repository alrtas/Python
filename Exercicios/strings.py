name = str(input("Type your name "))
age = int(input("Type your age: "))


print("Hi, " +name.title()+", you have "+str(age)+" old")
if age > 18:
    print("And you can see any movie")
elif age <  18 and age > 13:
    print("And you can see a PG-13 movie")
else:
    print("And you can only see PG movies")

exit()
