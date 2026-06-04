from car import Car
import time
lenard_car = Car("2026", "lenard sports car")
for i in range(5):
    lenard_car.accelerate()
    print(f"lenard's car accelerated, current speed: {lenard_car.get_speed()}")
    time.sleep(1)

for i in range(5):
    lenard_car.brake()
    print(f"lenard's car braked, current speed: {lenard_car.get_speed()}")
    time.sleep(1)    