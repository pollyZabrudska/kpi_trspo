import threading
import time

def calculate_squares():
    for i in range(1, 6):
        print(f"Square of {i} = {i*i}")
        time.sleep(1)

def calculate_cubes():
    for i in range(1, 6):
        print(f"Cube of {i} = {i*i*i}")
        time.sleep(1)

thread1 = threading.Thread(target=calculate_squares)
thread2 = threading.Thread(target=calculate_cubes)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Calculations completed.")
