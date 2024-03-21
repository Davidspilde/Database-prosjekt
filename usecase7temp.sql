-- SELECT S1.SkuespilleriD AS Førstskuespiller, S1.Navn AS FørsteNavn, 
-- S2.SkuespillerID AS Andreskuespiller, S2.Navn as AndreNavn FROM Skuespiller AS S1
-- INNER JOIN SkuespilleriRolle AS SiR1 ON SiR1

-- S2.SkuespillerID AS Collaborating_Actor_ID,
-- S2.Navn AS Collaborating_Actor_Name,
-- TS.StykkeNavn

SELECT
S1.Navn AS Specific_Actor_Name,
S2.Navn AS Second_Actor_Name,
TS.StykkeNavn
FROM Skuespiller AS S1
INNER JOIN SkuespilleriRolle AS SiR1 ON SiR1.SkuespillerID = S1.SkuespillerID
INNER JOIN RolleiAkt AS RA1 ON RA1.RolleID = SiR1.RolleID
INNER JOIN Akt AS A ON RA1.AktID = A.AktID
INNER JOIN RolleiAkt AS RA2 ON RA2.AktID = A.AktID
INNER JOIN SkuespilleriRolle AS SiR2 ON SiR2.RolleID = RA2.RolleID
INNER JOIN Skuespiller AS S2 ON S2.SkuespillerID = SiR2.SkuespillerID AND NOT S1.SkuespillerID = S2.SkuespillerID
INNER JOIN Teaterstykke AS TS ON TS.StykkeID = A.StykkeID
WHERE S1.SkuespillerID = 1
GROUP BY S1.Navn, S2.Navn;
