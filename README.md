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
```


## Roadmap

### AI-Powered Features

*   **Personalized Weather-Based Recommendations:** An AI model could analyze a user's historical weather data and location to provide personalized recommendations. For example, it could suggest activities ("It's going to be sunny, a great day for a hike!"), clothing ("Don't forget your umbrella, rain is expected."), or even health advice ("High pollen count today, take your allergy medication.").

*   **Predictive Weather Anomaly Detection:** An AI model could be trained on historical weather patterns to identify and alert users to unusual or extreme weather events that might not be immediately obvious from a standard forecast. This could include sudden temperature drops, unseasonal storms, or prolonged periods of unusual weather.

*   **Natural Language Querying:** Instead of using command-line arguments, users could interact with the weather app using natural language. For example, a user could ask, "What's the weather like in London for the next three days?" or "Will I need a coat in New York this weekend?". An AI-powered NLP model would parse the query and provide the relevant weather information.

*   **Hyper-Local Weather Forecasting:** By combining data from multiple sources (including user-submitted data from their own weather stations, if available), an AI model could provide hyper-local weather forecasts with a much higher degree of accuracy than a standard city-wide forecast.

*   **Automated Smart Home Integration:** The weather app could integrate with smart home devices to automatically adjust settings based on the weather forecast. For example, it could automatically close the blinds if a heatwave is predicted, or turn on the heating if a cold snap is on the way. This would require the user to grant permissions to control their smart home devices.
