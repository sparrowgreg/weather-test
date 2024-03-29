import requests
import datetime
import time

cronjob = True


def get_data():
    app_id = 'e21f33558fd40ca1efd2be1eb27de5d4'
    city_name = 'Athens'
    country_code = 'GR'
    api_call = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city_name + ',' + country_code + '&appid=' + app_id + '&mode=json&units=metric'

    data = requests.post(api_call)
    humidity = []
    date = []
    temp = []
    desc = []
    pressure = []
    sea_level = []

    data = data.json()
    print("\t" + "Details about the forcast of the city " + city_name + " of next 5 days " + "\n\n")
    for lists in data['list']:
        date.append(lists['dt_txt'])
        humidity.append(lists['main']['humidity'])
        temp.append(lists['main']['temp'])
        pressure.append(lists['main']['pressure'])
        sea_level.append(lists['main']['sea_level'])
        desc.append(lists['weather'][0]['description'])

    print('{:^25}{:^20}{:^20}{:^20}{:^20}{:^20}'.format("Date", "Description", "Temprature", "Humidity", "Pressure", "Sea_level\n"))
    for i in range(len(humidity)):
        print('{:^25}{:^20}{:^20}{:^20}{:^20}{:^20}'.format(str(date[i]), desc[i], str(temp[i])+" C\N{DEGREE SIGN}", str(humidity[i])+" %",
            str(pressure[i])+" hPa", str(sea_level[i])+" hPa"))

    with open("test.txt", "a+") as file:
        date = datetime.datetime.now().strftime("%H:%M:%S")
        file.write('Logged data at: ' + str(date) + '\n')

    if cronjob:
        time.sleep(5)
        get_data()


def get_call():
    print("===========calling")

get_data()
get_call()
