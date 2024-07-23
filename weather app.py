import requests

api_key = "e68f4520e7ca48afb0f24545232603"
city = input("Enter your city: ")

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}" 
weather = requests.get(url).json()

temp = weather["current"]["temp_c"]

print("\nThe Temperature is",temp, "\n")
