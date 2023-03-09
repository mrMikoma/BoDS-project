
import sqlite3
import os.path


def createTables(conn, cur):
    print("...Creating tables.")

    # Enabling foreign keys
    cur.execute('''PRAGMA foreign_keys = ON;''')

    # Car -table
    try:
        cur.execute('''
            CREATE TABLE "Car" (
            "CarID"	INTEGER NOT NULL,
            "Registeration_number" TEXT UNIQUE,
            "Brand"	TEXT,
            "Model"	TEXT,
            "Number_of_passangers" INTEGER,
            PRIMARY KEY("CarID" AUTOINCREMENT))
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Customers -table
    try:
        cur.execute('''
            CREATE TABLE "Customers" (
            "CustomerID" INTEGER NOT NULL UNIQUE,
            "Firstname" TEXT,
            "Lastname" TEXT,
            "Phone"	TEXT,
            PRIMARY KEY("CustomerID" AUTOINCREMENT))
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Locations -table
    try:
        cur.execute('''
            CREATE TABLE "Locations" (
            "LocationID" INTEGER NOT NULL,
            "City" TEXT,
            "Address" TEXT,
            "Type" TEXT,
            PRIMARY KEY("LocationID" AUTOINCREMENT))
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)
    
    # Prices -table
    try:
        cur.execute('''
            CREATE TABLE "Prices" (
            "PriceID" INTEGER NOT NULL,
            "CarID" INTEGER,
            "Week_price" INTEGER,
            "Day_price"	INTEGER,
            PRIMARY KEY("PriceID" AUTOINCREMENT),
            FOREIGN KEY("CarID") REFERENCES "Car" ("CarID"))
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Cars -table
    try:
        cur.execute('''
            CREATE TABLE "Cars" (
            "CarID"	INTEGER,
            "LocationID" INTEGER,
            FOREIGN KEY("CarID") REFERENCES "Car" ("CarID"),
            FOREIGN KEY("LocationID") REFERENCES "Locations" ("LocationID"))
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)      
 
    # Reservations -table
    try:
        cur.execute('''
            CREATE TABLE "Reservations" (
            "ReservationID"	INTEGER NOT NULL UNIQUE,
            "CustomerID"	INTEGER,
            "CarID"	INTEGER,
            PRIMARY KEY("ReservationID" AUTOINCREMENT))
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # ReservationTime -table
    try:
        cur.execute('''
            CREATE TABLE "ReservationTime" (
            "ReservationID"	INTEGER NOT NULL,
            "Start_time"	TEXT,
            "End_time"	TEXT,
            FOREIGN KEY("ReservationID") 
            REFERENCES Reservations ("ReservationID")
            ON UPDATE CASCADE
            ON DELETE CASCADE)
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    conn.commit()
    return

def addDefaultValues(conn, cur):
    print("...Adding default values.")

    # Car -values
    try:
        cur.execute('''
            INSERT INTO Car (Registeration_number, Brand, Model, Number_of_passangers) VALUES 
            ("ASD-123", "Bmw", "M5", 5),
            ("FSD-642", "Volvo", "V40", 5),
            ("YJV-878", "Saab", "93", 5),
            ("FDH-113", "Volvo", "XC60", 5),
            ("HFG-534", "Mazda", "MX-5", 2),
            ("HDW-533", "Chervolet", "Corvette C8", 2)
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Customers -values
    try:
        cur.execute('''
            INSERT INTO Customers (Firstname, Lastname, Phone) VALUES 
            ("Taneli",	"Mäkelä", "+358 45 73966153"),
            ("Pirkko",	"Leppänen",	"+358 50 43593422"),
            ("Jonne",	"Eeeäss",	"+358 50 27571484"),
            ("Veeti",	"Tarppinen", "+358 49 46873673"),
            ("Anne",	"Välimäki",	"+358 49 46077948"),
            ("Jesper",	"Pulunen",	"+358 49 466354")
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Locations -values
    try:
        cur.execute('''
            INSERT INTO Locations (Address, City, Type) VALUES 
            ("Tietyö 60", "Lappeenranta", "Store"),
            ("Asemakatu 6", "Pirkkala", "Self-service"),
            ("Ammattikoulunkatu 6", "Imatra", "Store"),
            ("Nörttikatu 100101100", "Lappeenranta", "Self-service"),
            ("Mikonkatu 32", "Helsinki", "Store"),
            ("Mannerheiminkatu 101", "Helsinki", "Store"),
            ("Lintutornintie 423", "Simpele", "Self-service")
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Prices -values
    try:
        cur.execute('''
            INSERT INTO Prices (CarID, Week_price, Day_price) VALUES 
            (1, 1000, 140),
            (2, 600, 100),
            (3, 490, 80),
            (4, 500, 90),
            (5, 1250, 160),
            (6, 800, 90)
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Cars -values
    try:
        cur.execute('''
            INSERT INTO Cars (CarID, LocationID) VALUES 
            (1, 2),
            (2, 4),
            (3, 6),
            (4, 3),
            (5, 3),
            (6, 3)
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Reservations -values
    try:
        cur.execute('''
            INSERT INTO Reservations (CustomerID, CarID) VALUES 
            (1, 1),
            (2, 5),
            (3, 6),
            (4, 3),
            (5, 4),
            (6, 3)
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # ReservationTime -values
    try:
        cur.execute('''
            INSERT INTO ReservationTime (ReservationID, Start_time, End_time) VALUES 
            (1, "2023-03-06T15:00:00+02:00", "2023-03-07T12:00:00+02:00"),
            (2, "2023-03-06T15:00:00+02:00", "2023-03-09T12:00:00+02:00"),
            (3, "2023-03-06T15:00:00+02:00", "2023-03-012T12:00:00+02:00"),
            (4, "2023-03-06T15:00:00+02:00", "2023-03-12T12:00:00+02:00"),
            (5, "2023-03-13T15:00:00+02:00", "2023-03-14T12:00:00+02:00"),
            (6, "2023-03-14T15:00:00+02:00", "2023-03-21T12:00:00+02:00")
            ''')
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)
    
    conn.commit()
    return

def initializeDataBase(dbName):
    print("Initializing database...")

    # Check if database already exists
    if os.path.exists(dbName):
        print("Database already exists.")

    # Create new data base if not existing already
    else:
        conn = sqlite3.connect(dbName) 
        cur = conn.cursor()
        createTables(conn, cur)
        addDefaultValues(conn, cur)
        conn.close()

    print("Initiation completed.")
    return


# For testing purposes only
if __name__ == '__main__':
    print("yea boi")
    dbName = "test2.sqlite"
    initializeDataBase(dbName)

# EOF