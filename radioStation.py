class radioStation:

    def __init__(self):
        self.radioStationList = {};
        f = open('radioList', 'r')
        for x in f.read().split('\n'):
            if not (x == '' or x[0]=='#') :
                name = x.split(',')[0]
                name.strip()
                addr = x.split(',')[1]
                addr.strip()
                addr = addr.split('://')[1]
                addr = 'x-rincon-mp3radio://' + addr
                self.radioStationList[name] = addr


    def list(self):
        return self.radioStationList

    def listStations(self):
        return self.radioStationList.keys()

    def getByName(self, statioName):
        return self.radioStationList.get(statioName)

    def getStationFromUri(self,uriToLookFor):
        for name, uri in self.radioStationList.items():
            print(uriToLookFor.find(uri),uri,uriToLookFor)
            if uriToLookFor.find(uri)>0:
                return name




def addRadioStation(self,stationName,stationUri,stationImg = None):
        raise "Not implemented - mach mal ;)"
