
from kafka import KafkaConsumer
import json
from kafka.errors import KafkaError


def json_deserializer(data):
    return json.loads(data)

# each consumer will be in a consumer group
consumer = KafkaConsumer(
                        bootstrap_servers=["localhost:9092","localhost:9093"],
                        auto_offset_reset='earliest',
                        group_id="C1",
                        key_deserializer=json_deserializer,
                        value_deserializer=json_deserializer)
consumer.subscribe(["Reg_User","Data_User"])

if __name__ == "__main__":
    print("Starting")
    for msg in consumer:
        print("Key: ", msg.key)
        print("Key: ", msg.value["price"])
        print("Key: ", type(msg.value))
        log1 = json.dumps(msg.value)
        print(type(log1))
        print("Reg_User: ", type(log1))


   
    
        
