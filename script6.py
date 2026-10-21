import requests


def get_minsk_hourly_weather():
  url = "https://wttr.in/Minsk?format=j1"
  headers = {"User-Agent": "Mozilla/5.0"}

  try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      data = response.json()

      today = data["weather"][0]
      date_str = today.get("date", "Сегодня")

      print(f" Почасовой прогноз погоды в Минске ({date_str}):\n")
      print(f"{'Время':<8} | {'Состояние':<22} | {'Температура':<12} | {'Ощущается':<12} | {'Влажность'}")
      print("-" * 70)

      for hour in today.get("hourly", []):
        raw_time = int(hour.get("time", 0))
        time_formatted = f"{raw_time // 100:02d}:00"

        temp = hour.get("tempC", "N/A")
        feels_like = hour.get("FeelsLikeC", "N/A")
        humidity = hour.get("humidity", "N/A")

        weather_desc = "Нет данных"
        try:
          weather_desc = hour["lang_ru"][0]["value"]
        except (KeyError, IndexError):
          try:
            weather_desc = hour["weatherDesc"][0]["value"]
          except (KeyError, IndexError):
            pass

        print(
            f"{time_formatted:<8} | {weather_desc:<22} | {temp + '°C':<12} |"
            f" {feels_like + '°C':<12} | {humidity}%"
        )

    else:
      print(" Ошибка при получении данных с сервера.")

  except Exception as e:
    print(f" Произошла ошибка: {e}")


if __name__ == "__main__":
  get_minsk_hourly_weather()