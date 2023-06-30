class Node:
    """Класс для узла односвязного списка"""
    def __init__(self):
        self.data = None
        self.next_node = None


class LinkedList:
    """
    Класс для односвязного списка
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел
        с этими данными в начало связанного списка
        """
        new_node = Node()
        new_node.data = data
        if not self.head:
            self.head = self.tail = new_node
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет
        узел с этими данными в конец связанного списка
        """
        new_node = Node()
        new_node.data = data
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """
        Вывод данных односвязного списка
        в строковом представлении
        """
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.lstrip()

    def to_list(self):
        data_list = []
        if self.head:
            current_head = self.head
            while current_head is not None:
                data_list.append(current_head.data)
                current_head = current_head.next_node
            return data_list
        else:
            return data_list

    def get_data_by_id(self, value):
        result = None
        data_list = self.to_list()
        for item in data_list:
            try:
                result = item if item['id'] == value else None
            except TypeError:
                print('Данные не являются словарем или в словаре нет ключа id')
        if result is None:
            return f"{'Нет записей с данным id'}"
        return result
