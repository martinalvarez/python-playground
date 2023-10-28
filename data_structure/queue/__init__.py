class Queue:
    def __init__(self):
        self.items = []


    def debug(self):
        print(self.items)


    def dequeue(self) -> int:
        return self.items.pop()


    def enqueue(self, item: int):
        self.items.insert(0, item)


    def isEmpty(self) -> bool:
        return self.items == []
        

    def size(self) -> int:
        return len(self.items)


