FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def get_valid_temperature():
    while True:
        temperature_input = input("Enter the temperature to convert: ")
        if is_numeric(temperature_input):
            return float(temperature_input)
        else:
            print("Invalid temperature. Please enter a numeric value.")

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_valid_unit():
    valid_units = ['C', 'F']
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if unit in valid_units:
            return unit.upper()  # Return the uppercase version
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def convert_temperature():
    temperature = get_valid_temperature()
    unit = get_valid_unit()
    
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F")

def main():
    while True:
        convert_temperature()
        again = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

