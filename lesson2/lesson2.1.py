# class Car:
#     def __init__(self,motor,wheels,marki,colors,light,drive,cost):
#         self.motor = motor
#         self.wheels = wheels
#         self.marki = marki
#         self.colors = colors
#         self.light = light
#         self.drive = drive
#         self.cost = cost
#     def tunning(self, cost_tunning):
#         summa = cost_tunning + self.cost
#         return f"Итоговая цена за тюннинг вместе с машиной будет - {summa}$"
#
#     def __str__(self):
#         return f"Motor - {self.motor}\n" \
#                f"wheels - {self.wheels}\n" \
#                f"Marki - {self.marki}\n" \
#                f"colors - {self.colors}\n" \
#                f"light - {self.light}\n" \
#                f"drive - {self.drive}\n" \
#                f"cost - {self.cost} $"
#
# car1 = Car(motor=1.6,wheels="195/65 R15", marki="Toyota",colors="White", light="Ksenon",drive="AT",cost=15000)
# print(car1.tunning(2000))
# print(car1)
#
# class Electric_Car(Car):
#     def __init__(self, motor, wheels, marki, colors, light, drive, cost,charger,battery):
#         super().__init__(motor, wheels, marki, colors, light, drive, cost)
#         self.charger = charger
#         self.battery = battery
#     def __str__(self):
#         return super(Electric_Car, self).__str__()+f"\ncharger-{self.charger}battery-{self.battery}"

class Animal:
        def __init__(self,legs,hands,eyes,stomach,bones,teeth):
            self.legs = legs
            self.hands = hands
            self.eyes = eyes
            self.stomach = stomach
            self.bones = bones
            self.teeth = teeth
        def __str__(self):
            return f"legs - {self.legs}\n" \
                   f"hands - {self.hands}\n" \
                   f"eyes - {self.eyes}\n" \
                   f"stomach - {self.stomach}\n" \
                   f"bones - {self.bones}\n" \
                   f"teeth - {self.teeth}"
class Cat(Animal):
    def __init__(self, legs, hands, eyes, stomach, bones, teeth):
        super().__init__(legs, hands, eyes, stomach, bones, teeth)
    def __str__(self):
        return super(Cat,self).__str__()
cat1 = Cat(legs="small",hands="small",eyes="green",stomach="small",bones="strong",teeth="sharp")
cat2 = Cat(legs="big",hands="small",eyes="blue",stomach="fat",bones="light",teeth="sharp")
print(cat1)
print('-'*20)
print(cat2)
class Dog(Animal):
    def __init__(self, legs, hands, eyes, stomach, bones, teeth):
        super().__init__(legs, hands, eyes, stomach, bones, teeth)
    def __str__(self):
        return super(Dog, self).__str__()
dog1 = Dog(legs="big",hands="small",eyes="yellow",stomach="week",bones="strong",teeth="sharp")
dog2 = Dog(legs="big",hands="big",eyes="blue",stomach="fat",bones="strong",teeth="sharp")
print(dog1)
print('-'*20)
print(dog2)







