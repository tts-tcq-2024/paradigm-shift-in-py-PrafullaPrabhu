def validate_temperature(temperature):
    """Validates temperature"""
    if temperature < 0 or temperature > 45:
        return False
    return True


def validate_soc(soc):
    """Validates state of charge"""
    if soc < 20 or soc > 80:
        return False
    return True


def validate_charge_rate(charge_rate):
    """Validates charge rate"""
    if charge_rate > 0.8:
        return False
    return True


def print_errors(temperature, soc, charge_rate):
    """Prints all validation errors"""
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
    if charge_rate > 0.8:
        print('Charge rate is out of range!')


def battery_is_ok(temperature, soc, charge_rate):
    """Defines battery state considering all validations"""
    print_errors(temperature, soc, charge_rate)

    return all([
        validate_temperature(temperature),
        validate_soc(soc),
        validate_charge_rate(charge_rate)
    ])


if __name__ == '__main__':
    assert (battery_is_ok(25, 70, 0.7) is True)  # All within acceptable ranges
    assert battery_is_ok(0, 20, 0.9) is False  # Charge rate out of range
    assert battery_is_ok(30, 10, 0.2) is False  # SOC out of range
    assert (battery_is_ok(30, 81, 0.9) is False)  # Charge rate and SOC out of range
    assert battery_is_ok(50, 75, 0.6) is False  # Temperature out of range
    assert (battery_is_ok(46, 21, 0.81) is False)  # Temperature and Charge rate out of range
    assert (battery_is_ok(50, 85, 0) is False)  # Temperature and SOC out of range
    assert battery_is_ok(-5, 90, 1.0) is False  # All parameters out of range
