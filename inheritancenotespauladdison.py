class Vehicle(object):
    def __init__(self, source, material, seat, speed, passengers):
        self.power_source = source
        self.material = material
        self.seat_location = seat
        self.max_speed = speed
        self.passengers = passengers

    def move(self):
        print('you have moved forward')

    def change(self):
        print('you have changed directions')


class Car(Vehicle):
    def __init__(self,material, seat, speed, passengers, windows):
        super(Car, self).__init__('engine', material, seat, speed, passengers)
        self.windows = windows

    def roll_down_windows(self):
        print('you rolled windows down')

    def turn_on(self):
        print('you turn the key and the engine starts.')
test_car = Car('aluminum linoleum','plush, drivers side', 360, 3, True)

class keylesscar(Car):
    def __init__(self, material, seat, speed, passengers, windows):
        super(keylesscar, self).__init__(material, seat, speed, passengers, windows)

    def turn_on(self):
        print('you pushed the button and the car turned on')

cool_car = keylesscar('aluminum linoleum','plush, drivers side', 360, 3, True)


class Tesla(Car):
    def __init__(self, material, seat, speed, passengers, windows):
        super(Tesla, self).__init__(material, seat, speed, passengers, windows)


    def fly(self):
        print("the earth falls, thereby allowing you(and your car) to fly")


    def turn_on(self):
        Car.turn_on(self)
