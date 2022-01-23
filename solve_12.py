"""
    Healthy  Programmer
    Work timing : 9 AM -5 PM
    Activity :
        1. Drink Water - Water.mp3 - Plays after some time and user needs to drink 250 ml of water and log it using
            DRANK keyword
        2. Eyes - eyes.mp3 - Plays after every 30 min time and user needs to enter EyDone and log it
        3. Physical Activity - physical.mp3 - Plays after every 45 min and user needs to enter ExDone and log it
    Rules :
        Need to use pygame library
"""


def capture_time():
    HH, MM = map(int, input("Enter time in HH:MM format").split(":"))
    return HH * 60 + MM


if __name__ == '__main__':
    import time as t
    import pygame as pg
    import datetime as dt

    print(" ***** Welcome to Healthy Programmer *****")
    # Taking input from the user and then storing calculating work hours
    print("Enter work Start time in 24-Hour %H:%M ")
    w_start_time = capture_time()
    print("Enter work End time in 24-Hour Format : ")
    w_end_time = capture_time()
    w_h_time = w_end_time - w_start_time
    total_water_intake_expected = int(input("Enter amount of water needs to be consumed (in ml):"))
    water_intake_per_break = int(input("Enter amount to be consumed in every interval(in ml) : "))
    min_attempts = int(total_water_intake_expected / water_intake_per_break)
    water_break_gap = int(w_h_time / min_attempts)
    ex_eye_gap = 3  # Capture gap for eye exercise 30 min
    eye_min_attempts = int(w_h_time / ex_eye_gap)
    # Capture current system time in minutes
    curr_time = int((t.localtime(t.time())).tm_hour * 60 + (t.localtime(t.time())).tm_min)
    d_status = str()
    d_e_status = str()
    print(total_water_intake_expected, water_intake_per_break, min_attempts, water_break_gap, w_start_time, w_end_time,
          curr_time, d_status)
    if (curr_time < w_end_time) and (curr_time > w_start_time):
        for e_water in range(min_attempts):
            pg.mixer.init()
            pg.mixer.music.load("C:\\Users\\KalkiAvatharam\\Downloads\\tune1-41324-2-56030.mp3")
            pg.mixer.music.play(0)
            print("Playing Music while drinking water")
            t.sleep(5)
            curr_time = int((t.localtime(t.time())).tm_hour * 60 + (t.localtime(t.time())).tm_min)
            d_status = str(input("Enter KeyWord DRANK "))
            if d_status == "DRANK":
                break
            else:
                continue
        for e_eye in range(eye_min_attempts):
            pg.mixer.init()
            pg.mixer.music.load("C:\\Users\\KalkiAvatharam\\Downloads\\tune1-41324-2-56030.mp3")
            pg.mixer.music.play(0)
            print("Playing Music while doing eye exercises")
            t.sleep(5)
            curr_time = int((t.localtime(t.time())).tm_hour * 60 + (t.localtime(t.time())).tm_min)
            d_e_status = str(input("Enter KeyWord ER "))
            if d_e_status == "ER":
                break
            else:
                continue

    print(total_water_intake_expected, water_intake_per_break, min_attempts, water_break_gap, w_start_time, w_end_time,
          curr_time, d_status, d_e_status)
    # Capture data in file
    with open("Activity_logger.txt", 'a') as f:
        f.write(f"***** Welcome Healthy Programmer Record******\n")
        f.write(f"Record Date:{dt.datetime.today()}\n")
        f.write(f"Work Start Timing:{w_start_time}\n")
        f.write(f"Work End Timing:{w_end_time}\n")
        f.write(f"Amount of water recommended:{total_water_intake_expected}\n")
        f.write(f"Amount of breaks Needed:{min_attempts}\n ")
        f.write(f"Amount of water per break needed:{water_intake_per_break}\n")
        f.write(f"Capture WB Status:{d_status}\n")
        f.write(f"Amount of eye exercise break Needed:{eye_min_attempts}\n ")
        f.write(f"Capture EB Status:{d_e_status}\n")
