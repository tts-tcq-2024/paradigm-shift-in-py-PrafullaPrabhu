# messages.py

from translations import translate
from validation import TEMP_MIN, TEMP_MAX, SOC_MIN, SOC_MAX, CHARGE_RATE_MAX, TEMP_TOLERANCE, SOC_TOLERANCE, CHARGE_RATE_TOLERANCE


def print_error_message(value, min_value, max_value, tolerance, param_name):
    conditions = {
        value < min_value or value > max_value: f'{param_name}_out_of_range',
        min_value <= value < min_value + tolerance: f'{param_name}_warning_low',
        max_value - tolerance < value <= max_value: f'{param_name}_warning_high'
    }
    print_message(conditions)


def print_message(conditions):
    message_key = next((message_key for condition, message_key in conditions.items() if condition), '')
    if message_key:
        print(translate(message_key))


def print_temperature_error_message(temperature):
    print_error_message(temperature, TEMP_MIN, TEMP_MAX, TEMP_TOLERANCE, 'temperature')


def print_soc_error_message(soc):
    print_error_message(soc, SOC_MIN, SOC_MAX, SOC_TOLERANCE, 'soc')


def print_charge_rate_error_message(charge_rate):
    print_error_message(charge_rate, 0, CHARGE_RATE_MAX, CHARGE_RATE_TOLERANCE, 'charge_rate')


def print_errors(temperature, soc, charge_rate):
    """Prints all validation errors and warnings"""
    print_temperature_error_message(temperature)
    print_soc_error_message(soc)
    print_charge_rate_error_message(charge_rate)
