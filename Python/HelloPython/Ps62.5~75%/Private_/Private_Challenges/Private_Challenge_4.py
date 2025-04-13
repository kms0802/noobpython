class Device:
    def __init__(self, brand, battery):
        self.brand = brand
        self._battery = battery
    
class Smartphone(Device):
    def __init__(self, brand, battery):
        super().__init__(brand, battery)
        self._battery -= 15

    def show_status(self):
        print(f"브랜드명: {self.brand} / 베터리: {self._battery}%")

phone = Smartphone("삼성", 50)
phone.show_status()