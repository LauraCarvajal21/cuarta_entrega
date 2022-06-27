import RPi.GPIO as GPIO


class Home():
    def __init__(self, lcd) -> None:
        self.is_running = True
        self.my_lcd = lcd
        self.OPTIONS = ['PWM', 'DIRECCION', '# VUELTAS']
        self.BOTON_SUBIR = 14
        self.BOTON_BAJAR = 4
        self.BOTON_ENTER = 25

        self.position = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BOTON_SUBIR, GPIO.IN)
        GPIO.setup(self.BOTON_BAJAR, GPIO.IN)
        GPIO.setup(self.BOTON_ENTER, GPIO.IN)
        GPIO.setwarnings(False)

    def __show_menu(self, bajando):
        self.my_lcd.lcd_clear()

        new_option = self.OPTIONS[self.position - bajando:self.position+2-bajando]
        print(new_option)
        self.my_lcd.lcd_display_string(new_option[0], 1, 3)
        self.my_lcd.lcd_display_string(new_option[1], 2, 3)

        self.my_lcd.lcd_display_string('->', bajando+1)

    def show(self):
        self.__show_menu(0)
        while self.is_running:
            if GPIO.input(self.BOTON_BAJAR) and self.position != len(self.OPTIONS)-1:
                self.position += 1
                while GPIO.input(self.BOTON_BAJAR):
                    pass
                self.__show_menu(1)
            if GPIO.input(self.BOTON_SUBIR) and self.position != 0:
                self.position -= 1
                while GPIO.input(self.BOTON_BAJAR):
                    pass
                self.__show_menu(0)
