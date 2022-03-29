# Kafka_Demo_Python

For installing and running Kafka we have some pre-req

- Java

Will need to have Java 11 installed in our system, why java 11 because the cluster manager for Kafka that we will be using to manage our kafka related stuff
need Java 11 else we won't be able to access that. I have installed Zulu Java 11 for ubuntu and then added its path in my system.

Your path will be different from mine

vim ~/.bashrc


export JAVA_HOME=/home/ubuntu/Java/zulu8.60.0.21-ca-jdk8.0.322-linux_x64
export PATH=$PATH:$JAVA_HOME/bin

source ~/.bashrc

- Python

After we have Java will Install Python

sudo apt-get update
sudo apt-get install python3 
sudo apt-get install pip


vim ~/.bashrc

export PATH=$PATH:/home/ubuntu/.local/bin

source ~/.bashrc


-- Zookeeper and Kafka

Now we install zookeeper and kafka server both will be in the same file will download this from google just type kafka download.
Remember to download the binary one and not the source one because we then have to build that on our own.

Will download the zip file and unzip it and will get he folder

In the Conf File of Kafka Server we need to provide our IP of machine on which kafka is hosted and similarly for zookeeper

server.properties
advertised.listeners=PLAINTEXT://your.host.name:9092
zookeeper.connect=localhost:2181

kafka-server port 9092
zookeeper 2181

Change Directory to the kafka directory start the zookeeper after the above Changes have been made 

Open Terminal

bin/zookeeper-server-start.sh config/zookeeper.properties

The above command will start the Zookeeper


JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties



to start the kafka server 
we use JMC so that we can use a GUI to make topics and all things 


- Kafka Manager 

git clone https://github.com/yahoo/CMAK.git
.sbt clean inside this 
./sbt clean dist

A target folder will be created and an universal folder and will have a folder which is zip we need to unzip that all the files html one we will get

Inside the cmak.zkhosts file we need to provide our IP

CMAK/target/universal/cmak-3.0.0.5
Inside conf will have application.conf

After all of this we will now start our kafka manager

bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080

http://localhost:8080/

Above on browser of your choice and will open the Kafka Manager where we can make clusters, topics etc
