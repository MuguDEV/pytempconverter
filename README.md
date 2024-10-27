# pytempconverter
A Python module for converting temperatures between Celsius, Fahrenheit, Kelvin, Rankine, and Reaumur.

## Project Structure

```
pytempconverter
├── src
│   ├── temperature_converter.py
│   └── __init__.py
├── setup.py
└── requirements.txt
```

## Usage

1. Import the `TemperatureConverter` class:

    ```python
    from pytempconverter import TemperatureConverter
    ```

2. Use the `convert` method to convert temperatures:

    ```python
    try:
        result = TemperatureConverter.convert(100, 'Celsius', 'Fahrenheit', precision=2)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    ```

## Custom Errors 🚫

- `UnsupportedUnitError`: Raised when an unsupported temperature unit conversion is requested.
- `SameUnitConversionError`: Raised when attempting to convert between the same temperature units.

## Temperature Units 🌐

- Celsius (`'Celsius'`)
- Fahrenheit (`'Fahrenheit'`)
- Kelvin (`'Kelvin'`)
- Rankine (`'Rankine'`)
- Reaumur (`'Reaumur'`)

## Unit Conversions 🔄

The following conversions are supported:

- Celsius to Fahrenheit, Kelvin, Rankine, Reaumur and vice versa
- Fahrenheit to Kelvin, Rankine, Reaumur and vice versa
- Kelvin to Rankine, Reaumur and vice versa
- Rankine to Reaumur and vice versa

## Contribution 🤝

Feel free to contribute or open issues if you find any bugs or have suggestions for improvements.

Happy temperature converting! 🌡️🔥❄️
