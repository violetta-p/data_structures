"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual('data1', self.queue.head.data)
        self.assertEqual('data2', self.queue.head.next_node.data)
        self.assertEqual('data3', self.queue.tail.data)
        self.assertEqual(None, self.queue.tail.next_node)

    def test_dequeue(self):
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual('data1', self.queue.dequeue())
        self.assertEqual('data2', self.queue.dequeue())
        self.assertEqual('data3', self.queue.dequeue())
        self.assertEqual(None, self.queue.dequeue())

    def test_str(self):
        self.assertEqual("", str(self.queue))
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual('data1\ndata2\ndata3', str(self.queue))
