# This is a simple Python script.
import sqlite3
import initializeDB

"""
TODO:
- 

"""


def printCars():
    print("Printing cars")

    cur.execute('''SELECT 
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

    return


def printLocations():
    print("Printing rental locations")

    cur.execute("SELECT * FROM Locations;")
    results = cur.fetchall()
    for row in results:
        print(row)

    return


def printX():
    print("Printing X")

    cur.execute("SELECT * FROM Reservation;")
    results = cur.fetchall()
    for row in results:
        print(row)

    return


def searchPlayer():
    playerName = input("What is the player's surname? ")
    """ 
    Insert the correct Python and SQL commands to find the player 
    using the given surname
    """
    # Start your modifications after this comment
    # You are given the print statements, now you need to add the fetched data to the five prints.

    print("ID:")
    print("First name:")
    print("Last name:")
    print("Birthdate: ")
    print("Nationality:")

    return


def moveMatch():
    matchID = input("What is the matchID of the match you want to move? ")
    newMatchDate = input("What is the new matchdate you want to set?")

    """ 
    Using the correct Python and SQL comands:
    Change the match date based on the given matchID and new matchdate
    IF a new matchdate is set to NULL, set the winner and result to NULL as well
    """
    # Start your modifications after this comment

    return


def deletePlayer():
    playerID = input("What is the player's PlayerID? ")
    """ 
    Using the correct Python and SQL comands:
    Delete the Player and his Ranking information
    Additionally, set the playerid to NULL in ALL match-data it is found
    """
    # Start your modifications after this comment


if __name__ == '__main__':
    # Declaring variables
    db_name = "test.sqlite"
    userInput = -1

    # Initialize database connection and cursor
    initializeDB.initializeDataBase(db_name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    
    # Main loop
    while (userInput != "0"):
        # Print selection
        print("\nMenu options:")
        print("1: Print Cars")
        print("2: Print Locations")
        print("3: Print -")
        print("4: Print -")
        print("5: Print -")
        print("6: Search for ")
        print("7: Make -")
        print("8: Delete -")
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
            printX()
        if userInput == "4":
            printX()
        if userInput == "5":
            printX()
        if userInput == "6":
            searchPlayer()
        if userInput == "7":
            moveMatch()
        if userInput == "8":
            deletePlayer()
        if userInput == "0":
            print("Ending software...")

    # End program
    conn.close()

# EOF
