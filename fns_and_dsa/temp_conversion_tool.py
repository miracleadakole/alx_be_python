# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32)* FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    try:
        #Get user input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # perform conversion based on user input
        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else: 
            print("Invalid unit. Please enter 'C' for celsius or 'F' for Fahrenheit")

    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")