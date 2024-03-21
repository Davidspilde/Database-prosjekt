import sqlite3
# Dynamiske properties her: ForestillingID og Count.
# the function below takes in requested vacant amount
# and it also takes in the types of customers
# if the sum of these customers exceed the vacant amount
# it will not execute
# else it tests.


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
    

conn = sqlite3.connect('teater.db')

print(checkForVacantSeatsInRow(6, 9, 9, 0, 0, 0),"kr")

conn.close()