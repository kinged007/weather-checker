# Weather Checker

## Description
The Weather Checker app retrieves weather forecasts from the OpenWeatherMap API. Users can check the weather for a specified city and number of days.

## Requirements
- Python 3.x
- Required Python packages:
  - requests
  - prettytable
  - python-dotenv

You can install the required packages using:
```
pip install -r requirements.txt
```

## Configuration
1. Create a `.env` file in the root directory of the project.
2. Add your OpenWeatherMap API key to the `.env` file:
   ```
   API_KEY=your_api_key_here
   ```
3. Add your Telegram bot token and chat ID(s) to the `.env` file:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   CHAT_ID=your_chat_id_here,another_chat_id_here
   ```
   Note: You can specify multiple chat IDs separated by commas to receive the weather forecast.

## Usage
To run the app, use the following command:
```
python main.py --city <CityName> --days <NumberOfDays>
```
For example, to check the weather in London for the next 3 days:
```
python main.py --city London --days 3
