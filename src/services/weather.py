import json

from fastapi import HTTPException

from services.open_weather import OpenWeatherAPIService


class WeatherService:
    def get_city_weather(self, city: str, parameters: str) -> dict:
        weather_response = OpenWeatherAPIService().get_weather(city)

        if weather_response.status_code != 200:
            raise HTTPException(
                status_code=weather_response.status_code,
                detail=weather_response.json()['message']
            )

        result = dict()
        result['city_name'] = city
        result['parameters'] = self.convert_to_dict(weather_response.json(), parameters)

        return result

    @classmethod
    def convert_to_dict(cls, response: json, parameters: str) -> dict:
        result = dict()

        param_list = parameters.lower().split(' ')

        if 'temperature' in param_list:
            result['temperature'] = response['main']['temp']

        if 'feels' in param_list:
            result['feels'] = response['main']['feels_like']

        if 'wind' in param_list:
            result['wind'] = response['wind']

        if 'visibility' in param_list:
            result['visibility'] = response['visibility']

        if 'humidity' in param_list:
            result['humidity'] = response['main']['humidity']

        return result

    def get_city_list_weather(self, cities: list[str], parameters: str) -> dict:
        result = list()

        for city in cities:
            city_weather = self.get_city_weather(city, parameters)

            result.append(city_weather)

        return {'weather_list': result}
