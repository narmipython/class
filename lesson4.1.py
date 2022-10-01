class Car:
    def __init__(self, motor, wheels, lights):
        self.motor = motor
        self.wheels = wheels
        self.lights = lights
    def work(self, on_when_press):
        return f"the motor whill be {on_when_press}"

    def __str__(self):
        return f"motor - {self.motor}\n" \
               f"mouse - {self.wheels}\n" \
               f"keyboards - {self.lights}"
Lamba = Car(motor="lamba1", wheels="lamborgini", lights=True)

print(Lamba.work("on_when_press"))

class Second_car(Car):
    def __init__(self, motor, wheels, lights, super_motor):
        super().__init__(motor, wheels, lights)
        self.super_motor = super_motor
    def work_faster(self, working_good):
        return f"your motor is  {working_good}"

    def __str__(self):
        return super(Second_car, self).__str__()+f"\nsuper_motor - {self.super_motor}"

lamba_huracan = Second_car(motor="lamba+", wheels="lamba1superplus", lights=True, super_motor=True)
print(lamba_huracan.work("on_when_press"))
print(lamba_huracan.work_faster("working_good"))

class Third_car(Second_car):
    def __init__(self, motor, wheels, lights, super_motor, good_salon):
        super().__init__(motor, wheels, lights, super_motor)
        self.good_salon = good_salon

    def soft_seats(self, soft_seats):
        return f"this car has  {soft_seats}"

    def __str__(self):
        return super(Third_car, self).__str__()+f"\nseats {self.good_salon}"

lamba_ultra = Third_car(motor="new+", wheels="ultra+1", lights=False, super_motor=True, good_salon=True)
print(lamba_ultra.work("on_when_press"))
print(lamba_ultra.work_faster(True))
print(lamba_ultra.soft_seats(True))
