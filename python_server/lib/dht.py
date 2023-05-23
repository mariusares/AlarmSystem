#!/usr/bin/python3
import Adafruit_DHT
sensor = Adafruit_DHT.AM2302
#pin = 4

def getTemperature(pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temp =  round(float(temperature), 2)
    humi =  round(float(humidity), 3)
    return (temp, humi)
