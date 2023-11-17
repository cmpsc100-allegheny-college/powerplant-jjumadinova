import json

# Import libraries
from CoalStation import CoalGenerator
from SolarField import SolarPanel

def charge_battery(energy: dict = {}):
    """Charge_battery function to store power generated
          in .battery file"""
    with open(".battery", "r") as file:
        data = json.load(file)

    # Aggregate generated energy
    data["coal"] += energy["coal"]

    # Write data to json
    with open(".battery", "w") as file:
        json.dump(data, file)   

def main():
    
    coal_plant = CoalGenerator()
    coal_plant.use()
    print(coal_plant.energy)

    solar_panel1 = SolarPanel()

    # Charge battery
    charge_battery(
        {
            "solar": solar_panel1.power, 
            "coal": coal_plant.energy
        }
    )

    # TODO: Create power generation objects and run them

    # TODO: Call charge_battery to store the energy created

if __name__ == "__main__":
    main()