import threading
import time


def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for {} seconds\n'.format(name, n))
    time.sleep(n)
    print('{} has woken up from sleep\n'.format(name))


threads_list = []
start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper,
                         name=f'thread.{i}',
                         args=(5, f'thread.{i}'))
    threads_list.append(t)

    t.start()
    print(f'{t.name} has started')

for t in threads_list:
    t.join()

end = time.time()
print(f'time taken: {end - start}')
print('All five threads have finished their jobs')

# Without Threading
start = time.time()
for i in range(5):
    sleeper(2, i)

end = time.time()
print(f'time take : {end - start}')
