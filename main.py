import RPi.GPIO as GPIO
import I2C_LCD_driver

lcd = I2C_LCD_driver.lcd()
BOTON_SUBIR = 14
BOTON_BAJAR = 4
BOTON_ENTER = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(BOTON_SUBIR, GPIO.IN)
GPIO.setup(BOTON_BAJAR, GPIO.IN)
GPIO.setup(BOTON_ENTER, GPIO.IN)
GPIO.setwarnings(False)

velocidad = 20
sentido = 1
vueltas = 0


def main():
    menu = 'home'
    while True:
        if menu == 'home':
            lcd.lcd_display_string("Velocidad      *", 1)
            lcd.lcd_display_string("Sentido", 2)


if __name__ == '__main__':

    main()
