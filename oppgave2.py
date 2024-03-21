import sqlite3

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

with open("gamle-scene.txt", "r") as f:
    text = f.read()
    text = text.split("\n")
    date = text[0]
    if date.isalpha() == False:
        ValueError("The date is not formatted correctly.")
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
    for i in range(len(places)):
        cur.execute('''UPDATE ''')
