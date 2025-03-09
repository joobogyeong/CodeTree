class Secret:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

secert_code, secret_place, secret_time = input().split()
secret_time=int(secret_time)

Secret_spy = Secret(secert_code, secret_place, secret_time)
print(f"secret code : {Secret_spy.code}")
print(f"meeting point : {Secret_spy.place}")
print(f"time : {Secret_spy.time}")