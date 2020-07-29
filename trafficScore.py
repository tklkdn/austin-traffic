import sqlite3
from getTraffic import traffic

routeList = ["SchoolCommuteEBEast",
             "SchoolCommuteWBEast",
             "WorkCommute183NBEast",
             "WorkCommute183SBEast",
             "MLKJrWBEast",
             "MLKJrEBEast",
             "I35SBEastCentral",
             "I35NBEastCentral",
             "I35NBNorth",
             "I35SBNorth",
             "MopacSBNorth",
             "MopacNBNorth",
             "Str183290WBNorth",
             "Str183290EBNorth",
             "LamarSBCentral",
             "LamarNBCentral",
             "MopacSBWestCentral",
             "MopacNBWestCentral",
             "Str360SBWest",
             "Str360NBWest",
             "BeeCaveWBWest",
             "BeeCaveEBWest",
             "Str71WBSoutheast",
             "Str71EBSoutheast",
             "MontopolisStassneySBSoutheast",
             "MontopolisStassneyNBSoutheast",
             "I35SBSouthSoutheast",
             "I35NBSouthSoutheast",
             "CongressSBSouthCentral",
             "CongressNBSouthCentral",
             "RiversideBartonSpringsWBSouthCentral",
             "RiversideBartonSpringsEBSouthCentral",
             "SlaughterWBSouth",
             "SlaughterEBSouth",
             "ManchacaSBSouth",
             "ManchacaNBSouth",
             "OltorfBartonSpringsWBSouth",
             "OltorfBartonSpringsEBSouth",
             "MopacSBCrossRegional",
             "MopacNBCrossRegional",
             "Str183SBCrossRegional",
             "Str183NBCrossRegional",
             "I35SBCrossRegional",
             "I35NBCrossRegional"]

def fetchData():
    conn = sqlite3.connect("TrafficData.db")
    c = conn.cursor()
    
    maxList = []
    minList = []
    normList = []
    for route in routeList:
        c.execute("SELECT max({r}), min({r}) FROM duration".format(r=route))
        rows = c.fetchall()
        
        max_val = [x[0] for x in rows][0]
        min_val = [x[1] for x in rows][0]
        norm_val = max_val - min_val

        maxList.append(max_val)
        minList.append(min_val)
        normList.append(norm_val)

    conn.close()

    return maxList, minList, normList

def score(time):
    maxList,minList,normList = fetchData()
    durations = traffic(time)

    s = []
    for d,m,n in zip(durations,minList,normList):
        score = int((d - m) / n * 100)
        s.append(score)

    east = (s[2]+s[3]+s[4]+s[5]+s[6]+s[7]) / 600
    central = (s[6]+s[7]+s[14]+s[15]+s[16]+s[17]) / 600
    north = (s[8]+s[9]+s[10]+s[11]+s[12]+s[13]) / 600
    west = (s[16]+s[17]+s[18]+s[19]+s[20]+s[21]) / 600
    southeast = (s[22]+s[23]+s[24]+s[25]+s[26]+s[27]) / 600
    south = (s[26]+s[27]+s[32]+s[33]+s[34]+s[35]+s[36]+s[37]) / 800
    southcentral = (s[28]+s[29]+s[30]+s[31]) / 400
    cross = (s[38]+s[39]+s[40]+s[41]+s[42]+s[43]) / 600

    # weighted average (greater weight on highways)
    avg = int(round((sum(s[2:38])/36)*0.7+(sum(s[38:44])/6)*0.3))

    scoreList = []
    scoreList.append(central)
    scoreList.append(north)
    scoreList.append(east)
    scoreList.append(southeast)
    scoreList.append(southcentral)
    scoreList.append(south)
    scoreList.append(west)

    return scoreList, avg, s
