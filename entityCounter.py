# MXS170018
# MANUEL SALADO ALVARADO

import re, string
import spacy
from kafka import KafkaConsumer, KafkaProducer
from json import dumps 

consumer = KafkaConsumer(
    'topic1',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: x.decode('utf-8')
)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")
entityCount = {}
for message in consumer:
    
    newsStringRaw = message.value
    newString = re.sub(r'[^A-Za-z ]+', ' ', newsStringRaw)
    #print(newString.split(),"WAG")
    stop_words = nlp.Defaults.stop_words


    flatCleanerText = [x for x in newString.split() if x.lower() not in stop_words]

    #temp = [x.replace(" ","") for x in flatCleanerText]

    newsString = " ".join(flatCleanerText)

    allEnts = nlp(newsString).ents
    entities = [ents.text for ents in allEnts]
    entities = [x.replace(" s","") for x in entities]
    entities = [x.replace("U S","US") for x in entities]
    
    for ent in entities:
        if ent in entityCount:
            entityCount[ent] = entityCount[ent] +1
        else:
            entityCount[ent] = 1
    producer.send('topic2',entityCount)
    producer.flush()
    #print(entityCount)
exit()