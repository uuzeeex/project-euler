import time


class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, tb):
        if self.name:
            print('[%s] ' % self.name, end='')
        print('Elapsed: %s (s)' % (time.time() - self.start))
