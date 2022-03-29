
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json 
from Data_Generator import get_reg_user
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

# only one producer for now we can have multiple producer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        key_serializer=json_serializer,
                        value_serializer=json_serializer,
                        )
# for this we need to start a new kafka server in a new 
# terminal and provide a new server.properties file
# which will have diff broker.id, port, log folder

# we can also give this bootstrap above as a list 

producer1 = KafkaProducer(bootstrap_servers=['localhost:9093'],
                        key_serializer=json_serializer,
                        value_serializer=json_serializer,
                        )


if __name__ == "__main__":
    while 1==1:
        try:
            reg_user = get_reg_user()
            print(reg_user)
            metadata = producer.send(topic="Reg_User", key="first", value=reg_user)
            
        except KafkaError:
            pass

        try:
            reg_user = get_reg_user()
            print(reg_user)
            metadata = producer.send(topic="Data_User", key="second", value=reg_user)
            
        except KafkaError:
            pass

     

        # sync call will block and get metadata
        # try:
        #     record_metadata = metadata.get(timeout=10)
        # except KafkaError:
        #     pass

        # # Successful result returns assigned partition and offset
        # # These are used for sync calls only will not work for async
        # print (record_metadata.topic)
        # print (record_metadata.partition)
        # print (record_metadata.offset)
                
        time.sleep(3)