SELECT F.ForestillingID, TS.StykkeNavn, F.Dato, COUNT(BillettNummer) AS Solgt FROM Forestilling AS F
INNER JOIN StykkeiSal ON StykkeiSal.TeaterSalID = F.TeaterSalID
INNER JOIN Teaterstykke AS TS ON TS.StykkeID = StykkeiSal.StykkeID
LEFT JOIN Billett AS B ON B.ForestillingID = F.ForestillingID
GROUP BY F.ForestillingID
ORDER BY COUNT(BillettNummer) DESC;