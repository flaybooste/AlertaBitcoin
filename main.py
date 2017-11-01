from datetime import datetime
import vBit
from pygame import mixer

with open("arquivo.csv", "w") as _file:
    _file.write("hora, compra,venda ,moeda, fonte, ID\n")
    Cont = 1
    while True:
        if(Cont%2 == 1):
            _file.write(str(datetime.now().hour)+":"+str(datetime.now().minute)+":"+str(datetime.now().second)+","+str(vBit.Mbt(1))+","+str(vBit.Mbt(2))+","+" Bitcoin"+","+"MBT"+","+str(Cont)+"\n")
            if(float(vBit.Mbt(2)) > 23600):
                mixer.init()
                mixer.music.load("ring.mp3")
                mixer.music.play()
            print(str(datetime.now().hour)+":"+str(datetime.now().minute)+":"+str(datetime.now().second)+","+str(vBit.Mbt(1))+","+str(vBit.Mbt(2))+","+" Bitcoin"+","+"MBT"+","+str(Cont)+"\n")
            Cont += 1
            from time import sleep
            sleep(10)
        if(Cont%2 == 0):
            _file.write(str(datetime.now().hour)+":"+str(datetime.now().minute)+":"+str(datetime.now().second)+","+str(vBit.Nc(1))+","+str(vBit.Nc(2))+","+" Bitcoin"+","+"NC"+","+str(Cont)+"\n")
            if(vBit.Nc(2) > 23600):
                mixer.init()
                mixer.music.load("ring.mp3")
                mixer.music.play()
            print(str(datetime.now().hour)+":"+str(datetime.now().minute)+":"+str(datetime.now().second)+","+str(vBit.Nc(1))+","+str(vBit.Nc(2))+","+" Bitcoin"+","+"NC"+","+str(Cont)+"\n")
            Cont += 1
            from time import sleep
            sleep(10)
