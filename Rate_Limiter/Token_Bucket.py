import multiprocessing as mp
import time


class TokenBucket():
    def __init__(self):
        self.tokens_add_per_100ms = 1
        self.max_bucket_size = 10
        self.bucket = mp.Value('i', 0)
        self.bucket_filler = mp.Process(target=self.bucket_refresh)
        self.stop_event = mp.Event()
        self.bucket_filler.start()

    # Add tokens to the bucket for use
    def __add_to_bucket(self):
        with self.bucket.get_lock():
            if self.bucket.value < self.max_bucket_size:
                self.bucket.value += 1

    # Check to see if we have any tokens in the bucket
    def __token_available(self):
        with self.bucket.get_lock():
            return self.bucket.value > 0

    # We request a token and if one is available we return TRUE else FALSE
    def request_token(self):
        with self.bucket.get_lock():
            if self.__token_available():
                self.bucket.value -= 1
                return True
            return False

    # This is a seperate process that we are running to periodically fill the bucket (but won't overfill the bucket)
    def bucket_refresh(self):
        counter = 0
        last_time = time.time()
        while not self.stop_event.is_set():
            current_time = time.time()
            if (current_time - last_time)*1000 >= 100:
                for _ in range(self.tokens_add_per_100ms):
                    self.__add_to_bucket()
                last_time = current_time
            counter += 1

    # We call this to end the bucket refresh
    def kill_proces(self):
        self.stop_event.set()
        self.bucket_filler.join()


if __name__ == '__main__':
    rateLimiter = TokenBucket()
    start_time = time.time()
    # let's let a few tokens build up
    print("Build up some tokens")
    while (time.time()-start_time) < 1:
        time.sleep(1)

    print("Tokens: ", rateLimiter.bucket.value)
    ms_per_request = 50
    start_time = time.time()
    counter = 100
    while counter > 0:
        if (time.time() - start_time)*1000 >= ms_per_request:
            counter -= 1
            start_time = time.time()
            print("request a token: ", rateLimiter.request_token())

    rateLimiter.kill_proces()
