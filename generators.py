#bellek te daha az yer tutmasını sağlamak

""" def cube():
    result =[]

    for i in range(5):
        result.append (i**3)
    return result

print(cube) """


""" def cube():
    
    for i in range(5):
        yield i**3

Generator = cube ()

iterator =iter(Generator)
print(next (iterator))
print(next (iterator))
print(next (iterator))
print(next (iterator))
print(next (iterator))

print(next (iterator)) """

#//////////////////////////////
#liste = [i**3 for i in range (5)]
liste = (i**3 for i in range (5))

print(liste)
for i in liste:
    print(i)