import sqlite3
import time

def splitPlace(text):
    end = 1
    omraadearr = []
    omraadearr.append(text[0])
    text = text[1:]
    for i in range(len(text)):
        if text[i].isdigit() or text[i] == '':
            omraadearr.append(text[i])
            end = i
        else:
            return omraadearr, text[end+1:]
    return omraadearr, None  # Return None for the text part

stolID = 1
billettID = 1

with open("hovedscenen.txt", "r") as f:
    text = f.read()
    text = text.split("\n")
    date = text[0]
    date = date.split(" ")[1]
    text = text[1:]
    places = []
    while text:
        val1, text = splitPlace(text)
        if val1[-1:] == ['']:
            val1 = val1[0:len(val1)-1]
        if val1 is None:  # Check if an error occurred
            print("Error: No numbers found in the text or the text is not formatted correctly.")
            break
        places.append(val1)
    con = sqlite3.connect("teater.db")
    cur = con.cursor()
    stolNr = 0
    places = places[::-1]
    for item in places:
        sted = item[0]
        if(sted == 'Galleri'):
            stolID = 505
        item = item[1:]
        item = item[::-1]
        for rad in item:
            for char in rad:
                stolNr +=1
                if(char == 'x'):
                    continue
                elif(char == '0'):
                    stolID += 1
                elif(char == '1'):
                    billettID += 1
                    forestilling = cur.execute("SELECT * FROM Forestilling WHERE Dato = ? AND TeaterSalID = ?", (date,1)).fetchone()
                    cur.execute("INSERT INTO Billett (BillettNummer, KundeType, Pris, Dato, ForestillingID, StolID) VALUES (?, ?, ?, ?, ?, ?)", (billettID,'Ordinær',450, date, 3, stolID))
                    cur.execute("INSERT INTO KjoptBillett (Kundenummer, BillettNummer) VALUES (?, ?)", (1, billettID))
                    con.commit()
                    stolID += 1    
    con.close()


with open("gamle-scene.txt", "r") as f:
    text = f.read()
    text = text.split("\n")
    date = text[0]
    date = date.split(" ")[1]
    text = text[1:]
    places = []
    while text:
        val1, text = splitPlace(text)
        if val1[-1:] == ['']:
            val1 = val1[0:len(val1)-1]
        if val1 is None:  # Check if an error occurred
            print("Error: No numbers found in the text or the text is not formatted correctly.")
            break
        places.append(val1)
    con = sqlite3.connect("teater.db")
    cur = con.cursor()
    stolNr = 0
    places = places[::-1]
    for item in places:
        sted = item[0]
        item = item[1:]
        item = item[::-1]
        for rad in item:
            stolNr = 0
            for char in rad:
                stolNr +=1
                if(char == 'x'):
                    continue
                elif(char == '0'):
                    stolID += 1
                elif(char == '1'):
                    billettID += 1
                    forestilling = cur.execute("SELECT * FROM Forestilling WHERE Dato = ? AND TeaterSalID = ?", (date,2)).fetchone()
                    cur.execute("INSERT INTO Billett (BillettNummer, KundeType, Pris, Dato, ForestillingID, StolID) VALUES (?, ?, ?, ?, ?, ?)", (billettID,'Ordinær',450, date, 6,stolID))
                    cur.execute("INSERT INTO KjoptBillett (Kundenummer, BillettNummer) VALUES (?, ?)", (1, billettID))
                    con.commit()
                    stolID += 1    
    con.close()