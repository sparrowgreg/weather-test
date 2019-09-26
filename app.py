import os
from pprint import pprint
import requests
from flask import request #Import flask requests
from flask import render_template #Import flask render templates
import json, urllib #import api modules
import time #Imporing time in darlek voice
import urllib.request

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Athens,gr&APPID=e21f33558fd40ca1efd2be1eb27de5d4"
    response = urllib.request.urlopen(url) #Download Json
    data = json.loads(response.read()) #Parse json
    return("Current Weather in " +data['name']+" "+"status: "+ data['weather'][0]['description'] +", "+ " Temperature: " + str(data['main']['temp'])) #Debug infomation


if __name__ == "__main__":
        #port = int(os.environ.get("PORT", 5000))
        #app.run(host='0.0.0.0', port=port)
        app = Flask(__name__)
        app.run(environ.get('PORT'))
        
