"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored in
form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)


class CustomList(object):

    def __init__(self, *items):
        self._head = None
        if items:
            item = Item(value=items[0])
            items = items[1:]
            self._head = item
            for value in items:
                item.next = Item(value=value)
                item = item.next

    def append(self, value):
        item = Item(value)
        if not self._head:
            self._head = item
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = item

    def add_start(self, value):
        item = Item(value)
        item.next = self._head
        self._head = item

    def remove(self, value):
        current = self._head
        previous = None
        while current:
            if current.value == value:
                if not previous:
                    self._head = current.next
                else:
                    previous.next = current.next
                return
            else:
                previous = current
                current = current.next
        raise ValueError

    def __getitem__(self, index):
        for i, item in enumerate(self):
            if i == index:
                return item.value
        else:
            raise IndexError

    def __setitem__(self, index, data):
        for i, item in enumerate(self):
            if i == index:
                item.value = data
                return
        else:
            raise IndexError

    def __delitem__(self, index):
        current = self._head
        previous = None
        i = 0
        while current:
            if i == index:
                if not previous:
                    self._head = current.next
                else:
                    previous.next = current.next
                return
            else:
                i += 1
                previous = current
                current = current.next
        raise IndexError

    def clear(self):
        for _ in range(len(self)):
            self.__delitem__(0)

    def __str__(self):
        item = self._head
        items = []
        while item:
            items.append(item.value)
            item = item.next
        items.append(None)
        return str(items)

    def find(self, value):
        current = self._head
        index = 0
        while current:
            if current.value == value:
                return index
            else:
                index += 1
                current = current.next
        raise ValueError

    def __len__(self):
        current = self._head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        item = self._head
        while item:
            yield item
            item = item.next

