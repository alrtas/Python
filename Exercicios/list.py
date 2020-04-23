

bikeList=['ducati', 'yamaha', 'honda', 'suzuki']
print(bikeList[1])

bikeList.append('kawasaki')
bikeList.remove(bikeList[1])
print(bikeList[1])

bikeList.remove('suzuki')
print(bikeList[-1])

bikeList.append('yamaha')
bikeList.append('suzuki')
bikeList.append('aprila')
bikeList.append('bmw')

bikeList.sort()
print(bikeList)

bikeList.sort(reverse=True)
print(bikeList)
print(len(bikeList))

print("\n Novo exercicio \n")


places = ['new york', 'monaco', 'amsterda', 'rome', 'tokyo']
print(places)
print(places.sort())
print(places)
print(places.sort(reverse=True))
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print(len(places))

