import httpx
import settings


class OpenWeatherAPIService:
    def get_weather(self, city: str):
        return httpx.get(
            url=f"https://api.openweathermap.org/data/2.5/weather",
            params={
                'q': city,
                'appid': settings.API_TOKEN,
                'units': 'metric'
            }
        )
