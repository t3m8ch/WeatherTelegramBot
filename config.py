import os


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
assert TELEGRAM_TOKEN is not None, \
    'For the bot to work, you need to enter ' \
    'TELEGRAM_TOKEN environment variable!'

OWM_TOKEN = os.getenv('OWM_TOKEN')
assert OWM_TOKEN is not None, \
    'For the bot to work, you need to enter ' \
    'OWM_TOKEN (OpenWeatherMap api key) environment variable!'

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'WARNING').upper()

