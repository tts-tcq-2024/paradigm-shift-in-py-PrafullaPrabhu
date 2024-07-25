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


def validate_temperature(temperature):
    """Validates temperature"""
    return TEMP_MIN <= temperature <= TEMP_MAX


def validate_soc(soc):
    """Validates state of charge"""
    return SOC_MIN <= soc <= SOC_MAX


def validate_charge_rate(charge_rate):
    """Validates charge rate"""
    return charge_rate <= CHARGE_RATE_MAX
