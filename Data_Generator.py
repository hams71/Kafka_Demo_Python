from faker import Faker
import datetime
import random


faker = Faker()
ts = datetime.datetime.now()



def get_reg_user():
    return {
        #"name":faker.name(),
        #"address":faker.address(),
        #"created_at":faker.year(),
        "country":faker.country(),
        "price":random.randint(5,1000),
        "time":datetime.datetime.now().isoformat()
    }


if __name__ == "__main__":
    print(get_reg_user())