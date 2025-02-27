import PCF8591 as ADC  # Import PCF8591 module
import time  # for delay in print statement
from gpiozero import Motor
from time import sleep
import board
import adafruit_dht
import requests
import datetime
#WATER LEVEL SHOULD BE IN Ain1 in the converter thingy

def main(args):
    #setup stuff
    ADC.setup(0x48)  # idk tutorial made me do it
    tempSensor = adafruit_dht.DHT11(board.D22)
    #grabbing readings
    currentTime = str(datetime.datetime.now())
    waterLevel = str(ADC.read(1))
    soilMoisture = str(ADC.read(2))
    temperature_f = str(tempSensor.temperature * (9 / 5) + 32) # converts celcius reading to F
    humidity = str(tempSensor.humidity)    
    tempSensor.exit()
    #sends data to web server
    url = 'http://localhost:3000/data'
    sensorData = {'time': currentTime, 'waterLevel' : waterLevel, 'soilMoisture' : soilMoisture, 'temperature': temperature_f, 'humidity': humidity}
    requests.post(url, sensorData) #add error handling here (if server is down)
    #for logging purposes
    print("Sent data to server at: " + currentTime)
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
