import time
import datetime
import asyncio
import threading
#from desktop_notifier import DesktopNotifier, Button

#notifier = DesktopNotifier()

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

async def countdown(seconds):
    print("timer started")
    remaining = seconds
    while remaining:
        mins, seconds = divmod(remaining, 60)
        print(f"{mins:02d}:{seconds:02d}")
        await asyncio.sleep(1)
        remaining -= 1
    print("\n[NOTIFY] Time to get up!")
#print(convertMinutesToSeconds("2:20"))




