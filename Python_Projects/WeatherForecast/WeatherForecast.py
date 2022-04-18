import requests
from pprint import pprint







def main():
    API_Key = '3e225fe543c6aea0fa76bfe971666109'


    city = input("Enter a city: ")
   # lat = 38
   # lon = 24
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid"+API_Key

  #  base_url = "http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid="+API_Key

    weather_data = requests.get(base_url).json()

    pprint(weather_data)


#Main Call to main()
if __name__ == '__main__':
    main()
