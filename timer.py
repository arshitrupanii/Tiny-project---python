import time 

def alarm(second):
    time_elapsed = -1

    while time_elapsed < second:
        time.sleep(1)
        time_elapsed += 1

        time_left = second - time_elapsed
        min_left = time_left // 60
        sec_left = time_left % 60

        print(f"{min_left} : {sec_left}")

    # playsound("alarm.wav")


if __name__ == "__main__":
    second = int(input("enter the second : "))
    alarm(second)
