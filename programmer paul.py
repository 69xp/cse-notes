class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age):
        super(Employee, self).__init__(name, age)


    def cannot_think(self):
        print('%s cannot think and starts daydreaming.' % self.name)


class Programmer(Employee):
    def __init__(self, name, age):
        super(Programmer, self).__init__(name, age)

    def death(self):
        print('%s has died of paralytic boredom...' % self.name)
