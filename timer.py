import time
import datetime

def convertMinutesToSeconds(time_str):
    parts = list(map(int, time_str.split(':')))
    if len(parts) == 3: #HH:MM:SS
        h, m, s = parts
        return int(h) * 3600 + int(m) * 60 + int(s)
    elif len(parts) == 2: #MM:SS
        m, s = parts
        return m * 60 + s
    elif len(parts) == 1: #SS
        return parts[0]
    else:
        raise ValueError("Invalid time format. Use HH:MM:SS, MM:SS, or SS.")


print(convertMinutesToSeconds("2:20"))

timeInSeconds = convertMinutesToSeconds("0:20")

def countdown(TimeFromUser):
    while TimeFromUser:
        mins, secs = divmod(TimeFromUser, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timer}', end='', flush=True)
        time.sleep(1)
        TimeFromUser -= 1
    print("\nTime to get up now")



countdown(timeInSeconds)