import sqlite3


conn = sqlite3.connect('teater.db')


c = conn.cursor()

kundetype = "Adult"
dato = "2024-02-03"

def buying_tickets():

