class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class QueueArray:
    def __init__(self, capacity):
        # the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = 0 # pointer to the front of queue
        self.rear = 0 # pointer to the rear of queue
        self.items = [None]*capacity # array whose size is the capacity
        self.num_items = len(self.items) # number of items in array

    def is_empty(self):
        count = 1
        for x in self.items:
            if x is None:
                count +=1
            if count == self.capacity:
                return True
            else:
                return False

    def is_full(self):
        count = 1
        if self.size() == self.capacity:
            for x in self.items:
                if x is None:
                    count += 1
            if count == len(self.items):
                return False
            return True
        return False

    def enqueue(self, item):
        if self.is_full() is True:
            raise IndexError
        else:
            # add element to the queue
            self.items.append(item)
            # increment the tail pointer
            self.rear = (self.rear + 1) % self.capacity
            return True

    def dequeue(self):
        if self.items.is_empty() is True:
            raise IndexError
        else:
            # fetch data
            item = self.items[self.front]
            # increment head
            self.front = (self.front + 1) % self.capacity
            return item

    # returns the number of items in the queue
    def size(self):
        if self.rear >= self.front:
            queue_size = len(self.items)
        else:
            queue_size = self.capacity - (self.front - self.rear)
            # return the size of the queue
        return queue_size


# You must have the same functionalities for the Linked List Implementation
class QueueLinked:

    def __init__(self, capacity):
        # the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = self.rear = None # pointer to the front of queue and pointer to the rear of queue
        self.num_items = 0

    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def is_full(self):
        if self.size() == self.capacity:
            return True
        return False

    def enqueue(self, item):
        temp = Node(item)
        if self.is_full():
            raise IndexError
        if self.rear is None:
            self.front = self.rear = temp

        self.rear.next = temp
        self.rear = temp
        self.num_items += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        self.num_items -= 1
        return str(temp.data)

    # returns the number of items in the queue
    def size(self):
        return self.num_items
