# Using Kafka to recieve and send messages to Python apps
In this project I built a food order app that generates orders, sends it to Kafka, and Kafka relays to the other apps.
![TerminalKafka](https://user-images.githubusercontent.com/30685241/184810166-f6004801-5fea-4cad-b559-ef6f6faf901b.jpg)



## Technologies Used
* Python
* Docker
* Kafka

## Dependencies
* Install Python- https://www.python.org/downloads/
* Install Docker - https://docs.docker.com/get-docker/
* Install Kafka (Docker) - https://hub.docker.com/r/confluentinc/cp-kafka/
```
docker pull confluentinc/cp-kafka
```
* Install Kafka (Python) - https://kafka-python.readthedocs.io/en/master/
```
pip install kafka-python
```

## Executing program
* Download the repository to your computer go to project file
```
git clone https://github.com/sayedh/python-kafka-order_app
cd python-kafka-order_app
```
* Run the Docker Compose file, once complete leave this terminal open
```
docker compose up
```

* In new terminals, run these commands. One per terminal. 
```
python email.py
python analytics.py
python transaction.py
```

* Now start generating orders
```
python orders.py
```
