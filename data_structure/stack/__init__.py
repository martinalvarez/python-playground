class Stack:
    def __init__(self):
        self.items = []


    def debug(self):
        print(self.items)


    def isEmpty(self) -> bool:
        return self.items == []


    def pop(self) -> int:
        return self.items.pop()


    def push(self, item: int):
        self.items.append(item)
   

    def size(self) -> int:
        return len(self.items)