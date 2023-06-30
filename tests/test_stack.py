"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack
import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(3, self.stack.top.data)
        self.assertEqual(2, self.stack.top.next_node.data)
        self.assertEqual(1, self.stack.top.next_node.next_node.data)
        self.assertEqual(None, self.stack.top.next_node.next_node.next_node)

    def test_pop(self):
        self.assertEqual(None, self.stack.top)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(3, self.stack.pop())
        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.pop())
        self.assertEqual(None, self.stack.top)

    def test_str(self):
        self.assertEqual('No data', str(self.stack))
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual('data3\ndata2\ndata1', str(self.stack))
