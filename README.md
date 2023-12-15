# pytempconverter 🌡️

A Python module for converting temperatures between Celsius, Fahrenheit, and Kelvin.

## Usage

1. Import the `TemperatureConverter` class from `temperature_converter.py`:

    ```python
    from pytempconverter import TemperatureConverter, TemperatureUnit
    ```

2. Use the `convert_between_units` method to convert temperatures:

    ```python
    try:
        result = TemperatureConverter.convert_between_units(100, TemperatureUnit.CELSIUS, TemperatureUnit.FAHRENHEIT, precision=2)
        print(f"Result: {result}")
    except TemperatureConversionError as e:
        print(f"Error: {e}")
    ```

## Custom Errors 🚫

- `UnsupportedUnitError`: Raised when an unsupported temperature unit conversion is requested.
- `TemperatureOutOfRangeError`: Raised when the temperature value is outside the valid range.
- `TemperatureConversionError`: Raised for general errors in temperature conversion.
- `InvalidPrecisionError`: Raised when the precision value is invalid.
- `SameUnitConversionError`: Raised when attempting to convert between the same temperature units.

## Temperature Units 🌐

- Celsius (`TemperatureUnit.CELSIUS`)
- Fahrenheit (`TemperatureUnit.FAHRENHEIT`)
- Kelvin (`TemperatureUnit.KELVIN`)

## Unit Conversions 🔄

The following conversions are supported:

- Celsius to Fahrenheit and vice versa
- Celsius to Kelvin and vice versa
- Fahrenheit to Kelvin and vice versa


## Contribution 🤝

Feel free to contribute or open issues if you find any bugs or have suggestions for improvements.

Happy temperature converting! 🌡️🔥❄️
