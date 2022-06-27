import time
import RPi.GPIO as GPIO


class Laps():
    def __init__(self, lcd, velocidad, sentido):
        self.is_running = True
        self.my_lcd = lcd
        self.laps = 0
        self.speed = velocidad
        self.direction = sentido

        self.BOTON_SUBIR = 14
        self.BOTON_BAJAR = 4
        self.BOTON_ENTER = 25

        self.PinN1 = 23
        self.PinN2 = 24
        self.PWM = 18

        GPIO.setup(self.BOTON_SUBIR, GPIO.IN)
        GPIO.setup(self.BOTON_BAJAR, GPIO.IN)
        GPIO.setup(self.BOTON_ENTER, GPIO.IN)
        GPIO.setup(self.PWM, GPIO.OUT)
        GPIO.setup(self.PinN1, GPIO.OUT)
        GPIO.setup(self.PinN2, GPIO.OUT)




    def __show(self):
        self.my_lcd.lcd_clear()
        self.my_lcd.lcd_display_string(f'Vueltas: {self.laps}', 1)

    def show_and_run(self):
        pwm= GPIO.PWM(self.PWM,500)
        pwm.start(0)
        self.__show()
        while self.is_running:
            if GPIO.input(self.BOTON_BAJAR) and self.laps != 0:
                self.laps -= 1
                while GPIO.input(self.BOTON_BAJAR):
                    pass
                self.__show()
            if GPIO.input(self.BOTON_SUBIR):
                self.laps += 1
                while GPIO.input(self.BOTON_SUBIR):
                    pass
                self.__show()
            if GPIO.input(self.BOTON_ENTER):
                while GPIO.input(self.BOTON_ENTER):
                    pass
                self.my_lcd.lcd_clear()

                pwm.ChangeDutyCycle(self.speed)


                if self.direction==0:
                    GPIO.output(self.PinN1,False)
                    GPIO.output(self.PinN2,True)
                else:
                    GPIO.output(self.PinN1,True)
                    GPIO.output(self.PinN2,False)

                while self.laps != 0:
                    self.my_lcd.lcd_display_string(f'Quedan: {self.laps}', 1)
                    time.sleep(1)
                    self.laps -= 1

                self.is_running = False
        return self.laps
