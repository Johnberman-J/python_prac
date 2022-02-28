# 큐 > 회전하는 큐

class Circular_Queue:
    def __init__(self, size):
        self.queue = list(range(1, int(size)+1))        
    def pop(self):
        data = self.queue.pop(0)
        return data
    def moveLeft(self):
        data = self.queue.pop(0)
        self.queue.append(data)
        return
    def moveRight(self):
        data = self.queue.pop()
        self.queue.insert(0,data)
        return
