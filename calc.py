import sqlite3

# function to calculate points a player has scored from batting stats
def battingPoints(player):
    points = 0
    
    myCricket = sqlite3.connect('cricket.db')
    cricketCursor = myCricket.cursor()
    cricketCursor.execute("SELECT Faced FROM match WHERE Player=?;", (player,))
    balls = cricketCursor.fetchone()

    balls = float(balls[0])
    
    if balls == 0.0:
        return 0

    cricketCursor.execute("SELECT Scored FROM match WHERE Player=?;", (player,))
    runs = cricketCursor.fetchone()
    runs = int(runs[0])

    cricketCursor.execute("SELECT Fours FROM match WHERE Player=?;", (player,))
    fours = cricketCursor.fetchone()
    fours = int(fours[0])

    cricketCursor.execute("SELECT Sixes FROM match WHERE Player=?;", (player,))
    sixes = cricketCursor.fetchone()
    sixes = int(sixes[0])
    
    points = runs/2
    
    if runs >= 100:
        points = points + 15
    elif runs >= 50:
        points = points + 5

    if (runs/balls) > 1:
        points = points + 6
    elif (runs/balls) >= 0.8:
        points = points + 2
    
    points = points + fours
    points = points + 2 * sixes

    myCricket.close()

    return points

# function to calculate points a player has scored from bowling stats
def bowlingPoints(player):
    points = 0
    
    myCricket = sqlite3.connect('cricket.db')
    cricketCursor = myCricket.cursor()
    cricketCursor.execute("SELECT Bowled FROM match WHERE Player=?;", (player,))

    balls = cricketCursor.fetchone()
    
    balls = float(balls[0])
    
    if balls == 0.0:
        return 0

    overs = balls/6
    
    cricketCursor.execute("SELECT Wkts FROM match WHERE Player=?;", (player,))
    wkts = cricketCursor.fetchone()
    wkts = int(wkts[0])


    cricketCursor.execute("SELECT Given FROM match WHERE Player=?;", (player,))
    runs = cricketCursor.fetchone()
    runs = float(runs[0])

    points = points + 10.0*wkts

    if wkts >= 5:
        points = points + 15
    elif wkts >= 3:
        points = points + 5

    if (runs/overs) < 2:
        points = points + 10
    elif (runs/overs) < 3.5:
        points = points + 7
    elif (runs/overs) < 4.5:
        points = points + 4
    myCricket.close()


    return points

# function to calculate points a player has scored from fielding stats
def fieldingPoints(player):
    myCricket = sqlite3.connect('cricket.db')
    cricketCursor = myCricket.cursor()
    
    cricketCursor.execute("SELECT Catches FROM match WHERE Player=?;", (player,))
    catches = cricketCursor.fetchone()
    catches = int(catches[0])

    cricketCursor.execute("SELECT Stumping FROM match WHERE Player=?;", (player,))
    stumping = cricketCursor.fetchone()
    stumping = int(stumping[0])

    cricketCursor.execute("SELECT RO FROM match WHERE Player=?;", (player,))
    ro = cricketCursor.fetchone()
    ro = int(ro[0])

    points = 10* (catches + stumping + ro)
    myCricket.close()
    return points

def totalPoints(player):
    return (battingPoints(player) + bowlingPoints(player) + fieldingPoints(player))
