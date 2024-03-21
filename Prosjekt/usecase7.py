import sqlite3

conn = sqlite3.connect('teater.db')

actor = input('Skriv inn et skuespiller navn (fornavn og etternavn): ')

cursor = conn.cursor()

query = (
    "SELECT " +
    "S1.Navn AS Specific_Actor_Name, " +
    "S2.Navn AS Second_Actor_Name, " +
    "TS.StykkeNavn " +
    "FROM Skuespiller AS S1 " +
    "INNER JOIN SkuespilleriRolle AS SiR1 ON SiR1.SkuespillerID = S1.SkuespillerID " +
    "INNER JOIN RolleiAkt AS RA1 ON RA1.RolleID = SiR1.RolleID " +
    "INNER JOIN Akt AS A ON RA1.AktID = A.AktID " +
    "INNER JOIN RolleiAkt AS RA2 ON RA2.AktID = A.AktID " +
    "INNER JOIN SkuespilleriRolle AS SiR2 ON SiR2.RolleID = RA2.RolleID " +
    "INNER JOIN Skuespiller AS S2 ON S2.SkuespillerID = SiR2.SkuespillerID AND NOT S1.SkuespillerID = S2.SkuespillerID " +
    "INNER JOIN Teaterstykke AS TS ON TS.StykkeID = A.StykkeID " +
    f"WHERE S1.Navn = '{actor}' " +
    "GROUP BY S1.Navn, S2.Navn;"
)

cursor.execute(query)

rows = cursor.fetchall()

if (len(rows) != 0):
    print("FørstesNavn|AndresNavn|Teaterstykke")
    for row in rows:
        print(row)
else:
    print("No such actor found")