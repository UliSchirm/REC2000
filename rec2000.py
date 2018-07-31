import serial, math, sys

# Serial Port öffnen
schnittstellenFehler = 1
while schnittstellenFehler == 1:
    try:
        ser = serial.Serial('/dev/tty.wchusbserial1450')
        schnittstellenFehler = 0
    except:
        input ("Die serielle Schnittstelle konnte nicht geöffnet werden! \n"
               "Bitte Gerät anschließen und beliebige Taste drücken...")

# Messung auswerten
print ("Am Tachymeter Registrierung auf R-R einstellen und")
print ("Messung am Gerät auslösen... \n")
while(True):
    if ser.inWaiting() >= 79:
        dataIn = ser.read(79).decode()
        # print ("Messung:", dataIn)
        P = dataIn[8:22]
        print ("Punktkennung:", P)
        T1 = dataIn[36:38]
        if T1 !="  ":
            W1 = float(dataIn[38:50])
            print (f"{T1} {W1:.3f}")
        else:
            T1 = "--"
            W1 = "---.----"
            print (T1, W1)
        T2 = dataIn[51:53]
        W2 = float(dataIn[53:66])
        print (f"{T2} {W2:.4f}")
        T3 = dataIn[67:69]
        W3 = float(dataIn[69:78])
        print (f"{T3} {W3:.4f}")

        messwerte = (P, T1, W1, T2, W2, T3, W3)
            
        # Messwerte in Datei schreiben
        try:
            datei = open("daten.txt", "a")
        except:
            print("Dateizugriff nicht erfolgreich!")
            sys.exit()
        datenzeile = [messwerte]
        datei.writelines(str(datenzeile) + "\n")
        # print ("Gespeicherte Datenzeile:", datenzeile)
        datei.close()
            
        print ("")
        print ("Messung am Gerät auslösen...")
    else:
        continue
