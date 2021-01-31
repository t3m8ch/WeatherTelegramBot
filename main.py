from config import TELEGRAM_TOKEN, OWM_TOKEN, LOGGING_LEVEL

from loguru import logger
from config_logger import configure_logger
configure_logger(LOGGING_LEVEL)

import asyncio
from aiogram import Bot, Dispatcher, executor, types

from exceptions import CityNotFoundError
from weather import OpenWeatherMap


bot = Bot(token=TELEGRAM_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
owm = OpenWeatherMap(OWM_TOKEN, bot.session)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    text = '<b>Привет!</b> Я Телеграм-бот, который покажет ' \
           'погоду в любом городе.\n\n' \
           'Просто отправь мне <b>название города</b> и я покажу <b>полную</b> ' \
           'информацию о погоде в нём.\n\n' \
           'Для получения информации о погоде используется сервис openweathermap.org.'
    await message.reply(text)


@dp.message_handler()
async def send_weather(message: types.Message):
    logger.debug(f'City: "{message.text}"')
    try:
        weather = await owm.get_weather(message.text)
        text = f'Погода в городе <b>{weather.city_name}</b>:\n' \
               f'Температура на улице: <b>{weather.temp}</b> °C\n' \
               f'Ощущается как <b>{weather.feels_like}</b> °C\n' \
               f'Давление <b>{round(weather.get_pressure_mm_of_mercury(), 2)}</b> мм. рт. ст.\n' \
               f'Влажность <b>{weather.humidity}</b>%\n\n' \
               f'<b>Ветер:</b>\n' \
               f'Скорость: <b>{weather.wind.speed}</b> м/с\n' \
               f'Направление: <b>{weather.wind.deg}</b>°\n'
        await message.answer(text)
    except CityNotFoundError as e:
        await message.answer('Такого города нет.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

