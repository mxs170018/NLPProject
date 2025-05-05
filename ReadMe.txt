COMET NEWS READ ME
We used WSL on Windows to set up everything (you can also use a virtual machine that is running linux)

Make sure you have the following files in the CometNews folder downloaded from gitHub
	newsGrabber.py
	entityCounter.py
	cometNews.py
	requirementsNLP.txt
	temoc.png
	
To install the windows subsystem for linux on a windows computer run the following command on
windows command prompt in adminstrator mode and restart your computer when finished

	wsl --install

After restarting run the following commands to go into wsl and CD into your downloads (or cometNews is located)
and copy it to your home path in wsl *REMINDER THAT YOU CAN PASTE BY RIGHT CLICKING IN THE TERMNIAL*

	wsl 
	cd /mnt/c/Users/<YOUR-USERNAME>/Downloads/cometNews
	cp -r cometNews/ ~/
	cd ~

Then we download kafka and zookeeper from the web
	cd ~
	wget https://archive.apache.org/dist/kafka/2.4.1/kafka_2.13-2.4.1.tgz
	wget https://dlcdn.apache.org/zookeeper/zookeeper-3.9.3/apache-zookeeper-3.9.3-bin.tar.gz
	tar -xvzf kafka_2.13-2.4.1.tgz
	tar -xvzf apache-zookeeper-3.9.3-bin.tar.gz

I ran the following commands to get pip and virtual environments installed on WSL:

	sudo apt-get update
	sudo apt-get install python3-pip
	sudo apt-get install python3-venv
	sudo apt install qtwayland5


I created a virtual environment, activated it. Once activated, I installed all the dependencies
this will take a few minutes and only needs to be done the first time: *nlpProject can be replaced with anything*
	cd ~
	python3 -m venv nlpProject
	source ~/nlpProject/bin/activate 
	python3 -m pip install -r requirementsNLP.txt

I then opened up 6 different terminalks
1 In the first terminal I cd into the kafka folder and wrote the following commands:

	cd ~/kafka_2.12-3.4.1/
	bin/zookeeper-server-start.sh config/zookeeper.properties

2 In the second terminal I also CD Kafka folder and wrote the following command:

	cd ~/kafka_2.12-3.4.1/
	bin/kafka-server-start.sh config/server.properties

3 In the third terminal I CD into the kafka folder and created two topics using the following commands
(this only has to be done the first time):

	cd ~/kafka_2.12-3.4.1/
	bin/kafka-topics.sh --create --topic topic1 --bootstrap-server localhost:9092
	bin/kafka-topics.sh --create --topic topic2 --bootstrap-server localhost:9092

4 In the fourth terminal, I activated the virtual environment in this terminal 
and ran the first consumer (consumes on topic1 and produces on topic2):

	source ~/nlpProject/bin/activate 
	python3 ~/cometNews/entityCounter.py

5 In the fifth terminal I do something similar, but I run the second consumer (consumes on topic1)

	source ~/nlpProject/bin/activate
	python3 ~/cometNews/cometNews.py

6 In the sixth terminal I do something similar, but I run the first producer (produces on topic1)

	source ~/nlpProject/bin/activate 
	python3 ~/cometNews/newsGrabber.py

then we let this program run for 60 minutes, all the output should be shown in the cometNews.py GUI 
we can premptively close before the 60 minutes by closing the GUI and ctrl-c every terminal 

if we want to run this program again, you only need to open 5 terminals, run wsl on all of them and copy paste for
terminal 1-2 and 4-6 
