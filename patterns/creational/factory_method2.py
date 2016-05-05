class Car(object):

    def factory(type_car):
        if type_car == 'Racecar':
            return Racecar()
        if type_car == 'Van':
            return Van()
        assert 0, 'Bad car creation: {}'.format(type_car)

    factory = staticmethod(factory)

class Racecar(Car):
    def drive(self): print('Racecar driving...')

class Van(Car):
    def drive(self): print('Van driving...')

# Create objects using factory:
racecar = Car.factory('Racecar')
racecar.drive()

vancar = Car.factory('Van')
vancar.drive()