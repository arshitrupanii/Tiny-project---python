from plyer import notification
import time


print('''.Drink water  ''')
def reminder():
    notification.notify(title = "Drink Water", message = "now" , timeout = 1)

while True:  
    reminder()
    time.sleep(10)