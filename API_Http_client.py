from typing import Optional
from pydantic import BaseModel
import requests


class WeatherData(BaseModel):
  city: str
  temp: float
  feels_like: float
  humidity: int
  description: str


class WeatherAPIClient:

  def __init__(self, api_key: str) -> None:
    self.api_key = api_key
    self.base_url = "https://api.openweathermap.org/data/2.5/weather"

  def get_weather(self, city: str) -> Optional[WeatherData]:
    params = {
        "q": city,
        "appid": self.api_key,
        "units": "metric",
        "lang": "ru",
    }

    try:
      response = requests.get(self.base_url, params=params)

      if response.status_code == 200:
        data = response.json()
        return WeatherData(
            city=city,
            temp=data["main"]["temp"],
            feels_like=data["main"]["feels_like"],
            humidity=data["main"]["humidity"],
            description=data["weather"][0]["description"],
        )
      elif response.status_code == 401:
        print(
            "Ошибка 401: Неверный API-ключ. Проверьте правильность введенного"
            " ключа."
        )
        return None
      else:
        print(f"Ошибка сервера: {response.status_code}")
        return None

    except requests.RequestException as e:
      print(f"Ошибка сети: {e}")
      return None


if __name__ == "__main__":
  client = WeatherAPIClient(api_key="4fa0e0ee7dec2f933da308666539a932")
  weather: Optional[WeatherData] = client.get_weather("Minsk")

  if weather:
    print(f"Погода в городе {weather.city}:")
    print(f"  Состояние:   {weather.description.capitalize()}")
    print(f"  Температура: {weather.temp} °C")
    print(f"  Ощущается:   {weather.feels_like} °C")
    print(f"  Влажность:   {weather.humidity}%")
