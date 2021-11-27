import json

import time

import sys

import signal


from ApiHandler import ApiHandler
from DataProcessing import ProcessData

def processData():
    for id in ids:
        # print(id.get('id'))
        weather = ApiHandler(id.get('id'), token)
        # result = weather.getWeatherData()
        dataProccessing = ProcessData(weather.getWeatherData())
        dataProccessing.process_data()

def cb_sigint_handler(signum, stack):
    global is_interrupted
    print ("SIGINT received")
    is_interrupted = True

if __name__ == "__main__":
    #apiConfig = json.load(open("config/api_config.json","r"))
    #/home/tuongnlc/Desktop/data_engineer_project/final/kythuatxulydulieu/weather/config/VN_list.json
    with open("/home/tuongnlc/Desktop/data_engineer_project/final/kythuatxulydulieu/weather/config/VN_list.json", encoding='utf-8-sig') as f:
        apiConfig = json.load(f)

    ids = apiConfig.get('ids')
    token = apiConfig.get('APPID')
    processData()

