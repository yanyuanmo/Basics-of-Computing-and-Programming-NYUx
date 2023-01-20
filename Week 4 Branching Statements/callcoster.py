day_to_int = {"Mon": 1, "Tue": 2, "Wed": 3, "Thr": 4, "Fri": 5, "Sat": 6, "Sun": 7}

day = day_to_int[input("Enter the day the call started at: ")]
time = int(input("Enter the time the call started at (hhmm): "))
duration = float(input("Enter the duration of the call (in minutes): "))
if day in [1, 2, 3, 4, 5]:
    if time >= 800 and time <= 1800:
        cost = 0.4*duration
    else:
        cost = 0.25*duration
else:
    cost = 0.15*duration
print("This call will cost ${:.2f}".format(cost))
