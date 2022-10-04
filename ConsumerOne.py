from json import loads
from kafka import KafkaConsumer
from pymongo import MongoClient
from configurations import AppConfig


myConsumer = KafkaConsumer(
    "messages",
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='myGroup',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
Configs = AppConfig()
client = MongoClient(Configs.getMongoUrl())
coll = client.container.Test


for msg in myConsumer:
    msg = msg.value
    coll.insert_one(msg)
    print("data inserted")
    # print(f"{msg} added to {coll}")

# if __name__ == "__main__":
#     consumer = KafkaConsumer(
#         "messages",
#         bootstrap_servers="localhost:9092",
#         auto_offset_reset='earliest'
#     )
#
#     for messages in consumer:
#         print(loads(messages.value))
