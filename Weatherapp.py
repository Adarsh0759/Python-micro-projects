import requests
import json
import pyttsx3

engine = pyttsx3.init()

city =input("Enter the name of the city\n")
url=f"http://api.weatherapi.com/v1/current.json?key=e5dd2aa5b6c74b42b0192941252203&q={city}"

r=requests.get(url)

wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]

engine.say(f"current weather in {city}is {w} degrees")
engine.runAndWait()