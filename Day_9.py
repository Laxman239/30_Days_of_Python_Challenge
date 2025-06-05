# Challenge Day 9
# Extend Car into an ElectricCar subclass with battery capacity

class Car:
    def __init__(self, brand_name, model_name):
        self.brand_name = brand_name
        self.model_name = model_name

    def display(self):
        print(f"🚗 Brand: {self.brand_name}")
        print(f"📝 Model: {self.model_name}")

        if self.model_name.lower() == "lexus":
            print("✨ Luxury Car")
            print("⚡ Accelerates from 0 to 60 mph in less than 4.4 seconds")
        elif self.model_name.lower() == "cybertruck":
            print("🔋 Electric Vehicle")
            print("⚡ Accelerates from 0 to 60 mph in less than 4.8 seconds")
        else:
            print("🚗 Standard Model")

    def brand_info(self):
        if self.brand_name.lower() == "toyota":
            print("🔧 Manufactures both conventional fuel and EV vehicles.")
        elif self.brand_name.lower() == "tesla":
            print("🔋 Manufactures only EVs.")
        else:
            print("ℹ️ Brand information not available.")


class ElectricCar(Car):
    def __init__(self, brand_name, model_name):
        super().__init__(brand_name, model_name)
        # Initialize battery capacity based on brand
        if self.brand_name.lower() == "toyota":
            self.battery_capacity_value = "71.4kWh"
        elif self.brand_name.lower() == "tesla":
            self.battery_capacity_value = "123kWh"
        else:
            self.battery_capacity_value = "Information not available."

    def display_battery_capacity(self):
        print(f"🔋 Battery Capacity: {self.battery_capacity_value}")


# Creating objects
toyota = ElectricCar("Toyota", "Lexus")
tesla = ElectricCar("Tesla", "Cybertruck")

# Display information
toyota.display()
toyota.brand_info()
toyota.display_battery_capacity()
print("\n")
tesla.display()
tesla.brand_info()
tesla.display_battery_capacity()
