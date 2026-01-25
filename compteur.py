compteur = 0
while compteur < 5:
    print(compteur)
    compteur +=1

fruits = ['pomme', 'banane', 'cerise']


for index, fruit in enumerate(fruits):
    print(f"Index {index} : {fruit}")

print(enumerate(fruits))
