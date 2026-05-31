# Main Driver Program
from car import Car
from car_dashboard_design import intro, loading, show_speed
import time

# MAIN PROGRAM
intro()
loading()

# Create Object
my_car = Car(2025, "Toyota Supra")

print(f"Car Model : {my_car.get_year_model()}")
print(f"Car Make  : {my_car.get_make()}\n")

# ACCELERATION
print("=" * 20)
print("ACCELERATION MODE")
print("=" * 20)

for i in range(5):

    my_car.accelerate()

    print(f"\nAcceleration #{i + 1}")
    show_speed(my_car.get_speed())

    time.sleep(0.7)

# BRAKING
print("=" * 20)
print("BRAKE MODE")
print("=" * 20)

for i in range(5):

    my_car.brake()

    print(f"\nBrake #{i + 1}")
    show_speed(my_car.get_speed())

    time.sleep(0.7)

print("=" * 55)
print("        Simulation Complete Successfully!")
print("=" * 55)


