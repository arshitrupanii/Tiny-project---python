import time,os, notification

def clock(second):
    timer = 0
    while timer < second:
        os.system('cls')
        print(second)
        time.sleep(1)
        second = second - 1
    def er():
        notification.notify(title = "Drink Water", message = "now" , timeout = 1)
    er()

clock(int(input("Enter the second for notifiaction: ")))