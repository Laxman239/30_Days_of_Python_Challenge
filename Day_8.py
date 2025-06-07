# Challenge Day 8
# Create a Car class with attributes and display method

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

# Creating objects
toyota = Car("Toyota", "Lexus")
tesla = Car("Tesla", "Cybertruck")

# Display information
toyota.display()
toyota.brand_info()
print("\n")  # Print a blank line for clarity
tesla.display()
tesla.brand_info()
