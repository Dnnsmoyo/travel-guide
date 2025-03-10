from flask import Flask, render_template
import requests

API_KEY = "cc24cc7c42f06680e1bec75abb70ca0c"
import os
#from twilio.rest import Client

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

                
@app.route("london")
def london():
requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=cc24cc7c42f06680e1bec75abb70ca0c"
message = client.messages.create(
    body= "The temperature in London is: " + data.main.temp + "Degrees",
    from_="+15017122661",
    to="+15558675310",
)
print(message.body)

@app.route("paris")
def paris():
requests.get("https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=cc24cc7c42f06680e1bec75abb70ca0c"
message = client.messages.create(
    body= "The temperature in Paris is: " + data.main.temp + "Degrees",
    from_="+15017122661",
    to="+15558675310",
)
print(message.body)

@app.route("rome")
def rome():
requests.get("https://api.openweathermap.org/data/2.5/weather?q=Rome&appid=cc24cc7c42f06680e1bec75abb70ca0c"
message = client.messages.create(
    body= "The temperature in Rome is: " + data.main.temp + "Degrees",
    from_="+15017122661",
    to="+15558675310",
)
print(message.body)

@app.route("berlin")
def berlin():
requests.get("https://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=cc24cc7c42f06680e1bec75abb70ca0c"
message = client.messages.create(
    body= "The temperature in Berlin is: " + data.main.temp + "Degrees",
    from_="+15017122661",
    to="+15558675310",
)
print(message.body)

@app.route("geneva")
def geneva():
requests.get("https://api.openweathermap.org/data/2.5/weather?q=Geneva&appid=cc24cc7c42f06680e1bec75abb70ca0c"
message = client.messages.create(
    body= "The temperature in Geneva is: " + data.main.temp + "Degrees",
    from_="+15017122661",
    to="+15558675310",
)
print(message.body)

@app.route("newyork")
def new():
requests.get("https://api.openweathermap.org/data/2.5/weather?q=NewYork&appid=cc24cc7c42f06680e1bec75abb70ca0c"
message = client.messages.create(
    body= "The temperature in New York is: " + data.main.temp + "Degrees",
    from_="+15017122661",
    to="+15558675310",
)
print(message.body)

@app.route("Cape Town")
def cape():
requests.get("https://api.openweathermap.org/data/2.5/weather?q=CapeTown&appid=cc24cc7c42f06680e1bec75abb70ca0c"
message = client.messages.create(
    body= "The temperature in Cape Town is: " + data.main.temp + "Degrees",
    from_="+15017122661",
    to="+15558675310",
)
print(message.body)


if __name__ == "__main__":
	app.run()
