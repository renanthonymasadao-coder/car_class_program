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
