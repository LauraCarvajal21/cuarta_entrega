import I2C_LCD_driver

# import visuales
from screens.home import Home
from screens.speed import Speed

lcd = I2C_LCD_driver.lcd()

velocidad = 20
sentido = 1
vueltas = 0


def main():
    menu = 'home'
    while True:
        if menu == 'home':
            home = Home(lcd)
            menu = home.show()
        elif menu == 0:
            speed = Speed(lcd)
            velocidad = speed.show()
            menu = 'home'


if __name__ == '__main__':

    main()
