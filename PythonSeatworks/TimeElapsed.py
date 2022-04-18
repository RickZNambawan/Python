hours = int(input("Enter Hour/s: "))
if hours < 0 or hours > 24:
    print("Invalid Hour.")
else:
    minutes = int(input("Enter Minute/s: "))
    if minutes < 0 or minutes > 60:
        print("Invalid Minute.")
    else:
        seconds = int(input("Enter Second/s: "))
        if seconds < 0 or seconds > 60:
            print("Invalid Second.")
        else:
            timeElapsedInSeconds = (hours * 3600) + (minutes * 60) + seconds
            print("Time Elapsed In Seconds: {:,}".format(timeElapsedInSeconds))