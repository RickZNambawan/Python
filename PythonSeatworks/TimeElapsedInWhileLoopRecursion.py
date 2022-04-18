print("\n \t \t(Program: Time Elapsed)")


class Time:
    def __init__(self):
        self.hour(), self.minute(), self.second()

    def hour(self):
        self.hours = int(input("\nEnter Hours: "))
        if self.hours < 0 or self.hours > 24:
            print("Invalid Hour.")
            self.hour()

    def minute(self):
        try:
            self.minutes = int(input("Enter Minutes: "))
            if self.minutes < 0 or self.minutes > 60:
                print("Invalid Minute.")
                self.minute()
        except:
            print("Invalid Input!")
            self.minute()

    def second(self):
        try:
            self.seconds = int(input("Enter Seconds: "))
            if self.seconds < 0 or self.seconds > 60:
                print("Invalid Second.")
                self.second()
        except:
            print("Invalid Input")


timeElapsed = Time()
timeElapsedInSeconds = (timeElapsed.hours * 3600) + (timeElapsed.minutes * 60) + timeElapsed.seconds
print("\nTime Elapsed in Seconds: {:,}".format(timeElapsedInSeconds))


# hours = int(input("Enter Hour: "))
# if hours < 0 or hours > 24:
#     print("Invalid Hour.")
# else:
#     minutes = int(input("Enter Minute: "))
#     if minutes > 0 or minutes < 60:
#         print("Invalid Minute.")
#     else:
#         seconds = int(input("Enter Second: "))
#         if seconds < 0 or seconds > 60:
#                 print("Invalid Second.")
#         else:
#             timeElapsedInSecondss = (hours * 3600) + (minutes * 60) + seconds
#             print("Time Elapsed In Seconds: {:,}".format(timeElapsedInSecondss))
