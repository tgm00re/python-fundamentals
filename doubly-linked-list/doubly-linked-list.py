from email import header


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self.head = None

    def addToFront(self, value):
        print("adding to front")
        new_node =  Node(value)
        new_node.next = self.head
        new_node.prev = None
        #check if not empty
        if(self.head != None):
            self.head.prev = new_node
        self.head = new_node
        return self
        

    def addEnd(self, value):
        new_node = Node(value)
        new_node.next = None
        if(self.head == None):
            self.head = new_node
            return self
        current_node = self.head
        while(current_node.next != None):
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        return self

    def addValue(self, value, n):
        new_node = Node(value)
        if(n == 0):
            self.addToFront(value)
            return self
        if(self.head == None or n < 0): #invalid input!
            print("invalid index")
            return self
        current_node = self.head
        previous_node = None
        index = 0
        while(current_node.next != None):
            if(n == index):
                new_node.prev = previous_node
                new_node.next = current_node.next
                previous_node.next = new_node
                current_node.next.prev = new_node
                return self
            previous_node = current_node
            current_node = current_node.next
            index += 1
        if(index == n):
            previous_node.next = new_node
            new_node.prev = previous_node
            new_node.next = current_node
            current_node.prev = new_node
        elif(index == n-1): #trying to add value to the end of the list
            self.addEnd(value)
        else:
            print("invalid index")
        return self

    def printList(self):
        if(self.head == None):
            return self
        current_node = self.head
        while(current_node.next != None):
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)
        return self
            
        
        

    



my_list = DList()
my_list.addToFront(5).addEnd(4).addEnd(3).addEnd(2).addEnd(1).addToFront(6).addValue(27,6).printList()


# 6, 5, 4, 3, 2, 1, 
# 0, 1, 2, 3, 4, 5,


