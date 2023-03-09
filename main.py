# This is a simple Python script.
import sqlite3
import initializeDB
import datetime

"""
TODO:
- ADD MISSING OPTIONS
- CREATE INDEXES

"""

# Print all cars and car locations
def printCars():
    print("Printing cars...")

    try:
        cur.execute('''
            SELECT
            Car.CarID, 
            Brand, 
            Model,
            Registeration_number, 
            Number_of_passangers,
            Locations.City
            FROM Car
            INNER JOIN Cars ON Cars.CarID = Car.CarID
            INNER JOIN Locations ON Locations.LocationID = Cars.LocationID;
            ''')
        results = cur.fetchall()
        for row in results:
            print(row)

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return

# Print all rental locations (TODO: Add list of cars.)
def printLocations():
    print("Printing rental locations...")

    try:
        cur.execute('''
            SELECT
            LocationID, 
            City,
            Address,
            Type
            FROM Locations;
            ''')
        results = cur.fetchall()
        for row in results:
            print(row)

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return

# Print all reservations
def printReservations():
    print("Printing reservations...")

    try:
        cur.execute('''
            SELECT
            Reservations.ReservationID,
            Customers.Firstname,
            Customers.Lastname,
            ReservationTime.Start_time,
            ReservationTime.End_time
            FROM Reservations
            INNER JOIN Customers ON Customers.CustomerID = Reservations.CustomerID
            INNER JOIN ReservationTime ON ReservationTime.ReservationID = Reservations.ReservationID
            ORDER BY ReservationTime.Start_time, Customers.Firstname, Customers.Lastname, ReservationTime.End_time;
            ''')
        
        results = cur.fetchall()
        for row in results:
            print(row)

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return

# Print all customers
def printCustomers():
    print("Printing all customers")

    try:
        cur.execute("SELECT * FROM Customers;")
        results = cur.fetchall()
        for row in results:
            print(row)

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return

# Print rental price
def rentalPrice():
    reservationID = input("Reservation ID: ")

    # Get times from ReservationTime-table
    try:
        cur.execute('''
                SELECT * FROM ReservationTime 
                WHERE reservationID = (?);
                ''', (reservationID, ))
        results = cur.fetchall()
        startTimeString = results[0][1]
        endTimeString = results[0][2]

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Calculate rental duration
    try:
        startTime = datetime.datetime.fromisoformat(startTimeString)
        endTime = datetime.datetime.fromisoformat(endTimeString)
        durationDays = (endTime - startTime).days + 1
        print(f"Your rental duration is {durationDays} days.")


    except sqlite3.Error as er:
        print("--- ERROR OCCURED WHILE CALCULATING RENTAL PRICE ---")
        print(er)

    # Get car id
    try:
        cur.execute('''
                SELECT CarID FROM Reservations 
                WHERE reservationID = (?);
                ''', (reservationID, ))
        results = cur.fetchall()
        carID = results[0][0]

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Get rental prices
    try:
        cur.execute('''
                SELECT * FROM Prices 
                WHERE CarID = (?);
                ''', (carID, ))
        results = cur.fetchall()
        Week_price = results[0][2]
        Day_price = results[0][3]

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    # Calculate rental price
    rentalCost = 0
    durationInfo = divmod(durationDays, 7)

    if durationInfo[1] == 0:
        rentalCost = Week_price * durationInfo[0]
    else:
        rentalCost = Day_price * durationDays

    print(f"Rental will cost: {rentalCost}€")

    return

# Test print functions (FOR TESTING)
def printX():
    print("Printing X")

    try:
        cur.execute("SELECT * FROM ReservationTime;")
        results = cur.fetchall()
        for row in results:
            print(row)

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return

# Search cars by brand and seats
def searchCar():
    carBrand = input("Car brand: ")
    carSeats = input("Number of seats: ")

    try:
        cur.execute('''
            SELECT
            Car.CarID, 
            Brand, 
            Model,
            Registeration_number, 
            Number_of_passangers,
            Locations.City
            FROM Car
            INNER JOIN Cars ON Cars.CarID = Car.CarID
            INNER JOIN Locations ON Locations.LocationID = Cars.LocationID
            WHERE Brand = (?) AND Number_of_passangers = (?);
            ''', (carBrand, carSeats,))
        
        results = cur.fetchall()
        if not results:
            print("\nNo matching cars. Try again changing search options...")
        else:
            for row in results:
                print(row)
    
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return

