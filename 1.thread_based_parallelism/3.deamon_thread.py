import threading
import time

total = 4

def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('added item')
        total += 1
    print('creation is done')

def creates_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('added item')
        total += 1
    print('creation is done')

def limits_items():
    global total
    while True:
        if total > 5:
            print('overload')
            total -= 3
            print('subtracted 3')
        else:
            time.sleep(1)
            print('waiting')

creater_1 = threading.Thread(target=creates_items)
creater_2 = threading.Thread(target=creates_items_2)
# limiter = threading.Thread(target=limits_items)
limiter = threading.Thread(target=limits_items, daemon=True)

creater_1.start()
creater_2.start()
limiter.start()

creater_1.join()
creater_2.join()
# limiter.join()


print(f'out ending value of total is {total}')
