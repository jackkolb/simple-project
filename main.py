import time
import os

if __name__ == "__main__":
  count = 1
  while True:
    print(count, "env:", os.environment.get("TEST_ENV"))
    count += 1
    time.sleep(1)
