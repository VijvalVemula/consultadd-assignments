"""
5. Create a class 'Time' and initialize it with hours and minutes.
Create a method addTime() which should take two Time objects
and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
"""

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        total_hours = self.hours + other.hours + extra_hours
        final_minutes = total_minutes % 60
        return Time(total_hours, final_minutes)

    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        total_minutes = (self.hours * 60) + self.minutes
        print(f"Total minutes: {total_minutes}")

time1 = Time(int(input("Enter hours for time1: ")), int(input("Enter minutes for time1: ")))
time2 = Time(int(input("Enter hours for time2: ")), int(input("Enter minutes for time2: ")))

result = time1.addTime(time2)
print("Sum of Times:")
result.displayTime()
result.displayMinute()
