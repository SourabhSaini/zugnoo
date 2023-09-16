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
                'current_weather': 'true',
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
            print(api_data)
            return api_data
        else:
            raise "No data from Weather API"

    def extract_data(self, api_data):
         fields = {}
         fields['lat'] = api_data['latitude']
         fields['lon'] = api_data['longitude']
         fields['temperature_today'] = {
                 'max': api_data['daily']['temperature_2m_max'][0],
                 'min': api_data['daily']['temperature_2m_min'][0],
                 }
         fields['temperature_tomorrow'] = {
                 'max': str(api_data['daily']['temperature_2m_max'][1]),
                 'min': str(api_data['daily']['temperature_2m_min'][1]),
                 }
         fields['wmo_code_tomorrow'] = api_data['daily']['weathercode'][1]
         fields['wmo_code'] = api_data['current_weather']['weathercode']
         fields['temperature'] = api_data['current_weather']['temperature']
         fields['windspeed'] = api_data['current_weather']['windspeed']
         fields['winddir'] = api_data['current_weather']['winddirection']
         return fields

    def format_data(self, fields):
        fields['weather_status'] = wmo_code[int(fields['wmo_code'])]
        fields['weather_status_tomorrow'] = wmo_code[int(fields['wmo_code_tomorrow'])]
        fields['temperature_now'] = fields['temperature']
        fields['temperature_today'] = {
                                        'min': fields['temperature_today']['min'],
                                        'now': fields['temperature_now'],
                                        'max': fields['temperature_today']['max'],
                                    }
        fields['temperature_min'] = str(fields['temperature_today']['min']) # + '°C'
        fields['temperature_max'] = str(fields['temperature_today']['max']) # + '°C'
        fields['temperature_tomorrow_min'] = str(fields['temperature_tomorrow']['min']) # + '°C'
        fields['temperature_tomorrow_max'] = str(fields['temperature_tomorrow']['max']) # + '°C'
        fields['windspeed'] = float(fields['windspeed'])
        fields['winddir'] = int(fields['winddir'])
        return fields
    
    def get_weather_data(self):
        data = self.fetch_weather_data_from_api()
        data = self.extract_data(data)
        data = self.format_data(data)
        return data

