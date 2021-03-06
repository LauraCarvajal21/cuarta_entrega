import I2C_LCD_driver

# import visuales
from screens.home import Home
from screens.speed import Speed
from screens.direction import Direction
from screens.laps import Laps

lcd = I2C_LCD_driver.lcd()



def main():
    velocidad = 20
    sentido = 1
    
    menu = 'home'
    while True:
        if menu == 'home':
            home = Home(lcd)
            menu = home.show()
        elif menu == 0:
            speed = Speed(lcd)
            velocidad = speed.show()
            menu = 'home'
        elif menu == 1:
            direction=Direction(lcd)
            sentido = direction.show()
            menu = 'home'
        elif menu == 2:
            laps = Laps(lcd, velocidad,sentido)
            laps.show_and_run()
            menu = 'home'


if __name__ == '__main__':

    main()
