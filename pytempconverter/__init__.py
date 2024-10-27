import argparse
from enum import Enum

class UnsupportedUnitError(Exception):
    """Exception raised for unsupported temperature unit conversions."""
    pass

class SameUnitConversionError(Exception):
    """Exception raised for converting between the same temperature units."""
    pass

class Unit(Enum):
    CELSIUS = "Celsius"
    FAHRENHEIT = "Fahrenheit"
    KELVIN = "Kelvin"
    RANKINE = "Rankine"
    REAUMUR = "Reaumur"

class TemperatureConverter:
    """
    TemperatureConverter class provides methods to convert temperature values between various units.
    """
    @staticmethod
    def convert(temperature, from_unit, to_unit, precision=2):
        if from_unit == to_unit:
            raise SameUnitConversionError("Cannot convert between the same temperature units.")

        conversion_methods = {
            (Unit.CELSIUS, Unit.FAHRENHEIT): TemperatureConverter._celsius_to_fahrenheit,
            (Unit.CELSIUS, Unit.KELVIN): TemperatureConverter._celsius_to_kelvin,
            (Unit.CELSIUS, Unit.RANKINE): TemperatureConverter._celsius_to_rankine,
            (Unit.CELSIUS, Unit.REAUMUR): TemperatureConverter._celsius_to_reaumur,
            (Unit.FAHRENHEIT, Unit.CELSIUS): TemperatureConverter._fahrenheit_to_celsius,
            (Unit.FAHRENHEIT, Unit.KELVIN): TemperatureConverter._fahrenheit_to_kelvin,
            (Unit.FAHRENHEIT, Unit.RANKINE): TemperatureConverter._fahrenheit_to_rankine,
            (Unit.FAHRENHEIT, Unit.REAUMUR): TemperatureConverter._fahrenheit_to_reaumur,
            (Unit.KELVIN, Unit.CELSIUS): TemperatureConverter._kelvin_to_celsius,
            (Unit.KELVIN, Unit.FAHRENHEIT): TemperatureConverter._kelvin_to_fahrenheit,
            (Unit.KELVIN, Unit.RANKINE): TemperatureConverter._kelvin_to_rankine,
            (Unit.KELVIN, Unit.REAUMUR): TemperatureConverter._kelvin_to_reaumur,
            (Unit.RANKINE, Unit.CELSIUS): TemperatureConverter._rankine_to_celsius,
            (Unit.RANKINE, Unit.FAHRENHEIT): TemperatureConverter._rankine_to_fahrenheit,
            (Unit.RANKINE, Unit.KELVIN): TemperatureConverter._rankine_to_kelvin,
            (Unit.RANKINE, Unit.REAUMUR): TemperatureConverter._rankine_to_reaumur,
            (Unit.REAUMUR, Unit.CELSIUS): TemperatureConverter._reaumur_to_celsius,
            (Unit.REAUMUR, Unit.FAHRENHEIT): TemperatureConverter._reaumur_to_fahrenheit,
            (Unit.REAUMUR, Unit.KELVIN): TemperatureConverter._reaumur_to_kelvin,
            (Unit.REAUMUR, Unit.RANKINE): TemperatureConverter._reaumur_to_rankine,
        }

        try:
            conversion_method = conversion_methods[(from_unit, to_unit)]
            return round(conversion_method(temperature), precision)
        except KeyError:
            raise UnsupportedUnitError("Unsupported temperature unit conversion requested.")

    @staticmethod
    def _celsius_to_fahrenheit(temp):
        return (temp * 9/5) + 32

    @staticmethod
    def _celsius_to_kelvin(temp):
        return temp + 273.15

    @staticmethod
    def _celsius_to_rankine(temp):
        return (temp + 273.15) * 9/5

    @staticmethod
    def _celsius_to_reaumur(temp):
        return temp * 4/5

    @staticmethod
    def _fahrenheit_to_celsius(temp):
        return (temp - 32) * 5/9

    @staticmethod
    def _fahrenheit_to_kelvin(temp):
        return (temp + 459.67) * 5/9

    @staticmethod
    def _fahrenheit_to_rankine(temp):
        return temp + 459.67

    @staticmethod
    def _fahrenheit_to_reaumur(temp):
        return (temp - 32) * 4/9

    @staticmethod
    def _kelvin_to_celsius(temp):
        return temp - 273.15

    @staticmethod
    def _kelvin_to_fahrenheit(temp):
        return (temp * 9/5) - 459.67

    @staticmethod
    def _kelvin_to_rankine(temp):
        return temp * 9/5

    @staticmethod
    def _kelvin_to_reaumur(temp):
        return (temp - 273.15) * 4/5

    @staticmethod
    def _rankine_to_celsius(temp):
        return (temp - 491.67) * 5/9

    @staticmethod
    def _rankine_to_fahrenheit(temp):
        return temp - 459.67

    @staticmethod
    def _rankine_to_kelvin(temp):
        return temp * 5/9

    @staticmethod
    def _rankine_to_reaumur(temp):
        return (temp - 491.67) * 4/9

    @staticmethod
    def _reaumur_to_celsius(temp):
        return temp * 5/4

    @staticmethod
    def _reaumur_to_fahrenheit(temp):
        return (temp * 9/4) + 32

    @staticmethod
    def _reaumur_to_kelvin(temp):
        return (temp * 5/4) + 273.15

    @staticmethod
    def _reaumur_to_rankine(temp):
        return (temp * 9/4) + 491.67

def main():
    parser = argparse.ArgumentParser(description="Convert temperature between different units.")
    parser.add_argument("temperature", type=float, help="Temperature value to convert.")
    parser.add_argument("from_unit", type=str, choices=[unit.value for unit in Unit], help="Unit to convert from.")
    parser.add_argument("to_unit", type=str, choices=[unit.value for unit in Unit], help="Unit to convert to.")
    parser.add_argument("--precision", type=int, default=2, help="Precision of the converted value.")

    args = parser.parse_args()

    from_unit = Unit(args.from_unit)
    to_unit = Unit(args.to_unit)

    try:
        result = TemperatureConverter.convert(args.temperature, from_unit, to_unit, args.precision)
        print(f"{args.temperature} {from_unit.value} is {result} {to_unit.value}")
    except (UnsupportedUnitError, SameUnitConversionError) as e:
        print(e)

if __name__ == "__main__":
    main()
