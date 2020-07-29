from datetime import datetime
from flask import Flask
from flask import request
from flask import render_template
from trafficScore import score

app = Flask(__name__)

@app.route('/')
def traffic_map():
    dt = datetime.now().strftime('%m-%d-%Y %H:%M')
    #scoreList = [0.1,0.2,0.3,0.4,0.5,0.6,0.7]
    #avg = 40
    #s = [x for x in range(38)]
    time = "now"
    scoreList, avg, s = score(time)
    scoreList2 = [round(x*100) for x in scoreList]
    return render_template('index.html',
                           scoreList=scoreList,
                           avg=avg,
                           scoreList2=scoreList2,
                           allScores=s,
                           datetime=dt)

@app.route('/',methods=['POST'])
def traffic_map_post():
    dtrequest = request.form['datetime']
    #newScoreList = [0.3,0.4,0.5,0.4,0.3,0.2,0.3]
    #avg = 34
    #s = [x for x in range(38)]
    newScoreList, avg, s = score(dtrequest)
    newScoreList2 = [round(x*100) for x in newScoreList]
    return render_template('index.html',
                           scoreList=newScoreList,
                           avg=avg,
                           scoreList2=newScoreList2,
                           allScores=s,
                           datetime=dtrequest)

if __name__ == "__main__":
    app.run()
