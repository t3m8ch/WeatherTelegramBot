from typing import NamedTuple, Optional, Type
from types import TracebackType

from loguru import logger

import aiohttp

from exceptions import CityNotFoundError, OWMApiKeyIsNotCorrectError


class Wind(NamedTuple):
    speed: float
    deg: int


class Weather(NamedTuple):
    city_name: str
    temp: float
    feels_like: float
    pressure_hpa: float
    humidity: int
    wind: Wind

    def get_pressure_mm_of_mercury(self):
        return self.pressure_hpa * 0.750062  # according to Google


def _parse_owm_json(json) -> Weather:
    code = int(json['cod'])
    logger.debug(f'Status code = {code}')

    if code == 404:
        logger.debug(f'City not found!')
        raise CityNotFoundError()
    if code == 401:
        logger.error(f'OpenWeatherMap api key is not correct!')
        raise OWMApiKeyIsNotCorrectError()

    logger.debug('OK')
    wind_json = json['wind']
    wind = Wind(speed=float(wind_json['speed']),
                deg=int(wind_json['deg']))

    weather_json = json['main']
    weather = Weather(city_name=json['name'],
                      temp=float(weather_json['temp']),
                      feels_like=float(weather_json['feels_like']),
                      pressure_hpa=float(weather_json['pressure']),
                      humidity=int(weather_json['humidity']),
                      wind=wind)

    return weather


class OpenWeatherMap:
    def __init__(self,
                 api_key: str,
                 aiohttp_session: aiohttp.ClientSession,
                 lang='ru',
                 units='metric'):
        assert units.lower() in ('standart', 'metric', 'imperial'), \
            'There is no such metric system or it was not introduced in English.\n' \
            'Valid values are "standart", "metric", and "imperial".'

        self._api_key = api_key
        self._lang = lang.lower()
        self._units = units.lower()

        self.__aiohttp_session = aiohttp_session

    async def get_weather(self, city: str) -> Weather:
        url = f'https://api.openweathermap.org/data/2.5/weather?' \
              f'q={city}&' \
              f'appid={self._api_key}&' \
              f'lang={self._lang}&' \
              f'units={self._units}'

        async with self.__aiohttp_session.get(url) as response:
            json = await response.json()
            parsed = _parse_owm_json(json)
            return parsed

