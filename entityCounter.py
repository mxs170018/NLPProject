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
#spacy.cli.download("en_core_web_trf")
nlp = spacy.load("en_core_web_trf")
entityCount = {}
for message in consumer:
    print("CHICKEN JOCKEY")
    excluded_labels = {"CARDINAL", "ORDINAL", "QUANTITY", "PERCENT", "DATE", "TIME", "MONEY"}
    excluded_words = {"year", "million", "billion", "percent", "month", "week"}
    newsStringRaw = message.value
    newsString = re.sub(r'[^A-Za-z ]+', ' ', newsStringRaw)
    
    stop_words = nlp.Defaults.stop_words


    flatCleanerText = [x for x in newsString.split() if x.lower() not in stop_words]
    
    #temp = [x.replace(" ","") for x in flatCleanerText]

    newsString = " ".join(flatCleanerText)
    words = nlp(newsString)
    
    allEnts = words.ents
    entities = [
                ent.text for ent in allEnts
                if ent.label_ not in excluded_labels and ent.text.lower() not in excluded_words
                ]
    print(entities)
    for ent in entities:
        if ent in entityCount:
            entityCount[ent] = entityCount[ent] +1
        else:
            entityCount[ent] = 1
    print(entityCount)
    producer.send('topic2',entityCount)
    
    producer.flush()
    #print(entityCount)
exit()