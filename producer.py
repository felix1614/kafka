import random
import time
from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime
from dataGenerator import generateMessage

myProducer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

while True:
    msgData = generateMessage()
    myProducer.send("messages", value=msgData)
    print("msg sent")
    sleep(5)

#
# def serializer(msg):
#     return dumps(msg).encode('utf-8')
#
#
# producer = KafkaProducer(
#     bootstrap_servers=['localhost:9092'],
#     value_serializer=serializer
# )
#

# if __name__ == "__main__":
#     while True:
#         dummy = generateMessage()
#         print(f"producing msg @ {datetime.now()} | message = {str(dummy)}")
#         producer.send('messages', dummy)
#
#         sleepTime = random.randint(1, 11)
#         time.sleep(sleepTime)