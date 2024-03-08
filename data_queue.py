import queue

class MessageQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def put(self, item):
        """Put an item into the queue."""
        self.queue.put(item)

    def get(self):
        """Remove and return an item from the queue."""
        return self.queue.get()

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.queue.empty()
    