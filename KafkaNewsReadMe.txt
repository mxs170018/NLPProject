I used WSL with Ubuntu to set up everything 
Make sure you have the following files in your directory
	newsGrabber.py
	entityCounter.py
	barGraph.py
	kafka.x.x.x
	zookeeper.x.x.x
	requirements.txt
	

I ran the following commands to get pip installed on WSL:

	sudo apt-get update
	sudo apt-get install python3-pip

then I wget the tar for kafka and zookeeper and I unzipped them within my home directory 


I created a virtual environment, activated it. Once activated, I installed all the dependencies:
	python3 -m venv <virtualEnvName>
	source <virtualEnvName>/bin/activate 
	python3 -m pip install -r requirements.txt

I then opened up 5 different ubuntu terminals 
In the first terminal I cd into the unzipped kafka folder and wrote the following command:
	bin/zookeeper-server-start.sh config/zookeeper.properties

In the second terminal I also CD into the unzipped kafka folder and wrote the following command:
	bin/kafka-server-start.sh config/server.properties

In the third terminal I created two topics using the following commands:
	bin/kafka-topics.sh --create --topic topic1 --bootstrap-server localhost:9092
	bin/kafka-topics.sh --create --topic topic2 --bootstrap-server localhost:9092

afterwards, I activated the virtual environment in this terminal and ran the first consumer (consumes on topic1 and produces on topic2):
	source <virtualEnvName>/bin/activate 
	python3 entityCounter.py

In the fourth terminal I do something similar, but I run the second consumer (consumes on topic1)
	source <virtualEnvName>/bin/activate 
	python3 barGraph.py

In the fifth terminal I do something similar, but I run the first producer (produces on topic1)
	source <virtualEnvName>/bin/activate 
	python3 newsGrabber.py

then we let this program run for 60 minutes, all the output should be shown in the bargraph.py terminal