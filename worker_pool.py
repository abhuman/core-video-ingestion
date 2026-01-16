import threading

class WorkerPool:
    def submit(self, fn, *args):
        threading.Thread(target=fn, args=args, daemon=True).start()
