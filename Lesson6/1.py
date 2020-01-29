from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self, color):
        if color == 'red':
            self.__color = color
            print('red')
            sleep(7)
        elif color == 'yellow' and self.__color == 'red':
            self.__color = color
            print('yellow')
            sleep(2)
        elif color == 'green' and self.__color == 'yellow':
            self.__color = color
            print('green')
            sleep(3)
        else:
            print('Error')


light = TrafficLight()
light.running('red')
light.running('yellow')
light.running('green')
light.running('green')
