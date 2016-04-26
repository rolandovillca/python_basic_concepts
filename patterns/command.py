class Switch(object):
    ''' The invoker class '''

    def __init__(self, flipUpCommand, flipDownCommand):
        self.__flipUpCommand = flipUpCommand
        self.__flipDownCommand = flipDownCommand

    def flipUp(self):
        self.__flipUpCommand.execute()

    def flipDown(self):
        self.__flipDowncommand.execute()

class Light(object):
    ''' The receiver class '''

    def turnOn(self):
        print 'The light is on'

    def turnOff(self):
        print 'the light is off'

class Command(object):
    ''' The command abstract class '''

    def __init__(self):
        pass

    def execute(self):
        pass

class FlipUpCommand(Command):
    ''' The Command class for turning on the light '''

    def __init__(self, light):
        super(FlipUpCommand, self).__init__()
        self.__light = light

    def execute(self):
        self.__light.turnOn()

class FlipDownCommand(Command):
    ''' The Command class for turning off the light '''

    def __init__(self, light):
        super(FlipDownCommand, self).__init__()
        self.__light = light

    def execute(self):
        self.__light.turnOff()

class LightSwitch(object):
    ''' The client class that represents the one that instanciates the
    encapulate object. '''

    def __init__(self):
        self.__lamp = Light()
        self.__switchUp = FlipUpCommand(self.__lamp)
        self.__switchOff = FlipDownCommand(self.__lamp)
        self.__switch = Switch(self.__switchUp, self.__switchOff)

    def switch(self, cmd):
        cmd = cmd.strip().upper()
        try:
            if cmd == 'ON':
                self.__switch.flipUp()
            elif cmd == 'OFF':
                self.__switch.flipDown()
            else:
                raise ValueError('Argument ON or OFF is required.')
        except ValueError as e:
            print 'Exception: {}'.format(e)

if __name__ == '__main':
    lightSitch = LightSwitch()
    lightSitch.switch('ON')
    lightSitch.switch('OFF')
    lightSitch.switch('abc')