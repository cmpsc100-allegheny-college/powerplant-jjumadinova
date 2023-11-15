# Import resource
from resources import Coal

class CoalGenerator:

    def __init__(self):
        self.coal = Coal()
        self.energy = 0

    def use(self):
        for ton in self.coal:
            #print(dir(ton))
            self.energy += ton.energy