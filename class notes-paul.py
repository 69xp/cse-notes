# defining a class
class Cheeseburger(object):
    def __init__(self, patty_type, cheese):
        #2 underscores before and after
        self.patty = patty_type
        self.cheese = cheese
        self.eaten =False

    def give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("you cut the cheeseburger")

    def eat(self):
        print("you ate the cheeseburger.")
        self.eaten = True


burger1 = Cheeseburger("Beef", "Cheddar", )
burger2 = Cheeseburger("Bacon", "Swiss")

print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)


class Car(object):
    def __init__(self, name, color, num_of_doors, hp, ):
        self.color = color
        self.name = name
        self.doors = num_of_doors
        self.HP = hp
        self.running = False
        self.passengers = 0
        self.AC = True

    def turn_on(self):
        if self.running:
            print("nothing happens")
        else:
            print("the car starts")

    def move_forward(self):
        if self.running:
            print("you moved forward")
        else:
            print("nothing happens")

    def turn_off(self):
        if self.running:
            self.running = False
            print("your car turned off by itself")
        else:
            print("the car is already off")
    def go_for_a_drive(self, passengers):
        print("%d passengers get in." % passengers)
        self.passengers = passengers
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out" % passengers)
        self.passengers = 0
