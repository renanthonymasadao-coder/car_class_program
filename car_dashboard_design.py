# Dashboard Display Functions
import time

def intro():

    print("\n" + "=" * 55)
    print("        🚗 SUPER CAR SPEED SIMULATOR 🚗")
    print("=" * 55)

def loading():

    print("\nStarting Engine", end="")

    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)

    print("\nEngine Started Successfully!\n")

def show_speed(speed):

    print(f"Current Speed: {speed} km/h")

    if speed == 0:
        print("Status: 🛑 Stopped\n")

    elif speed <= 15:
        print("Status: 🚘 Cruising\n")

    elif speed <= 25:
        print("Status: 🏎️ Fast Mode\n")

    else:
        print("Status: 🔥 MAXIMUM SPEED\n")