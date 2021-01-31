import asyncio
import aiohttp
from config_logger import configure_logger
configure_logger('DEBUG')
from weather import OpenWeatherMap


async def main():
    async with aiohttp.ClientSession() as session:
        owm = OpenWeatherMap('1705b49007f1c0faee3b79178930aff4', session)
        for _ in range(10):
            await asyncio.sleep(1)
            await owm.get_weather('Saratov')


if __name__ == '__main__':
    asyncio.run(main())

