import argparse
import requests
from datetime import datetime
from prettytable import PrettyTable
from dotenv import load_dotenv
import os
from collections import Counter

# Load environment variables from .env file
load_dotenv()

# Function to get weather data from OpenWeatherMap API
def get_weather_data(api_key, city, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={days * 8}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to parse weather data and create a summary table
def create_weather_summary(weather_data):
    table = PrettyTable()
    table.field_names = ["Date/Time", "Weather", "Temp (°C)"]

    max_temps = []
    min_temps = []
    weather_conditions = []

    for entry in weather_data['list']:
        dt = datetime.fromtimestamp(entry['dt'])
        weather = entry['weather'][0]['description']
        temp_max = round(entry['main']['temp_max'])
        temp_min = round(entry['main']['temp_min'])
        max_temps.append(temp_max)
        min_temps.append(temp_min)
        weather_conditions.append(weather)
        table.add_row([dt.strftime('%d/%m %H:%M'), weather, f"{temp_max} | {temp_min}"])

    avg_max_temp = sum(max_temps) / len(max_temps)
    avg_min_temp = sum(min_temps) / len(min_temps)
    most_common_weather = Counter(weather_conditions).most_common(1)[0][0]

    city_name = weather_data['city']['name']
    country = weather_data['city']['country']

    report = f"*Weather report for {city_name}, {country}*\n"
    report += f"*Average Max Temperature:* {round(avg_max_temp)}°C\n"
    report += f"*Average Min Temperature:* {round(avg_min_temp)}°C\n"
    report += f"*Most Common Weather:* {most_common_weather}\n"
    report += f"```\n{table}\n```\n"  # Wrap the table in backticks

    print(report)

    # Send report to Telegram if token is set
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_ids = os.getenv('CHAT_ID')
    if telegram_token and chat_ids:
        for chat_id in chat_ids.split(','):
            send_telegram_message(telegram_token, chat_id.strip(), report)

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, json=payload)

def main():
    parser = argparse.ArgumentParser(description='Check the weather forecast.')
    parser.add_argument('--days', type=int, required=True, help='Number of days to check the weather forecast for')
    parser.add_argument('--city', type=str, default='London', help='City to check the weather for')
    args = parser.parse_args()

    # Get the API key from environment variable
    api_key = os.getenv('API_KEY')
    if not api_key:
        print("Error: API_KEY not found in environment variables.")
        return

    weather_data = get_weather_data(api_key, args.city, args.days)
    create_weather_summary(weather_data)

if __name__ == "__main__":
    main()
