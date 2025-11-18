import os
import time

message = os.getenv("MESSAGE", "No MESSAGE variable found")
print(message)

# Prevent container from exiting
while True:
    time.sleep(1)
