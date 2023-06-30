from src.linked_list import LinkedList
import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual({'id': 0}, self.ll.head.data)
        self.assertEqual({'id': 1}, self.ll.tail.data)

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.assertEqual({'id': 2}, self.ll.head.data)
        self.assertEqual({'id': 3}, self.ll.tail.data)

    def test_str(self):
        self.assertEqual('None', str(self.ll))
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_beginning({'id': 1})
        self.assertEqual("{'id': 1} -> {'id': 2} -> None", str(self.ll))

    def test_to_list(self):
        self.assertEqual([], self.ll.to_list())
        self.ll.insert_beginning({'id': 1, 'user': 'lazzy'})
        self.ll.insert_at_end({'id': 2, 'user': 'mik'})
        self.assertEqual([{'id': 1, 'user': 'lazzy'},
                          {'id': 2, 'user': 'mik'}], self.ll.to_list())

    def test_get_data_by_id(self):
        self.ll.insert_beginning({'id': 1, 'user': 'lazzy'})
        self.ll.insert_at_end({'id': 2, 'user': 'mik.r'})
        self.ll.insert_at_end({'id': 3, 'user': 'mosh'})
        self.ll.insert_beginning({'id': 0, 'user': 'serebro'})
        self.assertEqual({'id': 3, 'user': 'mosh'}, self.ll.get_data_by_id(3))
        self.assertEqual('Нет записей с данным id', self.ll.get_data_by_id(5))

    def test_exceptions(self):
        self.ll.insert_beginning({'id': 1, 'user': 'lazzy'})
        self.ll.insert_at_end('idusername')
        self.ll.insert_at_end([1, 2, 3])
        self.ll.insert_at_end({'id': 2, 'user': 'mosh'})
        self.assertRaises(TypeError, self.ll.get_data_by_id(2))
        self.assertEqual({'id': 2, 'user': 'mosh'}, self.ll.get_data_by_id(2))
