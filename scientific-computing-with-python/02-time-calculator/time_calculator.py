def convert_to_minutes(h,m):
    offset_minutes = h*60 + m
    return offset_minutes

def add_time(start, duration, day=""):
    start_h = int(start.split(":")[0])
    start_m = int(start.split(":")[1].split(" ")[0])
    start_fmt = start[-2:]
    
    duration_h, duration_m = map(int, duration.split(":"))

    days = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    
    if start_fmt == "PM":
        start_h += 12

    # convert to minutes
    start_tot_mins = convert_to_minutes(start_h,start_m)
    duration_tot_mins = convert_to_minutes(duration_h,duration_m)

    offset = start_tot_mins + duration_tot_mins

    m = offset % 60
    h = ( offset % 720 ) // 60
    if h == 0:
        h = 12
    fmt_ = (offset // 720) % 2
            # 720 mins in half day, even for AM, odd for PM


    if fmt_ == 0:
        fmt = "AM"
    else:
        fmt = "PM"

    num_day_later = offset // 1440

    new_day_ = ""
    if day != "":
        day_index = days.index(day.title())
        new_day_index = (day_index + num_day_later) % 7
        new_day = days[new_day_index]
        new_day_ = f", {new_day}" 

    if num_day_later > 1:
        new_time = f"{h}:{m:02d} {fmt}{new_day_} ({num_day_later} days later)"
    elif num_day_later == 1:
                new_time = f"{h}:{m:02d} {fmt}{new_day_} (next day)"
    else:
        new_time = f"{h}:{m:02d} {fmt}{new_day_}"

    return new_time

