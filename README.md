# WeatherTelegramBot
Telegram bot that shows the weather in the city.

## Setup
1. Clone this repository:
```bash
git clone https://github.com/t3m8ch/WeatherTelegramBot.git
cd WeatherTelegramBot/
```
2. Create and activate virtualenv:
```bash
python3 -m venv env
source env/bin/activate
```
3. Install required dependencies:
```bash
pip install -r requirements.txt
```
4. Everything is now ready to go!
```bash
TELEGRAM_TOKEN=<your-telegram-token> OWN_TOKEN=<your-openweathermap-api-key> python3 main.py
```

## Run
After installation, to restart, you need to run these commands:
```bash
# Go to the folder with the repository
source env/bin/activate
TELEGRAM_TOKEN=<your-telegram-token> OWN_TOKEN=<your-openweathermap-api-key> python3 main.py
```
