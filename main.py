# This is a sample Python script.
import sqlite3


# Connecting to the DB and creating a cursor
db_name = "RentalDB.db"
dbsql_name = "RentalDB.sqlite"
db = sqlite3.connect(db_name)
cur = db.cursor()

def initializeDB():
    try:
        f = open(dbsql_name, "r")
        commandstring = ""
        for line in f.readlines():
            commandstring += line
        cur.executescript(commandstring)
    except sqlite3.OperationalError:
        print("Database exists, skip initialization")
    except:
        print("No SQL file to be used for initialization")


def printPlayers():
    print("Printing players")
    """
    Insert the correct Python and SQL commands
    to print all players
    """
    # Start your modifications after this comment
    # You should print the data noe row at a time.

    return


def printRanking():
    print("Printing ranking")
    """
    Insert the correct Python and SQL commands 
    to print all ranking information
    """
    # Start your modifications after this comment
    # You should print the data noe row at a time.

    return


def printMatches():
    print("Printing matches")
    """ 
    Insert the correct Python and SQL commands 
    to print all ranking information
    """
    # Start your modifications after this comment
    # You should print the data one row at a time.

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
    initializeDB()
    userInput = -1
    while (userInput != "0"):
        print("\nMenu options:")
        print("1: Print Players")
        print("2: Print Ranking")
        print("3: Print Matches")
        print("4: Search for one player")
        print("5: Move matchdate")
        print("6: Delete player")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            printPlayers()
        if userInput == "2":
            printRanking()
        if userInput == "3":
            printMatches()
        if userInput == "4":
            searchPlayer()
        if userInput == "5":
            moveMatch()
        if userInput == "6":
            deletePlayer()
        if userInput == "0":
            print("Ending software...")
    db.close()

# EOF
