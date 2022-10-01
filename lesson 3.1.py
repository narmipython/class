# class Old_Tv:
#     def __init__(self, screen, wires, antenna, remote_controller, size):
#         self.screen = screen
#         self.wires = wires
#         self.antenna = antenna
#         self.remote_controller = remote_controller
#         self.size = size
#
#     def many_years_work(self, year):
#         return f"how many years your TV work - {year}years old"
#
#
#
#     def __str__(self):
#         return f"screen - {self.screen}\n" \
#                f"wires - {self.wires}\n" \
#                f"antenna - {self.antenna}\n" \
#                f"remote_controller - {self.remote_controller}\n" \
#                f"size - {self.size}"
# old_tv_1 = Old_Tv(screen="Display", wires="many", antenna="Old", remote_controller=True, size="640x420")
# print(old_tv_1.many_years_work(20))
# print(old_tv_1)
#
# class Modern_tv(Old_Tv):
#     def __init__(self, screen, wires, antenna, remote_controller, size, sensor, wifi_fi, games):
#         super().__init__(screen, wires, antenna, remote_controller, size)
#         self.sensor = sensor
#         self.wifi = wifi_fi
#         self.games = games
#
#     def new_games(self,new_game):
#         return f"show new games on your TV - {self.games}+{new_game}"
#
#
#     def __str__(self):
#         return  super(Modern_tv, self).__str__()+f"\nsensor - {self.sensor}\n" \
#                                                  f"WIFI - {self.wifi}\n" \
#                                                  f"игры - {self.games}"
# modern_tv_1 = Modern_tv(screen="Amoled Display",wires="a little",antenna="Cabel Antenna"
#                         remote_controller=True,size="1200x1600",sensor=True,wifi_fi=True,games="Tetris")
# print(modern_tv_1.many_years_work(10))
# print(modern_tv_1.new_games("Mario, Counter Strike"))
# print(modern_tv_1)


class Iphone:
    pass


class old_phone_1:
    def __init__(self, screen, charger, battery, camera, icon):
        self.screen = screen
        self.charger = charger
        self.battery = battery
        self.camera = camera
        self.icon = icon

    def many_years_work(self, year):
        return f"how many years your phone work - {year}years old"
    def __str__(self):
        return f"screen - {self.screen}\n" \
               f"charger - {self.charger}\n" \
               f"battery - {self.battery}\n" \
               f"camera - {self.camera}\n" \
               f"icon - {self.icon}"

    old_phone_1 = old_phone_1(screen="Display", charger="Samsung", battery="Android", camera="HD", icon="Samsung")
    print(old_phone_1.many_years_work(8))
    print(old_phone_1)

    class Iphone(old_phone_1):
     def __init__(self, screen, charger, battery, camera, icon, super_camera, new_icon):
         super().__init__(screen, charger, battery, camera, icon)
         self.super_camera = super_camera
         self.new_icon = new_icon

         def games(self, new_games):
          return f"show new games on your phone - {self.games}+{games}"

         def __str__(self):
              return  super(Iphone, self).__str__()+f"\nsuper_camera - {self.super_camera}\n" \
                                                    f" - new_icon{self.new_icon}"

    print(Iphone.many_years_work(8))
    print(Iphone.games("Brawl stars, Counter Strike"))
    print(Iphone)

    class Old_phone_1:
        def _init_(self, screen, charger, battery, camera, icon):
            self.screen = screen
            self.charger = charger
            self.battery = battery
            self.camera = camera
            self.icon = icon

        def many_years_work(self, year):
            return f"how many years your phone work - {year}years old"

        def _str_(self):
            return f"screen - {self.screen}\n" \
                   f"charger - {self.charger}\n" \
                   f"battery - {self.battery}\n" \
                   f"camera - {self.camera}\n" \
                   f"icon - {self.icon}"

    old_phone_1 = Old_phone_1(screen="Display", charger="Samsung", battery="Android", camera="HD", icon="Samsung")
    print(old_phone_1.many_years_work(8))
    print(old_phone_1)

    class Iphone(Old_phone_1):
        def _init_(self, screen, charger, battery, camera, icon, new_icon, super_camera):
            super()._init_(screen, charger, battery, camera, icon)
            self.new_icon = new_icon
            self.super_camera = super_camera

        def _str_(self):
            return super(Iphone, self)._str_() + f'/new_icon - {self.new_icon}\n' \
                                                 f'supercamera- {self.super_camera}'

    iphone1 = Iphone(screen='123', charger='123', battery='1234', camera='1234', icon='1234', new_icon='123',
                     super_camera='123')
    print(iphone1)


