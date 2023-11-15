import json

# Import libraries
from CoalStation import CoalGenerator

# TODO: Write charge_battery function to store power generated
#       in .battery file

def main():
    
    coal_plant = CoalGenerator()
    coal_plant.use()
    print(coal_plant.energy)
    # TODO: Create power generation objects and run them

    # TODO: Call charge_battery to store the energy created

if __name__ == "__main__":
    main()