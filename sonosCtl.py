from soco import SoCo


class sonosCtl:

    def __init__(self):
        self.players = {}
        self.ALL_PLAYERS = "@All"
        f = open('playerList', 'r')
        for x in f.read().split('\n'):
            if not (x == '' or x[0] == '#'):
                name = x.split(',')[0]
                name.strip()
                addr = x.split(',')[1]
                addr.strip()
                self.players[name] = addr
        self.selectedPlayerIp = list(self.players.values())[0]

    def listPlayers(self):
        return self.players

    def setActivePlayer(self, playerName):
        self.selectedPlayerIp = self.players.get(playerName)

    def playIt(self,uri,sonosDevice):
        sonosDevice.clear_queue()
        sonosDevice.add_uri_to_queue(uri,1,False)
        #sonosDevice.next()
        if not sonosDevice.get_current_transport_info()['current_transport_state'] == 'PLAYING':
         sonosDevice.play()

    def playOnSonos(self, uri, playerName = ""):
        if playerName == "":
            sonos = SoCo(self.selectedPlayerIp)
            self.playIt(uri,sonos)
            return

        if playerName == self.ALL_PLAYERS:
            for k, v in self.players.items():
                self.playIt(uri,SoCo(self.players.get(k)))
            return

        if not playerName == "":
            self.playIt(uri,SoCo(self.players.get(playerName)))
            return

    def stopAllSonos(self):
        for k, v in self.players.items():
            sonos = SoCo(v)
            #sonos.pause()
            sonos.stop()

    def pauseSonos(self):
        sonos = SoCo(self.selectedPlayerIp)
        #sonos.pause()
        sonos.stop()

    def changeVolume(self, how):
        sonos = SoCo(self.selectedPlayerIp)
        currentVol = sonos.volume
        if how == "+": sonos.volume = currentVol + 1
        if how == "-":
            if currentVol > 1:
                sonos.volume = currentVol - 1

    def extractUriDomain(self, uri):
        uri = uri.replace("x-rincon-mp3radio://", "")
        uri = uri.replace("https://", "")
        uri = uri.replace("http://", "")
        if uri.find("?") == -1:
            return uri[:uri.rfind("/")]
        else:
            return uri[:uri.rfind("?")]

    def getSonosInfo(self):
        sonos = SoCo(self.selectedPlayerIp)
        track = sonos.get_current_track_info()
        track['Volume'] = sonos.volume
        track['PlayerName'] = sonos.player_name
        track['CurrentStation'] = self.extractUriDomain(track['uri'])
        track['PlayerStatus'] = sonos.get_current_transport_info()['current_transport_state']
        return track
