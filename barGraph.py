# MXS170018
# MANUEL SALADO ALVARADO

from kafka import KafkaConsumer
import json
import asciibars

consumer = KafkaConsumer(
    'topic2',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: x.decode('utf-8')
)
# wa = "{'US': 20, 'Syrian Democratic Forces': 10, 'Newsweek': 60, 'Kurdish': 10, 'Syria': 10, 'Don': 10, 'Donald Trump': 80, 'Matt Gaetz': 30, 'dozen': 10, 'Boston Massachusetts': 10, 'Saturday': 40, 'today': 20, 'nPatient Hospital': 10, 'day week': 10, 'Monday': 180, 'Josh AllenLauren Leigh Bacho': 10, 'Kansas City': 10, 'Week': 20, 'fourth fourth quarter': 10, 'Los Angeles Lakers': 10, 'Pat Riley': 20, 'Star Plaza': 10, 'Utqiavik Alaska': 10, 'winters': 10, 'US December': 10, 'zero': 10, 'Joice Barnard': 10, 'year ago': 10, 'years': 30, 'Elon Musk': 30, 'OpenAI': 30, 'Josh Kushner': 10, 'Thrive Capital': 10, 'CBS News': 50, 'CBS Interactive Inc': 60, 'nGet': 50, 'Ohio': 20, 'Republican': 10, 'Jason Stephens': 10, 'past years': 10, 'Ohio House': 10, 'UFC': 50, 'Jim Miller': 10, 'Elon Musk Vivek Ramaswamy': 10, 'nMiller': 10, 'U u chars': 10, 'Calif': 10, 'LOUISVILLE Ky': 10, 'week': 20, 'Louisville': 10, 'WEST PALM': 10, 'Tuesday': 10, 'Spencer Lawton Jr Georgia': 10, 'Savannah': 10, 'Midnight Gard': 10, 'WiFi Money': 10, 'Nebraska': 10, 'million': 10, 'Tuesda': 10, 'NEW YORK': 20, 'Dana White': 10, 'Bo Nickal': 10, 'Paul Craig': 10, 'Energy': 30, 'nPresident': 10, 'Amari Cooper': 10, 'NFL': 20, 'Oakland Raiders': 10, 'Image Cath Virginia Verge Getty Images r n n n n n Emails': 10, 'Microsoft': 10, 'tha u chars': 10, 'Florida': 10, 'Joel Leppard': 10, 'Gaetz': 10, 'Venmo': 10, 'Israeli': 20, 'Benjamin Netanyahu': 10, 'countrys air': 10, 'Iran': 10, 'Tehrans': 10, 'Chris Wright': 30, 'Liberty Energy': 10, 'Atalanta Parma': 10, 'Lookman Dennis Man Serie': 10, 'nAtalanta': 10, 'Udinese': 10, 'AC Milan': 10, 'Christian': 10, 'Dusan Vlahovic': 10, 'Serie': 10, 'Business Insider': 10, 'Learn': 10, 'Insider home': 10, 'Natasha Rothwell': 10, 'Rothwell': 10, 'Hulu Die': 10, 'Copyright u': 10, 'Ben Affleck': 10, 'nLast week': 10, 'CNBC': 10, 'Delivering Alpha': 10, 'FOX House Homeland Security Committee': 10, 'FEMA': 10, 'Trump': 10, 'nRob': 10, 'nTheir Ro u chars Entertainment gossip': 10, 'Tree Hill': 10, 'Paul Teal': 20, 'Friday': 20, 'November': 30, 'nEmilia Torello': 10, 'Instagram': 10, 'Josh Tree Hill': 10, 'Fox News Digital': 10, 'nTim McGraw': 10, 'Gracie McGraw': 10, 'Sunday': 30, 'Amazon': 10, 'Black Friday Week deals Nov Nov Friday': 10, 'Thanksgiving': 10, 'Cyber Monday': 10, 'Fields Mistria': 10, 'NPC Studio': 10, 'Buckeyes': 10, 'Quinshon Judkins': 10, 'half': 10, 'NCAA': 10, 'Northwestern Wildcats Wrigley Field': 10, 'Chicago': 20, 'Google': 10, 'nGoogle': 10, 'Chrome': 10, 'Android': 20, 'Los Angeles USA College Football Playoff National Championship': 10, 'Los Angeles Airport': 10, 'Marriott Mandatory Credit': 10, 'Kirby Lee USA': 10, 'Lindsey Graham': 20, 'South Carolina': 10, 'Houthis June': 10, 'Yemen': 10, 'Xinhua News Agency': 20, 'Oklahomas': 10, 'Sean Diddy Combs': 20, 'nHow': 10, 'Hawaii': 10, 'Moana Surf': 10, 'Harry Getty Images': 20, 'Cincinnati': 10, 'Dallas': 20, 'season Week': 10, 'Library Congress': 10, 'Al Jazeera': 10, 'Swedish': 10, 'Europe': 10, 'Beirut': 10, 'days': 10, 'Lebanons': 10, 'Ministry Public Health': 10, 'Israel': 10, 'nKate Moss': 10, 'years old': 10, 'Wednesday': 20, 'ATHENS': 20, 'Greece Greece': 20, 'billion euros billion': 20, 'Kyriakos Mitsotakis': 20, 'Athens': 20, 'WASHINGTON Fossil': 20, 'safaris': 10, 'JACKSONVILLE Fla Jaguars': 10, 'Gabe Davis': 10, 'Doug Pederson': 10, 'second': 10, 'Joe Gibbs Racing': 10, 'Joey Logano': 10, 'Tony Stewart': 10, 'NASCAR': 10, 'ATLANTIC CITY': 10, 'New Jersey': 20, 'October': 20, 'Atlantic City': 20, 'ATLANTIC CITY N J': 10, 'BOSTON': 10, 'Boston': 10, 'Jewish': 10, 'nAle': 10, 'New York': 10, 'Todd Blanche': 10, 'Tru': 10, 'Mike Tyson': 10, 'Jake Paul': 10, 'year old': 10, 'afternoon': 10, 'night': 20, 'decent day': 10, 'Joe Brennan Jr': 10, 'Iraq': 10, 'Monday years': 10, 'January': 10, 'US Capitol r nEdward': 10, 'Kaley Cuoco': 10, 'Matilda': 10, 'Tom Pelphrey': 10, 'Fox News': 10, 'charshopping pet owner': 10, 'nSean Manaea': 10, 'nPer ESPN': 10, 'Alden Gonz': 10, 'New York Mets million': 10, 'Jose Antonio Ibarra': 10, 'Laken Riley': 10, 'earlier year': 10, 'Venezuelan': 10, 'Tren de Aragua': 10, 'Schmitt': 10, 'Ohio State': 10, 'F Noever FC Bayern Getty Images': 10, 'nDaniel Jones': 10, 'New York Giants': 10, 'Giants': 10, 'Tommy DeVito cent': 10, 'Houston Texans': 10, 'Jeff Okudah': 10, 'tonight': 10, 'Adam Schefter': 10, 'Nov PM ET': 10, 'nMiami Heat': 10, 'Jimmy Butler': 10, 'Philadelphia': 10, 'Jaquez Jr Terry Rozier': 10, 'Apple': 20, 'Steve Jobs': 10, 'nAlthough App': 10, 'Star Trek': 10, 'Trek': 10, 'nThe Braves': 10, 'Cubs': 10, 'MSNBC': 10, 'Morning Joe': 10, 'Joe Scarborough Mika Brzezinski': 10, 'Mar Lago': 10, 'Northwest': 10, 'National Weather Service': 10, 'St Louis Cardinals': 10, 'second year row': 10, 'Octobereason': 10, 'Auburn Tigers': 20, 'Jahki Howard': 10, 'Miles Kelly Auburn Tigers': 10, 'Vermont': 10, 'Iowa': 10, 'Brendan Sullivan': 10, 'Maryland': 10, 'ESPN': 10, 'McNamara': 10, 'Mayra Bueno Silva': 10, 'Jasmine Jasudavicius': 10, 'February': 10, 'Saudi Arabia': 10, 'National Weather Service NWS': 10, 'Texas': 10, 'morning': 10, 'Earth': 10, 'nRost Shutterstock': 10, 'Earths': 10, 'Nomad': 10, 'iPhone': 10, 'Apple Watch': 10, 'nGetty Images iStockphoto r nHome': 10, 'Shortly Game Awards': 10, 'Geoff Keighley': 10, 'nominees year': 10, 'Black Myth Wukong': 10, 'Twitter': 10, 'PORTLAND Maine': 10, 'America': 10, 'SEATTLE SEATTLE AP Boeing': 10, 'Washington Employment Security Department': 10}"
# water = wa.replace("\'","\"")
# theDict = json.loads(water)

# theDict2 = sorted(theDict,key=theDict.get,reverse=True)
# out = theDict2[0:10]

# bars = []
# for ent in out:
#     bars.append((ent,theDict[ent]))
# asciibars.plot(bars)
count = 0
for message in consumer:
    theJson = message.value
    toLoad = theJson.replace("\'","\"")
    theDict = json.loads(toLoad)

    toSort = sorted(theDict,key=theDict.get,reverse=True)
    out = toSort[0:10]

    bars = []
    for ent in out:
        bars.append((ent,theDict[ent]))
    print("Time:",count)
    asciibars.plot(bars)
    print("\n\n\n")
    count = count +3
    
