class Dog:
    species="Dog"
    def __init__(self,breed,age):
        self.breed=breed
        self.age=age
a=Dog('Beagle',4)
b=Dog('German Shepherd',2)
print("Crusoe is a {} , he is {} and {} years old".format(a.species,a.breed,a.age))
print("Lina is a {} , she is {} and {} years old".format(b.species,b.breed,b.age))