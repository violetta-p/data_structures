class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди.
        :return: Данные удаленного элемента
        """
        if self.head is None:
            return None
        result = self.head
        self.head = self.head.next_node
        return result.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head:
            data_list = []
            current_head = self.head
            while current_head is not None:
                data_list.append(current_head.data)
                current_head = current_head.next_node
            return "\n".join(data_list)
        else:
            return ""

