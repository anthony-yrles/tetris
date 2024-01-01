import time
from globales import *

def chrono():
    time_begin = get_time_begin()
    time_running = time.time() - time_begin
    set_time_end_game(time_running)
    return time_running