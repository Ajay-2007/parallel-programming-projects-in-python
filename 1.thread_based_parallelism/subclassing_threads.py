import time
import threading

class MyThread(threading.Thread):
    def run(self):
        """Method representing the thread's activity.

        You may override this method in a subclass. The standard run() method
        invokes the callable object passed to the object's constructor as the
        target argument, if any, with sequential and keyword arguments taken
        from the args and kwargs arguments, respectively.

        """
        print(f'{self.getName()} has started')
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs

        print(f'{self.getName()} has finished')


def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for {} seconds\n'.format(name, n))
    time.sleep(n)
    print('{} has woken up from sleep\n'.format(name))

def test_my_thread():
    for i in range(5):
        t = MyThread(target=sleeper,
                     name = f'thread.{i+1}',
                     args=(2, f'thread.{i+1}'))
        t.start()

class MySecondThread(threading.Thread):
    def __init__(self, number, func, args):
        super(MySecondThread, self).__init__()
        self._number = number
        self._func  = func
        self._args = args

    def run(self):
        print(f'thread {self._number} has started')
        self._func(*self._args)
        print(f'thread {self._number} has finished')


def doubles(number, cycles):
    for i in range(cycles):
        number *= 2
    print(number)

def test_my_second_thread():
    threads_list = []
    for i in range(5):
        t = MySecondThread(i+1, doubles, (i+1, 5))
        threads_list.append(t)
        t.start()

    for t in threads_list:
        t.join()

if __name__ == '__main__':
    test_my_thread()
    test_my_second_thread()