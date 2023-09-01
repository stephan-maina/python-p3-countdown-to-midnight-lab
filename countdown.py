# your code goes here!
import time

def countdown(start_number):
    while start_number > 0:
        print(f"{start_number} SECOND(S)!")
        start_number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(start_number):
    while start_number > 0:
        print(f"{start_number} SECOND(S)!")
        start_number -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")

# Example usage:
countdown(5)  # Countdown without sleep
countdown_with_sleep(5)  # Countdown with sleep
