class Weather:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather
n=int(input())
weather_arr =[]
for _ in range(n):
    date, day, weather = tuple(input().split())
    weather_arr.append(Weather(date, day, weather))
first_date = None
result_index=-1
for i in range(n):
    if weather_arr[i].weather=="Rain":
        if first_date is None or weather_arr[i].date < first_date:
            first_date = weather_arr[i].date
            result_index = i

print(f"{weather_arr[result_index].date} {weather_arr[result_index].day} {weather_arr[result_index].weather}")

