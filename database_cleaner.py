import schedule
import threading
import time


def worker():
    while True:
        schedule.run_pending()
        time.sleep(schedule.idle_seconds())


def start(job):
    schedule.every(30).minutes.do(job)
    threading.Thread(target=worker).start()
