#building for Node
class Node:
    def __init__(self,value,next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
    
    def __str__(self):
        return ' -> '.join([str(node)for node in self])
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count+=1
            node = node.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    @property
    def values(self):
        return [node.value for node in self]
    
    def add_to_tail(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_node_to_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value,self.head)
        return self.head
    def add_multiple_nodes(self,values):
        for value in values:
            self.add_to_tail(value)

class DoublyLinkedList(LinkedList):
    def add_to_tail(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value,None,self.tail)
            self.tail = self.tail.next
        return self
    
    def add_node_to_head(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head
    
class Display:
    def choices(self):
        print('what do you wnat to do:\n 1) create list\n 2)Linked List\n')
        choice = int(input('Enter choice: '))
        if choice==1:
            self.create_list_from_head()
        elif choice == 2:
            self.create_list_from_tail()
        elif choice==3:
            list_l = LinkedList()
            print(list_l.values)
            self.choices()
        else:
            print('invalid choice')

    def create_list_from_tail(self):
        entry = int(input('total numbers to add: '))
        list_l = LinkedList()
        for i in range(entry):
            new_entry = int(input('Enter Number: '))
            list_l.add_to_tail(new_entry)
        print(list_l.values)
        self.choices()
    
    def create_list_from_head(self):
        entry = int(input('total numbers to add: '))
        list_l = LinkedList()
        for i in range(entry):
            new_entry = int(input('Enter Number: '))
            list_l.add_node_to_head(new_entry)
        print(list_l.values)
        self.choices()

if __name__ == '__main__' :
    Display().choices()