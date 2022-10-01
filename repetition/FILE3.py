# name = ["f", "d", 7, True, False]
# name.append("hello")
# name.insert(5, "Imran")
# name.remove(7)
# del name[0]
# name[1] = "hi"
#
# name = [0, 9, 8, 7, 6, 5, 3, 4, 1, 2]
# name.sort()
# print(name)


# nominal = (1,3,6,8,45,67457,"1K","1M","50K")
# nominal = list(nominal)
# nominal[0]="hello"
# nominal[1]="Goodmorning"
# nominal = tuple(nominal)
# print(nominal)
# Games={
#     "Brawl Stars": 12,
#     12: "Brawl Stars",
#     "Nuls brawl": 1.12
# }
# Games["Nuls brawl"] = "Standoff"
# del Games[12]
# Games["Brawl Stars"] = 13
# for keys,values in Games.items():
#     print(f"{keys} - {values}")
# def=
# def plus(a,b,c):
#     print(a+b+c)
# plus(12,34,98)
# games = {
#     "Brawl Stars": {
#         "John": 10,
#         "Jack": 9
#     },
#     "Standoff": {}
# }
#
#
# def show():
#     for name, rates in games.items():
#         print(f"Game-{name}")
#         if len(rates) == 0:
#             print("Rating is not found!")
#         else:
#             print("Rates: ")
#             for user, rate in rates.items():
#                 print(f"{user}-{rate}")
#
#
# def add_game(game):
#     if game not in games.keys():
#         print("Game is not found")
#
#
# def add_rete(game):
#     if game not in game.keys():
#         print("Game is not found")
#     else:
#         name = str(input("Please write your name"))
#         rate = int(input("Please write your rating for Game"))
#         if rate < 0 or rate > 10:
#             print("rating must be 1 or 10")
#         else:
#             print(f"Game is grade:{name}-{rate}")
#
#
# def rate_view():
#     for game, rate in games.items():
#         rates = []
#         for i in rate.values():
#             rates.append(i)
#         if len(rates) == 0:
#             print("Rates in not found")
#         else:
#             print(f"{Games}-{sum(rates) / len(rates)}")
#
#
# while 1:
#     show()
#     command = int(input("\nWhrite your command(1-add game 2-add grade 3-show rates 0-exit)"))
#     print('-' * 50)
#     if command == 0:
#         print("Program end")
#         break
#     elif command == 1:
#         games = str(input("write new game!"))
#         add_game(games)
#         print("Game is good add")
#     elif command == 2:
#         Games = input("write game for add rates in film!")
#         add_rete(games)
#     elif command == 3:
#         rate_view()
#
#     else:
#         print("This command is not found")
class Car:
    def __init__(self, wheels, color, material):
        self.wheels = wheels
        self.color = color
        self.material = material

    def drive(self, when_press_drive):
        return f"the Car will "

    def __str__(self):
        return f"Wheels - {self.wheels}\n" \
               f"color - {self.color}\n" \
               f"material - {self.material}"
car1 = Car(wheels=True, color="red", material="metal")

class Mega_Car(Car):
    def __init__(self, wheels, color, material, motor, salon):
        super().__init__(wheels, color, material)
        self.motor = motor
        self.salon = salon

    def work(self, when_the_car_is_on_start_working):
        return f"the car will start working when the car will be on"

    def __str__(self):
        return f"motor - {self.motor}\n" \
               f"salon - {self.salon}"
car2 = Mega_Car(wheels=True, color="Black", material="Metal", motor=True, salon="beautiful")
print(Car)
print(Mega_Car)


