import time
from datetime import datetime
import re
import json
import googlemaps

# Replace apikey with your key
gmaps = googlemaps.Client(key='apikey')

# origin, destination
locTup = (
    ['30.280044, -97.743361','30.313779, -97.658138'], #School Commute EB East
    ['30.313779, -97.658138','30.280044, -97.743361'], #School Commute WB East
    ['30.222907, -97.708345','30.313779, -97.658138'], #Work Commute 183 NB East
    ['30.313779, -97.658138','30.222907, -97.708345'], #Work Commute 183 SB East
    ['30.277270, -97.637398','30.278718, -97.728187'], #MLKJr WB East
    ['30.278718, -97.728187','30.277270, -97.637398'], #MLKJr EB East
    ['30.338714, -97.700569','30.251535, -97.736181'], #I35 SB East/Central
    ['30.251516, -97.735975','30.338242, -97.700580'], #I35 NB East/Central
    ['30.339445, -97.699775','30.455600, -97.666193'], #I35 NB North
    ['30.455452, -97.666488','30.339727, -97.699907'], #I35 SB North
    ['30.439746, -97.698714','30.380310, -97.737676'], #Mopac SB North
    ['30.380782, -97.737131','30.439738, -97.698304'], #Mopac NB North
    ['30.345083, -97.579556','30.449541, -97.789113'], #183/290 WB North
    ['30.456560, -97.792947','30.343735, -97.580281'], #183/290 EB North
    ['30.346590, -97.713702','30.267324, -97.756050'], #Lamar SB Central
    ['30.267514, -97.755788','30.345670, -97.713355'], #Lamar NB Central
    ['30.384012, -97.742568','30.274586, -97.771248'], #Mopac SB West/Central
    ['30.274556, -97.770933','30.386600, -97.743522'], #Mopac NB West/Central
    ['30.389073, -97.746727','30.251255, -97.807161'], #360 SB West
    ['30.252033, -97.807397','30.388869, -97.746620'], #360 NB West
    ['30.266643, -97.783202','30.304497, -97.841264'], #Bee Cave WB West
    ['30.304300, -97.841127','30.266485, -97.783251'], #Bee Cave EB West
    ['30.186478, -97.609724','30.216184, -97.741348'], #71 WB Southeast
    ['30.215915, -97.741541','30.187503, -97.598238'], #71 EB Southeast
    ['30.243616, -97.691136','30.197894, -97.763069'], #Montopolis/Stassney SB Southeast
    ['30.197769, -97.763125','30.242718, -97.690905'], #Montopolis/Stassney NB Southeast
    ['30.215055, -97.752371','30.140223, -97.796182'], #I35 SB South/Southeast
    ['30.140316, -97.795828','30.214679, -97.752152'], #I35 NB South/Southeast
    ['30.260763, -97.745594','30.223776, -97.763426'], #Congress SB South Central
    ['30.223729, -97.763383','30.260703, -97.745533'], #Congress NB South Central
    ['30.248579, -97.736631','30.269044, -97.774817'], #Riverside/Barton Springs WB South Central
    ['30.268993, -97.774868','30.248064, -97.736163'], #Riverside/Barton Springs EB South Central
    ['30.167163, -97.787645','30.200508, -97.865021'], #Slaughter WB South
    ['30.200341, -97.865148','30.167001, -97.787639'], #Slaughter EB South
    ['30.229339, -97.788806','30.140585, -97.833043'], #Manchaca SB South
    ['30.140575, -97.832991','30.229536, -97.788565'], #Manchaca NB South
    ['30.233936, -97.741939','30.269178, -97.775243'], #Oltorf/Barton Springs WB South
    ['30.269057, -97.775248','30.233914, -97.742028'], #Oltorf/Barton Springs EB South
    ['30.421560, -97.704020','30.200323, -97.867237'], #Mopac SB Cross-regional
    ['30.199794, -97.865853','30.420924, -97.703861'], #Mopac NB Cross-regional
    ['30.449221, -97.790820','30.183504, -97.687593'], #183 SB Cross-regional
    ['30.183187, -97.687409','30.449560, -97.790474'], #183 NB Cross-regional
    ['30.455452, -97.666488','30.140223, -97.796182'], #I35 SB Cross-regional
    ['30.140090, -97.795891','30.455558, -97.666213'], #I35 NB Cross-regional
    )

def traffic(time):
    durations = []
    
    if time == "now":
        dt = datetime.now()
    else:
        year = int(time[6:10])
        month = int(time[:2])
        day = int(time[3:5])
        hour = int(time[11:13])
        minute = int(time[14:16])
        t = datetime(year,month,day,hour,minute)
        dt = t.timestamp()
        
    for route in locTup:
        distance_result = gmaps.distance_matrix(origins=route[0],
                                                destinations=route[1],
                                                units='imperial',
                                                departure_time=dt)
        data = json.dumps(distance_result)
        dist = json.loads(data)
        dist = dist["rows"][0]["elements"][0]["duration_in_traffic"]["text"]
        
        if bool(re.search('\d+(?=\shour)',dist)) == False:
            hours = 0
        else:
            hours = re.search('(\d+(?=\shour))',dist).group(1)
        minutes = re.search('(\d+(?=\smin))',dist).group(1)
        total = int(hours) * 60 + int(minutes)
        durations.append(total)

    return durations
