## Code to read sensor data from cupcarbon and send to IoT broker

This script reads the output from sensors in cupcarbon and makes it available to be sent to IoT broker.

Place the script on the results folder of the current project. This folder may only have the sensor data as ".txt". Run the script with python 

```
sensor-to-server.py
`````` 

The script only makes the data available to the application, the code needed to send to the broker is to be developed by the students.

Instead of having a python based IoT device in the simulation, the studends should replace that node with a base station with the instruction to write the received data (data is to be sent to the IoT broker) in a file. The instruction is as follows:

```
printfile data
```