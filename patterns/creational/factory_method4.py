# Interfaz:
class Pizza(object):
    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price

# The first type of pizza:
class HamAndMushroomPiza(Pizza):
    def __init__(self):
        self._price = 8.5

# The second type of pizza:
class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 10.5

# The third type of pizza:
class HawaiianPiza(Pizza):
    def __init__(self):
        self._price = 11.5

# Factory class - generator of objects:
class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'HamMushroom':
            return HamAndMushroomPiza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Hawaiin':
            return HawaiianPiza()

if __name__ == '__main__':
    pizza_factory = PizzaFactory.create_pizza('Hawaiin')
    print pizza_factory._price