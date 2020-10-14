from _celery.tasks import count_words

import time


if __name__ == '__main__':
    result = count_words.delay(4, 4)
    print 'Task result:', result.get(timeout=6)
