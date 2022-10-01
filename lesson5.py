# Gimn = open("gim.txt", "r", encoding="UTF-8")
# print(Gimn.read())
# Gimn.close()
# stix = open("text.txt", "r", encoding="UTF-8")
# print(stix.read())
# stix.close()
# with open("games", "w", encoding="UTF-8")as text:
#     text.write(input("write your favourite games"))
#     print(text)
# with open("games", "a", encoding="UTF-8")as text:
#     text.write(input("write something ?"))
#    print(text)
# with open("games", "w", encoding="UTF-8")as text:
#     text.write(input("what is your name ?"))
#     text.write(input("what is your hobby ?"))
#     print(text)
class Brawl_stars:
    def __init__(self, brawlers, skins):
        self.brawlers = brawlers
        self.skins = skins

    def run(self, when_press_run):
        return f"the brawler will run"

    def __str__(self):
        return f"brawlers - {self.brawlers}\n" \
               f"skins - {self.skins}"


brawl = Brawl_stars(brawlers="58brawlers", skins="beautiful")


class Brawl_stars2(Brawl_stars):
    def __init__(self, brawlers, skins, gems, mods):
        super().__init__(brawlers, skins)
        self.gems = gems
        self.mods = mods

    def add_gems(self, when_buy_add):
        return f"the gems will be added to your account when you will by them!"
brawl2 = Brawl_stars2(brawlers="59new", skins="more beautiful", gems=True, mods="New")

class Brawl_stars_3(Brawl_stars2):
    def __init__(self, brawlers, skins, gems, mods, money, new_season):
        super().__init__(brawlers, skins, gems, mods)
        self.money = money
        self.new_season = new_season

    def New_season(self, after_2_moth_new):
        return f"new season will start after 2 month!"
brawl3 = Brawl_stars_3(brawlers="60new", skins="NEW", gems=True, mods="robots_new", money=True, new_season=True)
print(brawl)
print(brawl2)
print(brawl3)
