import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import Keys
from twilio.rest import Client
#Provide your IBM Watson Device Credentials
organization = "t5udfe"
deviceType = "raspberrypi"
deviceId = "12345"
authMethod = "token"
authToken = "12345678"
# Initialize GPIO
def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=="smart bin opened":
        print ("The Smart Bin is Open now")
    else :
        print ("The Smart Bin is Close now")
       #print(cmd)
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        distance=random.randint(0,200)
        weight=random.randint(0,10)
        data = { 'distance' : distance, 'weight': weight }
        #print data
        def myOnPublishCallback():
            print ("Published Data to IOT Watson: \n       Distance= %s cm\n" % distance, "      Weight = %s Kg\n" % weight)
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(10)
        deviceCli.commandCallback = myCommandCallback
# Disconnect the device and application from the cloud
deviceCli.disconnect()
