class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        if self.top is not None:
            data_list = []
            current_top = self.top
            while current_top is not None:
                data_list.append(current_top.data)
                current_top = current_top.next_node
            return '\n'.join(data_list)
        else:
            return 'No data'

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data)  # Создание нового узла
        if self.top:
            node.next_node = self.top
        self.top = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения
        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        result = self.top.data
        self.top = self.top.next_node
        return result
