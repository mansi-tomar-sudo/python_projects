import requests
city=input("enter city")
YOUR_API_KEY="6c068dd4494850ca1394bbebdaff4d19"
api=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={YOUR_API_KEY}&units=metric"
response=requests.get(api)
data=response.json()
print(data)


