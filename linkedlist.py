class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Use consistent casing, change from self.Next to self.next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertion_at_beginning(self, data):
        newdata = Node(data)
        newdata.next = self.head
        self.head = newdata

    def insertion_at_the_end(self, data):
        newdata = Node(data)
        if not self.head:
            self.head = newdata
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newdata

    def insertion_at_a_specific_location(self, data, position):
        newdata = Node(data)
        if position == 0:
            newdata.next = self.head
            self.head = newdata
            return
        current = self.head  # Initialize current to self.head
        for _ in range(position - 1):
            if current is None:
                raise ValueError("Invalid position broski")
            current = current.next
        newdata.next = current.next
        current.next = newdata

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

##example##
# Create a linked list
my_list = Linkedlist()

# Insert elements at the beginning
my_list.insertion_at_beginning(10)
my_list.insertion_at_beginning(20)

# Insert elements at the end
my_list.insertion_at_the_end(30)
my_list.insertion_at_the_end(40)

# Insert element at a specific location
my_list.insertion_at_a_specific_location(25, 2)

# Display the linked list
my_list.display()

