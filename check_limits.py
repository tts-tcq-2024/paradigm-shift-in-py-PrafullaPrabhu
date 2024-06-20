def validate_temperature(temperature):
    """Validates temperature"""
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False
    return True


def validate_soc(soc):
    """Validates state of charge"""
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False
    return True


def validate_charge_rate(charge_rate):
    """Validates charge rate"""
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    return True


def battery_is_ok(temperature, soc, charge_rate):
    """Defines battery state considering all validations"""
    return all([validate_temperature(temperature), validate_soc(soc), validate_charge_rate(charge_rate)])


if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)

