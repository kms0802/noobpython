class Machine:
    def __init__(self, model, power):
        self.model = model
        self._power = power

class Washer(Machine):
    def __init__(self, model, power):
        super().__init__(model, power)
        self._power -= 10
    
    def status(self):
        print(f"{self.model} {self._power}")

wash = Washer("주행", 20)
wash.status()