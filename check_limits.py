# Global variable for language
LANGUAGE = 'EN'

# Translation dictionary
translations = {
    'EN': {
        'temperature_out_of_range': 'Temperature is out of range! Must be between 0 and 45.',
        'temperature_warning_low': 'Warning: Approaching low temperature.',
        'temperature_warning_high': 'Warning: Approaching high temperature.',
        'soc_out_of_range': 'State of Charge is out of range! Must be between 20 and 80.',
        'soc_warning_low': 'Warning: Approaching discharge.',
        'soc_warning_high': 'Warning: Approaching charge-peak.',
        'charge_rate_out_of_range': 'Charge rate is out of range! Must be 0.8 or less.',
        'charge_rate_warning_high': 'Warning: Approaching high charge rate.'
    },
    'DE': {
        'temperature_out_of_range': 'Die Temperatur liegt außerhalb des Bereichs! Muss zwischen 0 und 45 sein.',
        'temperature_warning_low': 'Warnung: Annäherung an niedrige Temperatur.',
        'temperature_warning_high': 'Warnung: Annäherung an hohe Temperatur.',
        'soc_out_of_range': 'Der Ladezustand liegt außerhalb des Bereichs! Muss zwischen 20 und 80 sein.',
        'soc_warning_low': 'Warnung: Annäherung an Entladung.',
        'soc_warning_high': 'Warnung: Annäherung an Ladehöhepunkt.',
        'charge_rate_out_of_range': 'Die Laderate liegt außerhalb des Bereichs! Muss 0,8 oder weniger sein.',
        'charge_rate_warning_high': 'Warnung: Annäherung an hohe Laderate.'
    }
}

# Constants for validation
TEMP_MIN = 0
TEMP_MAX = 45
SOC_MIN = 20
SOC_MAX = 80
CHARGE_RATE_MAX = 0.8

# Tolerance for warnings (5% of the upper limit)
TEMP_TOLERANCE = 0.05 * TEMP_MAX
SOC_TOLERANCE = 0.05 * SOC_MAX
CHARGE_RATE_TOLERANCE = 0.05 * CHARGE_RATE_MAX


def translate(message_key):
    """Translate message based on the global LANGUAGE variable."""
    return translations[LANGUAGE].get(message_key, message_key)


def validate_temperature(temperature):
    """Validates temperature"""
    return TEMP_MIN <= temperature <= TEMP_MAX


def validate_soc(soc):
    """Validates state of charge"""
    return SOC_MIN <= soc <= SOC_MAX


def validate_charge_rate(charge_rate):
    """Validates charge rate"""
    return charge_rate <= CHARGE_RATE_MAX


def print_error_message(value, min_value, max_value, tolerance, param_name):
    conditions = {
        value < min_value or value > max_value: f'{param_name}_out_of_range',
        min_value <= value < min_value + tolerance: f'{param_name}_warning_low',
        max_value - tolerance < value <= max_value: f'{param_name}_warning_high'
    }
    print_message(conditions)


def print_message(conditions):
    message_key = next((message_key for condition, message_key in conditions.items() if condition), None)
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


def battery_is_ok(temperature, soc, charge_rate):
    """Defines battery state considering all validations"""
    print_errors(temperature, soc, charge_rate)
    return all([
        validate_temperature(temperature),
        validate_soc(soc),
        validate_charge_rate(charge_rate)
    ])


if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True  # All within acceptable ranges
    assert battery_is_ok(0, 20, 0.9) is False  # Charge rate out of range
    assert battery_is_ok(30, 10, 0.2) is False  # SOC out of range
    assert battery_is_ok(30, 81, 0.9) is False  # Charge rate and SOC out of range
    assert battery_is_ok(50, 75, 0.6) is False  # Temperature out of range
    assert battery_is_ok(46, 21, 0.81) is False  # Temperature and Charge rate out of range
    assert battery_is_ok(50, 85, 0) is False  # Temperature and SOC out of range
    assert battery_is_ok(-5, 90, 1.0) is False  # All parameters out of range
