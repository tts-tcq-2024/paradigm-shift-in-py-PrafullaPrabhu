Battery Management System
This repository contains a Python implementation for validating various parameters of a battery management system. The system checks if temperature, state of charge (SOC), and charge rate values fall within acceptable ranges and provides warnings if they are approaching critical thresholds.

Constants for Validation
Temperature
TEMP_MIN: Minimum acceptable temperature (0°C).
TEMP_MAX: Maximum acceptable temperature (45°C).
TEMP_TOLERANCE: 5% of the maximum temperature value used to determine warning thresholds.
State of Charge (SOC)
SOC_MIN: Minimum acceptable state of charge (20%).
SOC_MAX: Maximum acceptable state of charge (80%).
SOC_TOLERANCE: 5% of the maximum SOC value used to determine warning thresholds.
Charge Rate
CHARGE_RATE_MAX: Maximum acceptable charge rate (0.8C).
CHARGE_RATE_TOLERANCE: 5% of the maximum charge rate used to determine warning thresholds.

In this script:

The set_language function sets the language for the messages.
The get_language function verifies the current language setting.
The battery_is_ok function checks if the battery parameters are within acceptable ranges and prints corresponding messages.
