def timeConversion(time):
    h, m, s = time.split(":")
    ampm = s[-2:]
    s = s.replace(ampm, '')

    h, m, s = map(int, (h, m, s))
    
    if ampm == "PM" and int(h) < 12:
        h = int(h) + 12
    elif ampm == "AM" and int(h) >= 12:
        h = 0
    else: 
        pass

    time_return = f"{h:02d}:{m:02d}:{s:02d}"
    
    return time_return

time = "12:40:22AM"

print(timeConversion(time))