# Search reservations by customer name
def searchReservations():
    customerFirstName = input("Firstname: ")
    customerLastName = input("Lastname: ")

    try:
        cur.execute('''
            SELECT
            Reservations.ReservationID,
            Firstname,
            Lastname,
            Car.Brand,
            Car.Registeration_number
            FROM Reservations
            INNER JOIN Customers ON Customers.CustomerID = Reservations.CustomerID
            INNER JOIN ReservationTime ON ReservationTime.ReservationID = Reservations.ReservationID
            INNER JOIN Cars ON Cars.CarID = Reservations.CarID
            INNER JOIN Car on Car.CarID = Cars.CarID
            WHERE Firstname = (?) AND Lastname = (?);
            ''', (customerFirstName, customerLastName, ))
        
        results = cur.fetchall()
        if not results:
            print("\nNo matching reservations. Try again changing search options...")
        else:
            for row in results:
                print(row)

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return

# Add a new reservation
def makeReservation():
    # Declaring variables
    printCustomers()
    customerID = input("Your customer ID: ")
    printCars()
    carID = input("Rental car ID: ")
    rentalStartTime = input("Rental start date (DD.MM.YYYY): ")
    rentalEndTime = input("Rental end time (DD.MM.YYYY): ")

    # Add reservation to Reservations-table
    try:
        cur.execute('''
            INSERT INTO
            Reservations (customerID, carID)
            VALUES (?, ?);
        ''', (customerID, carID, ))

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    print("Latest ID: " + str(cur.lastrowid))

    # Add reservation times to ReservationTime-table
    try:
        # Parse time
        dbTimeStart = datetime.datetime.strptime(rentalStartTime, "%d.%m.%Y").astimezone().replace(hour=15, minute=00, microsecond=0).isoformat()
        dbTimeEnd = datetime.datetime.strptime(rentalEndTime, "%d.%m.%Y").astimezone().replace(hour=15, minute=00, microsecond=0).isoformat()

        # Insert into table
        cur.execute('''
            INSERT INTO
            ReservationTime
            VALUES(?, ?, ?);
        ''', (cur.lastrowid, dbTimeStart, dbTimeEnd, ))

        conn.commit()
        print(f"Reservation with ID {carID} added.")            # FIX THIS

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)
    
    return

# Delete reservation with user input ID
def deleteReservation():
    printReservations()
    reservationID = input("To be deleted ID: ")

    try:
        cur.execute('''
            DELETE FROM Reservations
            WHERE reservationID = (?);
        ''', (reservationID, ))

        conn.commit()
        print(f"Reservation with ID {reservationID} deleted.")
        
    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return


if __name__ == '__main__':
    # Declaring variables
    dbName = "test.sqlite"
    userInput = -1

    # Initialize database connection and cursor
    try:
        initializeDB.initializeDataBase(dbName)
        conn = sqlite3.connect(dbName)
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")

    except sqlite3.Error as er:
        print("--- ERROR OCCURED WHILE INITIALIZING DATABASE ---")
        print(er)
    
    # Main loop
    while (userInput != "0"):
        # Print selection
        print("\nMenu options:")
        print("1: Print Cars")                  # SELECT-query
        print("2: Print Locations")             # SELECT-query
        print("3: Print Reservations")          # SELECT-query
        print("4: Get rental price")            # CALCULATE rental price
        print("5: Search for cars")             # SELECT-query
        print("6: Search for reservation")      # SELECT-query
        print("7: Make reservation")            # INSERT VALUES reservation
        print("8: Delete reservation")          # DELETE reservation
        print("0: Quit")

        # Get user input
        userInput = input("What do you want to do? ")

        # Manage user input
        print(userInput)
        if userInput == "1":
            printCars()
        if userInput == "2":
            printLocations()
        if userInput == "3":
            printReservations()
        if userInput == "4":
            rentalPrice()
        if userInput == "5":
            searchCar()
        if userInput == "6":
            searchReservations()
        if userInput == "7":
            makeReservation()
        if userInput == "8":
            deleteReservation()
        if userInput == "0":
            print("Ending software...")

    # End program
    conn.close()

# EOF