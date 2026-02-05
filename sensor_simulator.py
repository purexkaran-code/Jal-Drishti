import time
import random
import os

# Create the file if it doesn't exist
if not os.path.exists("water_data.csv"):
    with open("water_data.csv", "w") as f:
        f.write("timestamp,water_level\n")

print("Sensor is running... (Press Ctrl+C to stop)")

try:
    while True:
        # Simulate water level rising slowly (random number between 35 and 50)
        level = random.uniform(35, 50) 
        
        # Open the file, write the data, and close it automatically
        with open("water_data.csv", "a") as f:
            f.write(f"{time.time()},{level}\n")
        
        # Wait 1 second before adding more data
        time.sleep(1)

except KeyboardInterrupt:
    print("\n✅ Sensor stopped by user. Goodbye!")