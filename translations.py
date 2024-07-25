# translations.py

# Global variable for language
_language = 'EN'

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


def get_language():
    global _language
    return _language


def set_language(language):
    global _language
    _language = language


def translate(message_key):
    """Translate message based on the global LANGUAGE variable."""
    return translations[get_language()].get(message_key, "")
