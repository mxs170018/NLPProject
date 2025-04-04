# MXS170018
# MANUEL SALADO ALVARADO

from newsapi import NewsApiClient
import time 
from kafka import KafkaProducer
from json import dumps

def getNews(sources):
    #print(sources)
    sourcesString = [x.replace(" ","-") for x in sources]
    source = ",".join(sourcesString)
    #print(source)
    top_head = news.get_everything(sources=source, language="en")
    #print(top_head.values())
    #print(top_head.keys())
    articles = top_head["articles"][:]

    newsContent = [x["title"] for x in articles]
    newsStringRaw = " ".join(newsContent)
    return newsStringRaw


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
print("start")
news = NewsApiClient(api_key='1727d8504482453fa91b96e5c3835093')
sourcesRaw = news.get_sources()['sources']
sources = [x["name"] for x in sourcesRaw if x['country']=='us']

count = 0 
while count < 20:
    newsStringRaw = getNews(sources)
    producer.send('topic1',newsStringRaw)
    producer.flush()
    time.sleep(180)
    
    count = count +1

