import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            print("❌ City not found. Try again.")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"].title()

        print("\n🌤 Weather Report")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {desc}")

    except Exception as e:
        print("Error:", e)


def main():
    print("=== Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)


if __name__ == "__main__":
    main()
