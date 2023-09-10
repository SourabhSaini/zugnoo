import requests
from wmo_codes import wmo_code
from random import choice

class Weather:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

        self.city = 'BENGALURU'
        self.latitude = 12.9719
        self.longitude = 77.5937
        
        self.filter = None

    def get_filter(self):
        filter_dict = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'daily': 'weathercode,temperature_2m_max,temperature_2m_min',
                'timezone': 'auto',
            }
        print(filter_dict)
        return filter_dict

    def get_weather_url(self):
        filter_dict = self.get_filter()
        path = '&'.join([f"{key}={value}" for key, value in filter_dict.items()])
        weather_url = f'{self.base_url}?{path}'
        # print(weather_url)
        return weather_url

    def fetch_weather_data_from_api(self):
        weather_url = self.get_weather_url()
        response = requests.get(weather_url)
        if response.status_code == 200:
            api_data = response.json()
            return api_data
        else:
            raise "No data from Weather API"

    def extract_data(self, api_data):
         fields = {}
         fields['lat'] = api_data['latitude']
         fields['lon'] = api_data['longitude']
         fields['date_today'] = dict(zip(['year', 'month', 'day'], api_data['daily']['time'][0].split('-')))
         fields['temp_today'] = {
                 'max': str(api_data['daily']['temperature_2m_max'][0]),
                 'min': str(api_data['daily']['temperature_2m_min'][0]),
                 }
         fields['wmo_code'] = api_data['daily']['weathercode'][0]
         return fields

    def format_data(self, fields):
        fields['temp_today']['min'] = fields['temp_today']['min'] + '°C'
        fields['temp_today']['max'] = fields['temp_today']['max'] + '°C'
        fields['weather_status'] = wmo_code[int(fields['wmo_code'])]
        return fields
    
    def get_weather_data(self):
        data = self.fetch_weather_data_from_api()
        data = self.extract_data(data)
        data = self.format_data(data)
        return data

    def get_weather_status(self):
        weather_data = self.get_weather_data()
        status = weather_data['weather_status']
        return status

