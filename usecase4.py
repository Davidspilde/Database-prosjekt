import sqlite3

date = input("Format (yyyy-mm-dd): ")

conn = sqlite3.connect('testdb.db')
cursor = conn.cursor()

query = ("SELECT F.ForestillingID, F.Dato, Teaterstykke.StykkeNavn, COUNT(B.BillettNummer) AS BilletterSolgt FROM Forestilling AS F " +
        "LEFT JOIN Billett AS B ON F.ForestillingID = B.ForestillingID " +
        "INNER JOIN StykkeISal ON F.TeaterSalID = StykkeISal.TeaterSalID " +
        "INNER JOIN Teaterstykke ON StykkeISal.StykkeID = Teaterstykke.StykkeID " +
        f"WHERE F.Dato = '{date}' " +
        "GROUP BY F.ForestillingID;")
cursor.execute(query)

rows = cursor.fetchall()

if (len(rows) != 0):
    print("(ForestillingID|Dato|StykkeNavn|BilletterSolgt)")
    for row in rows:
        print(row)
else:
    print("No shows found")
conn.close()