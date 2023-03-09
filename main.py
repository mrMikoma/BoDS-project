# This is a simple Python script.
import sqlite3
import initializeDB

"""
TODO:
- ADD MISSING OPTIONS
- CREATE INDEX

"""

# Print all cars and car locations
def printCars():
    print("Printing cars...")

    try:
        cur.execute('''
            SELECT
            Car.CarID, 
            Brand AS "Car Brand", 
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
        cur.execute("SELECT * FROM Reservations;")
        results = cur.fetchall()
        for row in results:
            print(row)

    except sqlite3.Error as er:
        print("--- ERROR OCCURED ---")
        print(er)

    return

# Test print functions (FOR TESTING)
def printX():
    print("Printing X")

    try:
        cur.execute("SELECT * FROM Reservations;")
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
            Reservations.CarID
            FROM Reservations
            INNER JOIN Customers ON Customers.CustomerID = Reservations.CustomerID
            INNER JOIN ReservationTime ON ReservationTime.ReservationID = Reservations.ReservationID
            INNER JOIN Cars ON Cars.CarID = Reservations.CarID
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
    asd = input("What is the matchID of the match you want to move? ")

    try:
        print("aha") # DEBUG

        #cur.execute('''

        #''', (asd, ))

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
    db_name = "test.sqlite"
    userInput = -1

    # Initialize database connection and cursor
    try:
        initializeDB.initializeDataBase(db_name)
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
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
        print("4: Print -")                     # -
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
            printX()
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
