import PCF8591 as ADC  # Import PCF8591 module
import time  # for delay in print statement
from gpiozero import Motor
from time import sleep
import board
import adafruit_dht
import requests
import datetime 
import mysql.connector #will need to pip install this on pi virtual env
#WATER LEVEL SHOULD BE IN Ain1 in the converter thingy

def main(args):
    #setup stuff
    ADC.setup(0x48)  # idk tutorial made me do it
    tempSensor = adafruit_dht.DHT11(board.D22)
    #grabbing readings
    currentTime = str(datetime.datetime.now()) 
    waterLevel = str(ADC.read(1)) #sensor id 0
    soilMoisture = str(ADC.read(2)) #sensor id 1
    temperature_f = str(tempSensor.temperature * (9 / 5) + 32) # converts celcius reading to F #sensor id 2
    humidity = str(tempSensor.humidity)     #sensor id 3
    tempSensor.exit()
    #sends data to web server
    database= mysql.connector.connect(
        host="localhost",
        user="whateverTheUsernameIs",
        password="password here",
        database="database here"
    )
    cursor = database.cursor()
    sql = "INSERT INTO Measurement (measurment, time, Sensor_id) VALUES (%s, %s, %s)"
    waterLevelVals = (waterLevel, currentTime, 0)
    soilMoistureVals = (soilMoisture, currentTime, 1) 
    tempVals = (temperature_f, currentTime, 2) 
    humidityVals = (humidity, currentTime, 3) 

    cursor.execute(sql, waterLevelVals) 
    cursor.execute(sql, soilMoistureVals) 
    cursor.execute(sql, tempVals) 
    cursor.execute(sql, humidityVals) 
    database.commit()
    cursor.close()
    database.close()


    
   
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
