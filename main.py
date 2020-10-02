import soco
from radioStation import radioStation
from tkinter import *



deviceSet = None
currentDev = None

def discoverDevices():
    d = soco.discovery.discover(10,True,'192.168.178.47')
    return d

def getDeviceFromList(deviceName, deviceSet):
    for x in deviceSet:
        if x.player_name == deviceName:
            return x
    return None

if __name__ == "__main__":
    deviceSet = discoverDevices()
    for x in deviceSet:
        print(x.player_name)
    currentDev = getDeviceFromList('Wohnzimmer',deviceSet)
    """currentDev.stop()
    print(currentDev.get_current_transport_info())
    currentDev.play_uri(uri)
    print(currentDev.get_current_transport_info())
    currentDev.ramp_to_volume(20)
    print(currentDev.volume)
    """
    stations = radioStation()
    uri = stations.getByName("egoFm")
    print(uri)
    currentDev.play_uri(uri)



    root = Tk()
    root.title("Listbox demo")
    root.geometry("400x480")


    lbStations = Listbox(root)
    lbStations.pack(pady=15)
    for x in stations.listStations():
        print(x)
        lbStations.insert(END,x)

    root.mainloop()