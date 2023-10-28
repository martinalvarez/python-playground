from data_structure.queue import Queue
from data_structure.stack import Stack

def play_with_queue():
    queue = Queue()
    isEmpty = queue.isEmpty()
    print(isEmpty)

    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.debug()
    size = queue.size()
    print(size)

    q = queue.dequeue()
    print(q)
    queue.debug()

    q = queue.dequeue()
    print(q)
    queue.debug()

    q = queue.dequeue()
    print(q)
    queue.debug()

    q = queue.dequeue()
    print(q)
    queue.debug()

    q = queue.dequeue()
    print(q)
    queue.debug()


def play_with_stack():
    stack = Stack()
    print(stack.isEmpty())
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    print(stack.size())

    s = stack.pop()
    print(s)
    print(stack.size())
    

play_with_stack()

