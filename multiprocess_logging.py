import logging
from multiprocessing import Queue, Process
import os
import threading
import time
import datetime

logger = None


class QueueHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        self.queue = kwargs.pop('queue')

        super(QueueHandler, self).__init__(*args, **kwargs)

    def emit(self, record):
        self.queue.put(record)


def logger_thread(q, log_file):
    file_handler = logging.FileHandler(os.path.join('/tmp', log_file))
    file_handler.setFormatter(
        logging.Formatter(fmt='%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'))
    l = logging.getLogger(layer_name)
    l.propagate = False
    l.addHandler(file_handler)
    while True:
        record = q.get()
        if record is None:
            break
        l.handle(record)


def action():
    for i in range(10):
        logger.info('Step %s' % str(i))
        time.sleep(1)


def worker(q):
    global logger

    qh = QueueHandler(queue=q)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(qh)

    action()


def init():
    q = Queue()
    lp = threading.Thread(target=logger_thread, args=(q, datetime.date.today().strftime("%B_%d_%Y")))
    lp.start()

    qqh = QueueHandler(queue=q)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(qqh)

    logger.info("Start")

    workers = []
    for i in range(5):
        wp = Process(target=worker, name='worker %d' % (i + 1), args=(q,))
        workers.append(wp)
        wp.start()
        time.sleep(0.2)

    for wp in workers:
        wp.join()

    q.put(None)
    lp.join()

    # This line is not logged
    logger.info("End")


if __name__ == '__main__':
    init()
