# Import resource
from resources import Solar

class SolarPanel(Solar): 

    def __init__(self, wattage: int = 250):
        self.wattage = wattage
        super().__init__()