import multiprocessing as mp
import time


class LeakyBucket():
    def __init__(self):
        self.tokens_released_per_100ms = 1
        self.max_bucket_size = 10
        self.queue = mp.Manager().list()
        self.queue_processor = mp.Process(target=self.process_queue)
        self.stop_event = mp.Event()
        self.queue_processor.start()

    # Add tokens to the bucket for use
    def request_token(self, id_in):
        if len(self.queue) < self.max_bucket_size:
            print("Requested Token: ", id_in)
            self.queue.append(id_in)
            return True
        else:
            return False

    def process_queue(self):
        last_time = time.time()
        while not self.stop_event.is_set():
            current_time = time.time()
            if (current_time - last_time) * 1000 >= 100 and len(self.queue) > 0:
                last_time = current_time
                for _ in range(self.tokens_released_per_100ms):
                    try:
                        print("Released Token: ", self.queue.pop(0))
                    except IndexError:
                        break
            time.sleep(0.01)

    # We call this to end the bucket refresh
    def kill_process(self):
        self.stop_event.set()
        self.queue_processor.join()


if __name__ == '__main__':
    rateLimiter = LeakyBucket()
    for _ in range(10):
        rateLimiter.request_token(_)
    start_time = time.time()
    while (time.time()-start_time) < 5:
        time.sleep(1)
    print("DONE!")
    rateLimiter.kill_process()