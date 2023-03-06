
import sqlite3
from sqlite3 import Error
import os.path


def createTables(conn, cur):
    print("...Creating tables.")

    # Cars -table
    cur.execute('''
        CREATE TABLE "Cars" (
        "CarID"	INTEGER NOT NULL,
        "Registeration_number"	TEXT,
        "Brand"	TEXT,
        "Model"	TEXT,
        "Number_of_passangers"	INTEGER,
        PRIMARY KEY("CarID" AUTOINCREMENT))
          ''')
    
    # Customers -table
    cur.execute('''
        CREATE TABLE "Customers" (
        "CustomerID"	INTEGER NOT NULL,
        "Firstname"	TEXT,
        "Lastname"	TEXT,
        "Address"	TEXT,
        PRIMARY KEY("CustomerID" AUTOINCREMENT))
          ''')
    # Locations -table
    cur.execute('''
        CREATE TABLE "Locations" (
        "LocationID"	INTEGER NOT NULL,
        "Address"	TEXT,
        "Type"	TEXT,
        PRIMARY KEY("LocationID" AUTOINCREMENT))
          ''')
    # Prices -table
    cur.execute('''
        CREATE TABLE "Prices" (
        "PriceID"	INTEGER NOT NULL,
        "CarID"	INTEGER,
        "Week_price"	INTEGER,
        "Day_price"	INTEGER,
        PRIMARY KEY("PriceID" AUTOINCREMENT))
          ''')
    # Reservation -table
    cur.execute('''
        CREATE TABLE "Reservation" (
        "ReservationID"	INTEGER NOT NULL,
        "PriceID"	INTEGER,
        "Start_time"	TEXT,
        "End_time"	TEXT,
        PRIMARY KEY("ReservationID" AUTOINCREMENT))
          ''')
    # Reservations -table
    cur.execute('''
        CREATE TABLE "Reservations" (
        "ReservationID"	INTEGER NOT NULL,
        "CustomerID"	INTEGER,
        "CarID"	INTEGER,
        "LocationID"	INTEGER)
           ''')

    conn.commit()
    return

def addDefaultValues(conn, cur):
    print("...Adding default values.")

    # Cars -values
    cur.execute('''
        INSERT INTO Cars (Registeration_number, Brand, Model, Number_of_passangers) VALUES 
        ("ASD-123", "BMw", "M5", 5),
        ("FSD-642", "Volvo", "V40", 5),
        ("YJV-878", "Saab", "93", 5),
        ("FDH-113", "Volvo", "XC60", 5),
        ("HFG-534", "Mazda", "MX-5", 2),
        ("HDW-533", "Chervolet", "Corvette C8", 2)
        ''')

    # Customers -values
    cur.execute('''
        INSERT INTO Customers (Firstname, Lastname, Address) VALUES 
        ("Taneli",	"Mäkelä", "Tietyö 6, Lappeenranta"),
        ("Pirkko",	"Leppänen",	"Asemakatu 67, Pirkkala"),
        ("Jonne",	"Eeeäss",	"Ammattikoulunkatu 69, Imatra"),
        ("Veeti",	"Tarppinen",	"Nörttikatu 7, Lappeenranta"),
        ("Anne",	"Välimäki",	"Mikonkatu 1, Helsinki"),
        ("Jesper",	"Pulunen",	"Lintutornintie 668, Simpele")
        ''')

    
    # Locations -values
    cur.execute('''
        INSERT INTO Locations (Address, Type) VALUES 
        ("Tietyö 60, Lappeenranta", "Store"),
        ("Asemakatu 6, Pirkkala", "Self-service"),
        ("Ammattikoulunkatu 6, Imatra", "Store"),
        ("Nörttikatu 100101100, Lappeenranta", "Self-service"),
        ("Mikonkatu 32, Helsinki", "Store"),
        ("Mannerheiminkatu 101, Helsinki", "Store"),
        ("Lintutornintie 423, Simpele", "Self-service")
        ''')

    """
    # Prices -values
    cur.execute('''
        INSERT INTO Prices () VALUES 
        (),

        ''')
    # Reservation -values
    cur.execute('''
        INSERT INTO Reservation () VALUES 
        (),

        ''')
    # Reservations -values
    cur.execute('''
        INSERT INTO Reservations () VALUES 
        (),

        ''')
    """

    conn.commit()
    return

def initializeDataBase(dbName):
    print("Initializing database...")

    # Check if database already exists
    if os.path.exists(dbName):
        print("Database already exists.")

    else:
        conn = sqlite3.connect(dbName) 
        cur = conn.cursor()
        createTables(conn, cur)
        addDefaultValues(conn, cur)
        conn.close()

    print("Initiation completed successfully.")
    return


# For testing purposes only
if __name__ == '__main__':
    print("yea boi")
    #dbName = "test.sqlite"
    #initializeDataBase(dbName)

# EOF