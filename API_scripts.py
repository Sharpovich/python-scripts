# API
# API -- это набор функций, констант и методов
# WEB_API

import requests 

# обращение к сайту с погодой
def weather_calc():
    city = input("What city? ")
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': "11c0d3dc6093f7442898ee49d2430d20",
        'units': "metric"
    }

    res=requests.get(api_url, params=params)
    # print(res.status_code)
    # print(res.headers["Content-Type"])
    # print(res.json())
    data=res.json()
    template="Current temperature in {} is {}"
    print(template.format(city, data["main"]["temp"]))

if __name__=="__main__":
    while True:
        try:
            weather_calc()
        except:
            continue
