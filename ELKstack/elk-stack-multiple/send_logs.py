import json
import socket
import time
import random
import os

#sample log messages
sample_logs = [
    {"level": "INFO", "message": "User logged in", "user_id": 1},
    {"level": "DEBUG", "message": "Query executed", "user_id": 3},
]
error_logs = [
    {"level": "ERROR", "message": "Failed to connect to database", "user_id": 2},
    {"level": "ERROR", "message": "Permission denied", "user_id": 4},
]
# local set up 
LOGS_DIR = "./logs"
LOG_FILE = "python_logs.log"

#write log into local file 
def send_log(log):
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    with open(os.path.join(LOGS_DIR, LOG_FILE), "a") as f:
        f.write(json.dumps(log) + "\n")
        print(f"Sent log: {log}")


def simulate_log_stream():
    while True:
        if random.random() < 0.1:
            log = random.choice(error_logs)
        else:
            log = random.choice(sample_logs)

        send_log(log)
        print(log)
        time.sleep(random.uniform(0.5, 3))

if __name__ == "__main__":
    simulate_log_stream()