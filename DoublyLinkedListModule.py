
class Node:
     def __init__(self, data):
        self.data = data       # Data stored in the node
        self.next = None       # Pointer to the next node
        self.prev = None       # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            print("Head node data",self.head.data)
            self.tail = new_node
            print("tail node data",self.tail.data)
        else:
            self.tail.next = new_node  # Link the new node to the end of the list
            print("Tail Next node",self.tail.next.data)
            new_node.prev = self.tail  # Link the new node back to the current tail
            print("Previous Node",new_node.prev.data)
            self.tail = new_node       # Update the tail to the new node
            print("Updated tail data",self.tail.data)

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            self.prepend(data)
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            return  # Index out of bounds
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current


    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                print("Value Address is",id(current))  # Or return position if needed
            current = current.next
        return ValueError

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return IndexError  # Index out of bounds

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes)

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(100)
    dll.append(200)
    dll.append(300)
    dll.append(400)
    print("Doubly Linked List is ",dll)
    dll.search(300)
    dll.get(1)
    dll.insert(2,250)
    print(dll)
