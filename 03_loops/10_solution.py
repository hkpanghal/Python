# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
retries = 5
attempt = 1
while(attempt <= retries):
    print("attempt ",attempt,wait_time,"sec")
    wait_time = wait_time*2
    attempt +=1
    time.sleep(wait_time)

