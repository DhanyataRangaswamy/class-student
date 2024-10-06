class Parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=Parrot('blu',10)
woo=Parrot('woo',15)
print("Blue is {}".format(blu.species))
print("Woo is also {}".format(woo.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))