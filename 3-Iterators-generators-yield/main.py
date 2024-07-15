class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = self.flatten_list()

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.flat_list):
            raise StopIteration
        item = self.flat_list[self.current_index]
        self.current_index += 1
        return item

    def flatten_list(self):
        flat_list = []
        for sub_list in self.list_of_list:
            flat_list.extend(sub_list)
        return flat_list


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
