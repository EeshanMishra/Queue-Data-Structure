import unittest
from queues import *
class MyTest(unittest.TestCase):

    def test_is_empty(self):
        """tests is_empty() function"""
        my_queue = QueueArray(3)
        self.assertTrue(my_queue.is_empty())
        my_queue.enqueue(0)
        self.assertFalse(my_queue.is_empty())
        my_queue.dequeue()
        self.assertTrue(my_queue.is_empty())

        my_linked = QueueLinked(3)
        self.assertTrue(my_linked.is_empty())
        my_linked.enqueue(0)
        self.assertFalse(my_linked.is_empty())
        my_linked.dequeue()
        self.assertTrue(my_linked.is_empty())

    def test_is_full(self):
        """tests is_full() function"""
        my_queue = QueueArray(3)
        self.assertFalse(my_queue.is_full())
        my_queue.enqueue(1)
        self.assertFalse(my_queue.is_full())
        my_queue.enqueue(2)
        self.assertFalse(my_queue.is_full())
        my_queue.enqueue(3)
        self.assertTrue(my_queue.is_full())
        my_queue.dequeue()
        self.assertFalse(my_queue.is_full())

        my_linked = QueueLinked(3)
        self.assertFalse(my_linked.is_full())
        my_linked.enqueue(1)
        self.assertFalse(my_linked.is_full())
        my_linked.enqueue(2)
        self.assertFalse(my_linked.is_full())
        my_linked.enqueue(3)
        self.assertTrue(my_linked.is_full())
        my_linked.dequeue()
        self.assertFalse(my_linked.is_full())

