class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.function = 'left'

    def add_item(self, item: int):
        """if item < self.value:
            self.left = Node(item)
        else:
            self.left = Node(item)"""
        return Node(item)
            # en supposant qu'il n'y a que des items uniques

    def add_where(self, item: int):
        if item < self.value:
            return self.left
        return self.right

    def __next__(self):
        if self.function == 'left':
            return self.left
        return self.right


class BinaryTree:
    def __init__(self, racine: Node):
        self.racine = Node(racine)
        self.depth = 0
        self.function = 'left'

    def search(self, item_to_search: int):
        current = self.racine

        while current and next(current):
            if current.value == item_to_search:
                print('Found item {}'.format(item_to_search))
                break
            if item_to_search < current.value:
                current.function = 'left'
            else:
                current.function = 'right'
            if next(current):
                current = next(current)
        return current

    def add_item(self, item_value: int):
        current = self.search(item_value)

        if current.value < item_value:
            current.right = current.add_item(item_value)
        else:
            current.left = current.add_item(item_value)

        """if current.left:
            print('current-left', current.left.value)
        if current.right:
            print('current-right', current.right.value)"""

    def show(self):
        current = self.racine
        print('La fonction de parcours va vers {}'.format(current.function))
        while current:
            print('\nObjet courrant:', current.value)
            if current.left:
                print('\tcurrent-left', current.left.value)
            if current.right:
                print('\tcurrent-right', current.right.value)
            current.function = 'right'
            current = next(current)
        print('\nFin de parcours')

bT = BinaryTree(4)
bT.add_item(0)
bT.add_item(3)
bT.add_item(1)
bT.add_item(7)
bT.add_item(8)
bT.add_item(6)
bT.add_item(10)
bT.show()

