# Singly LinkedList
# Creating a node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Creating a LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data): # Insert a value at begining of LinkedList
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data): # Insert a value at end of LinkedList
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list): # Take values and creates new LinkedList
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_begining(50)
    # ll.insert_at_begining(40)
    # ll.insert_at_end(60)
    ll.insert_values(["Charan", "Dheeraj", "Bharath", "Tyson"])
    ll.print()
    print("Length of LinkedList:", ll.get_length()) # print the length of the LinkedList
    ll.remove_at(3) # removing value at index 3
    ll.print()
    ll.insert_at(1, "sravan")
    ll.insert_at(0, "Tyson")
    ll.print()