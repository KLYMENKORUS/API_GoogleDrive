import requests
from config import API_WEATHER_APP
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

google_auth = GoogleAuth()
google_auth.LocalWebserverAuth()

# Выгружаем данные из API
city_enter = input('Enter the city: ')
url = requests.get(
    f' https://api.openweathermap.org/data/2.5/weather?q={city_enter}&appid={API_WEATHER_APP}&units=metric')
data = url.json()
city = data['name']
temp = data['main']['temp']
weather = data['weather'][0]['description']
city_weather = f'City: {city}\nTemperature: {temp}\nWeather: {weather}'


# Загружаем файл на диск
def create_and_upload_file(file_name='test.txt', file_content='Hello'):
    try:
        drive = GoogleDrive(google_auth)
        file = drive.CreateFile({'title': f'{file_name}'})
        file.SetContentString(file_content)
        file.Upload()

        return f'File {file_name} was uploaded!'
    except Exception as _ex:
        return 'Got some trouble!'


def main():
    print(create_and_upload_file('Test.txt', city_weather))


if __name__ == '__main__':
    main()
