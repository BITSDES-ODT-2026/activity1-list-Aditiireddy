from machine import Pin
import time
led1=Pin(4,Pin.OUT)
led2=Pin(14,Pin.OUT)
led3=Pin(26,Pin.OUT)
led4=Pin(33,Pin.OUT)

list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
while True:
    for i in list:
        led1.value(i[0])
        led2.value(i[1])
        led3.value(i[2])
        led4.value(i[3])
        time.sleep(0.5)#Create any list
