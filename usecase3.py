import sqlite3

#forestillingen 3 februar
#en rad med 9 ledige seter, trenger ikke å være vedsiden av hverandre.

#finne denne raden. summere prisen

#SELECT * FROM Stol 

#SELECT * FROM Stol INNER JOIN Teatersal ON Teatersal.TeaterSalID = Stol.TeaterSalID WHERE Stol.TeaterSalID = 2;
# the query above to select all stol from gamle scene.

#SELECT * FROM Forestilling WHERE Forestilling.Dato = '2024-02-03' AND Forestilling.TeaterSalID = 2;
# the query to select forestilling from 2024-02-03. 3rd february.

# each ordinær is 350
# they are 9 so they don't get the bundle

# SELECT S.RadNr, S.Omraadet, COUNT(*) AS VacantSeats FROM Stol AS S
# LEFT JOIN Billett AS B ON S.StolID = B.StolID AND B.ForestillingID = 6
# WHERE B.BillettNummer IS NULL
# GROUP BY S.RadNr, S.Omraadet
# HAVING COUNT(*) >= 9;


# Dynamiske properties her: Forestilling ID og Count.

# show_id is the ForestillingID for a certain Show.
# vacant_amount is the amount of requested vacant seats.

def checkForVacantSeatsInRow(show_id, vacant_amount, ordi_am, honn_am, stud_am, child_am):
    prices = {
        "ordinary": 350,
        "honnor": 300,
        "student": 220,
        "child": 220
    }

    if (ordi_am + honn_am + stud_am + child_am > vacant_amount):
        print("There are more customers than requested vacant seats.") 
        return
    if (ordi_am >= 10):
        prices["ordinary"] = 320
    
    if (honn_am >= 10):
        prices["honnor"] = 270

    price = prices["ordinary"] * ordi_am + prices["honnor"] * honn_am + prices["student"] * stud_am + prices["child"] * child_am

    cursor = conn.cursor()

    query = f"SELECT S.RadNr, S.Omraadet, COUNT(*) AS VacantSeats FROM Stol AS S LEFT JOIN Billett AS B ON S.StolID = B.StolID AND B.ForestillingID = {show_id} WHERE B.BillettNummer IS NULL GROUP BY S.RadNr, S.Omraadet HAVING COUNT(*) >= {vacant_amount};"

    cursor.execute(query)

    row = cursor.fetchone()

    if row:
        return price
    else:
        return "There are no vacant seats"
    

conn = sqlite3.connect('testdb.db')

print(checkForVacantSeatsInRow(6, 9, 9, 0, 0, 0))

conn.close()