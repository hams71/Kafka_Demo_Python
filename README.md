# Kafka_With_Python

### Table of Contents

- [Overview](#overview)
- [Kafka](#kafka)
- [Kafka Installation](#kafka-installation)
- [Folder Structure](#folder-structure)
- [Program Flow](#program-flow)
- [Program Execution](#program-execution)
- [Level Up](#level-up)
- [Documentation and Material](#documentation-and-material)
- [Tools and Technologies](#tools-and-technologies)

---

### Overview

- Learn about Kafka and how is can be used in streaming data.
- Generated sales data in json and used Kafka with python to push this data to Power BI.

---

### Kafka

- Apache Kafka is a distributed event store and stream-processing platform.


### Kafka Installation

- For installing and running Kafka we have to install some programs.

#### Java

- Java 11 installed in our system, why java 11 because the cluster manager UI for kafka requires java 11. 
- I have installed Zulu Java 11 for ubuntu and then added its path in my system.

- After you have installed Java 11 will need to set the paths
```bash
  vim ~/.bashrc
```
- Once you have enter vim press **i** so that you can be in insert mode. Paste the below.
```bash
  export JAVA_HOME=/home/ubuntu/Java/zulu8.60.0.21-ca-jdk8.0.322-linux_x64
  export PATH=$PATH:$JAVA_HOME/bin
```

- Press **Esc** and enter **:x** to exit vim. 
- Now to updathe bashrc file
```bash
  source ~/.bashrc
```

#### Python

```bash
  sudo apt-get update
```
```bash
  sudo apt-get install python3
```
```bash
  sudo apt-get install pip
```
```bash
  vim ~/.bashrc
```
```bash
  export PATH=$PATH:/home/ubuntu/.local/bin
```
```bash
  source ~/.bashrc
```

### Zookeeper and Kafka

- Now we install zookeeper and kafka server both will be in the same file will download this from google just type kafka download.
- Remember to download the binary one and not the source one because we then have to build that on our own.
- Download the zip file and unzip it and will get the folder

- In the Conf File of Kafka Server we need to provide our IP of machine on which kafka is hosted and similarly for zookeeper
- We are defining the ports 
```bash
  server.properties
  advertised.listeners=PLAINTEXT://your.host.name:9092
  zookeeper.connect=localhost:2181
```


- Change Directory to the kafka directory start the zookeeper after the above Changes have been made. 

- Open Terminal
- This will start Zookeeper
```bash
  bin/zookeeper-server-start.sh config/zookeeper.properties
```

- Start the kafka server we use JMX so that we can use Cluster Manger UI to make topics and have more details 
```bash
  JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties
```





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
