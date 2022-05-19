import time


def stop_watch(sec):
    """
    :param sec: time in seconds
    :return: time lapsed ie difference between start and end time
    """
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


input("Press Enter to start ")
start_time = time.time()

input("Press Enter to stop ")
end_time = time.time()

time_lapsed = end_time - start_time
stop_watch(time_lapsed)


if __name__ == '__main__':
    stop_watch(4)
