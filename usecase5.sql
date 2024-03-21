SELECT TS.StykkeNavn, Skues.Navn, Rolle.RolleNavn FROM Skuespiller AS Skues
INNER JOIN SkuespilleriRolle AS SiR ON SiR.SkuespillerID = Skues.SkuespillerID
INNER JOIN Rolle ON Rolle.RolleID = SiR.RolleID
INNER JOIN RolleIAkt AS RiA ON RiA.RolleID = SiR.RolleID
INNER JOIN Akt ON Akt.AktID = RiA.AktID
INNER JOIN Teaterstykke AS TS ON TS.StykkeID = Akt.StykkeID
GROUP BY Skues.Navn, Rolle.RolleNavn;