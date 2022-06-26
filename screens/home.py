class Home():
    def __init__(self,lcd)->None:
        self.is_running=True
        self.my_lcd=lcd

    def __show_menu(self):
        self.my_lcd.lcd_clear()
        self.my_lcd.lcd_display_string("Velocidad      *", 1)
        self.my_lcd.lcd.lcd_display_string("Sentido", 2)

    def show(self):
        self.__show_menu()   
