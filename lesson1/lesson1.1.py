class Games:
    def __init__(self,title,interest_grade,price):
        self.title = title
        self.interest_grade = interest_grade
        self.price = price
    def run(self):
        return f"{self.title} can be run"

    def search_in_game(self):
        return f"{self.title}can be search in game"


    def __str__(self):
        return f"Title:{self.title}\n" \
               f"interest_grade:{self.interest_grade}\n" \
               f"price:{self.price}"
game1 = Games(title="Brawl-stars",interest_grade="10/10",price=0)
print(game1.run())
game2 = Games(title="Roblox",interest_grade="10/10",price=0)
print(game2.search_in_game())
print(game1)
print(game2)































# class Dog:
#     def __init__(self,breed,color,name,gender,age):
#         self.breed = breed
#         self.color = color
#         self.name = name
#         self.gender = gender
#         self.age = age
#
#     def __str__(self):
#         return f"breed:{self.breed}\n" \
#                f"color:{self.color}\n" \
#                f"name:{self.name}\n" \
#                f"gender:{self.gender}\n" \
#                f"age:{self.age}"
# dog1 = Dog(breed="britan shepherd",color="white",name="shepherd",gender="male",age=2)
# dog2 = Dog(breed="English buldog",color="black",name="buldog",gender="female",age=4)
# print(dog1)
# print(dog2)