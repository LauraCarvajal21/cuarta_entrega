import RPi.GPIO as GPIO


class Home():
    def __init__(self, lcd) -> None:
        self.is_running = True
        self.my_lcd = lcd
        self.OPTIONS = [{'option': 1, 'text': 'PWM'},
                        {'option': 2, 'text': 'DIRECCION'},
                        {'option': 3, 'text': '# VUELTAS'}]
        self.BOTON_SUBIR = 14
        self.BOTON_BAJAR = 4
        self.BOTON_ENTER = 25

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BOTON_SUBIR, GPIO.IN)
        GPIO.setup(self.BOTON_BAJAR, GPIO.IN)
        GPIO.setup(self.BOTON_ENTER, GPIO.IN)
        GPIO.setwarnings(False)

    def __show_menu(self):
        self.my_lcd.lcd_clear()
        self.my_lcd.lcd_display_string(self.OPTIONS[0].get('text'),1,3)
        self.my_lcd.lcd_display_string(self.OPTIONS[1].get('text'),2,3)
        self.my_lcd.lcd_display_string('->',1)
    def show(self):
        self.__show_menu()
