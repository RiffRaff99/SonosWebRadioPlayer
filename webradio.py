import logging
import json
from radioStation import radioStation
from sonosCtl import sonosCtl
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
app.config.from_pyfile("settings.py")
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/stationlist", methods=["Get"])
def stationList():
    return(json.dumps(stations.list()))

@app.route("/switchPlayer", methods=["Post"])
def switchMediaPlayer():
    zoneCtl.setActivePlayer(request.json['PlayerName'])
    return "Ok"

@app.route("/playuri", methods=["POST"])
def play():
    uri = request.json['uri']
    playerName = request.json['player']
    zoneCtl.playOnSonos(uri,playerName)
    return "Ok"

@app.route("/pauseall")
def pauseAll():
    zoneCtl.stopAllSonos()
    return "Ok"

@app.route("/pause")
def pause():
    zoneCtl.pauseSonos()
    return "Ok"

@app.route("/info")
def info():
    track = zoneCtl.getSonosInfo()
    return json.dumps(track)

@app.route("/volup")
def volUp():
    zoneCtl.changeVolume("+")
    return "Ok"

@app.route("/voldown")
def volDown():
    zoneCtl.changeVolume("-")
    return "Ok"

@app.route("/")
def index():
    track = zoneCtl.getSonosInfo()
    return render_template('index2.html', track=track, stationList=stations.list(), playerList=zoneCtl.listPlayers())


if __name__ == "__main__":
    stations = radioStation()
    zoneCtl = sonosCtl()
    app.run(debug=False,host= '0.0.0.0')
