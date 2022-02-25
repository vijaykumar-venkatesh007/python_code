# ROCK PAPER AND SCISSORS
X, Y = map(str,input().split())
if (X == "R" and Y == "P") or (X == "P" and Y == "R"):
    print("P")
elif (X == "R" and Y == "S") or (X == "S" and Y == "R"):
    print("R")
elif (X == "P" and Y == "S") or (X == "S" and Y == "P"):
    print("S")
elif (X == "R" and Y == "R"):
    print("D")
elif X == "S" and Y == "S":
    print("D")
elif X == "P" and Y == "P":
    print("D")