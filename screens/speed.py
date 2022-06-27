import RPi.GPIO as GPIO


class Speed():
    def __init__(self, lcd):
        self.is_running = True
        self.my_lcd = lcd
        self.velocidad = 100

    def __show(self):
        self.my_lcd.clear()
        self.my_lcd.lcd_display_string(f'Velocidad: {self.velocidad}%', 1)

    def show(self):
        self.__show()
        while self.is_running:
            if GPIO.input(self.BOTON_BAJAR) and self.velocidad != 0:
                self.velocidad -= 10
                while GPIO.input(self.BOTON_BAJAR):
                    pass
                self.__show()
            if GPIO.input(self.BOTON_SUBIR) and self.velocidad != 100:
                self.velocidad += 10
                while GPIO.input(self.BOTON_BAJAR):
                    pass
                self.__show_menu(0)
            if GPIO.input(self.BOTON_ENTER):
                while GPIO.input(self.BOTON_BAJAR):
                    pass
                self.is_running = False
        return self.velocidad
