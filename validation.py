# validation.py

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


def check_out_of_range(value, min_value, max_value):
    return value < min_value or value > max_value


def check_warning_low(value, min_value, tolerance):
    return min_value <= value < min_value + tolerance


def check_warning_high(value, max_value, tolerance):
    return max_value - tolerance < value <= max_value


def validate_parameter(value, min_value, max_value, tolerance):
    checks = {
        'out_of_range': check_out_of_range(value, min_value, max_value),
        'warning_low': check_warning_low(value, min_value, tolerance),
        'warning_high': check_warning_high(value, max_value, tolerance)
    }
    return next((status for status, result in checks.items() if result), 'ok')


def validate_temperature(temperature):
    return validate_parameter(temperature, TEMP_MIN, TEMP_MAX, TEMP_TOLERANCE)


def validate_soc(soc):
    return validate_parameter(soc, SOC_MIN, SOC_MAX, SOC_TOLERANCE)


def check_charge_rate_out_of_range(charge_rate):
    return charge_rate > CHARGE_RATE_MAX


def check_charge_rate_warning_high(charge_rate):
    return CHARGE_RATE_MAX - CHARGE_RATE_TOLERANCE < charge_rate <= CHARGE_RATE_MAX


def validate_charge_rate(charge_rate):
    result = (
        'out_of_range' if check_charge_rate_out_of_range(charge_rate) else
        'warning_high' if check_charge_rate_warning_high(charge_rate) else
        'ok'
    )
    return result
