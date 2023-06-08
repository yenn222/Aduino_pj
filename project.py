from datetime import datetime
import random
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED = [17, 27, 23]
BUTTON = 24
BUZZER = 12

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUZZER, GPIO.OUT)

MQTT_HOST = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_PUB_TOPIC = "mobile/yenniii/menu"

client = mqtt.Client()
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.loop_start() 
            

menu = input("고민하는 메뉴들을 적어주세요.(띄어쓰기로 구분)").split()

print(f"{len(menu)}개 중 오늘의 메뉴는?(버튼을 누르면 시작됩니다)")

while GPIO.input(BUTTON) == GPIO.LOW:
    time.sleep(0.1)

for pin in LED:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

GPIO.setup(BUZZER, GPIO.OUT)
buzzer = GPIO.PWM(BUZZER, 440)

try:
    
    for pin in LED:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)
            
   
    buzzer.start(50) 
    time.sleep(0.5)
    buzzer.stop()
        
    for pin in LED:
        GPIO.output(pin, GPIO.LOW)

        time.sleep(1)
        
    result = random.choice(menu)
    
    time.sleep(1)
    menu = {
    '♡오늘의 메뉴♡' : result 
    }
    value = json.dumps(menu, ensure_ascii=False) 
    client.publish(MQTT_PUB_TOPIC, value)
    print(value)
        
except KeyboardInterrupt:
    GPIO.cleanup()     


