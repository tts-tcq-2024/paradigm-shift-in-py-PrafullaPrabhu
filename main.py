# main.py

from validation import validate_temperature, validate_soc, validate_charge_rate
from messages import print_message
from messages import set_language, get_language


def print_errors(validation_results):
    for parameter, result in validation_results.items():
        print_message(parameter, result)


def battery_is_ok(temperature, soc, charge_rate):
    validation_results = {
        'temperature': validate_temperature(temperature),
        'soc': validate_soc(soc),
        'charge_rate': validate_charge_rate(charge_rate)
    }
    print_errors(validation_results)
    return all(result == 'ok' for result in validation_results.values())


if __name__ == '__main__':
    set_language('EN')
    assert get_language() == 'EN'  # Check the language is set to English
    assert battery_is_ok(25, 70, 0.7) is True  # All within acceptable ranges
    assert battery_is_ok(0, 20, 0.9) is False  # Charge rate out of range
    assert battery_is_ok(30, 10, 0.2) is False  # SOC out of range
    assert battery_is_ok(30, 81, 0.9) is False  # Charge rate and SOC out of range

    set_language('DE')
    assert get_language() == 'DE'  # Check the language is set to German
    assert battery_is_ok(50, 75, 0.6) is False  # Temperature out of range
    assert battery_is_ok(46, 21, 0.81) is False  # Temperature and Charge rate out of range
    assert battery_is_ok(50, 85, 0) is False  # Temperature and SOC out of range
    assert battery_is_ok(-5, 90, 1.0) is False  # All parameters out of range

