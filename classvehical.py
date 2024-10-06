class Vehical:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
modelX=Vehical(240,20)
print("modelX max speed is" , modelX.max_speed)
print("modelX mileage is" , modelX.mileage)