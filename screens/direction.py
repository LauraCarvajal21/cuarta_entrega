import RPi.GPIO as GPIO


class Direction():

    def __init__(self, lcd):
        self.is_running = True
        self.my_lcd = lcd
        self.sentido = 1

        self.BOTON_SUBIR = 14
        self.BOTON_BAJAR = 4
        self.BOTON_ENTER = 25
        GPIO.setup(self.BOTON_SUBIR, GPIO.IN)
        GPIO.setup(self.BOTON_BAJAR, GPIO.IN)
        GPIO.setup(self.BOTON_ENTER, GPIO.IN)

    def __show(self):
        self.my_lcd.lcd_clear()
        show_direction = '->'if self.sentido else '<-'
        self.my_lcd.lcd_display_string(f'Sentido: {show_direction}', 1)

    def show(self):
        self.__show()
        while self.is_running:
            if GPIO.input(self.BOTON_BAJAR):
                self.sentido=0
                while GPIO.input(self.BOTON_BAJAR):
                    pass
                self.__show()
            if GPIO.input(self.BOTON_SUBIR):
                self.sentido=1
                while GPIO.input(self.BOTON_SUBIR):
                    pass
                self.__show()
            if GPIO.input(self.BOTON_ENTER):
                while GPIO.input(self.BOTON_ENTER):
                    pass
                self.is_running = False
        return self.sentido
