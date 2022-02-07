class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class SList:
    def __init__(self) -> None:
        self.head = None

    def addToFront(self, value):
        #create a new node
        new_node = Node(value)
        #set new_node reference to current head
        new_node.next = self.head
        #set new_node to the head of the list
        self.head = new_node
        return self

    def print_values(self):
        if(self.head == None):
            return self
        current_node = self.head
        while(current_node.next != None):
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)
        return self

    def addToBack(self, value):
        if(self.head == None):
            self.addToFront(value)
            return self
        new_node = Node(value)
        current_node = self.head
        while(current_node.next != None):
            current_node = current_node.next
        current_node.next = new_node
        return self

    def removeFromFront(self):
        if(self.head.next == None):
            self.head = None
            return self
        self.head = self.head.next
        return self

    def removeFromBack(self):
        if(self.head.next == None):
            self.removeFromFront()
            return self
        current_node = self.head
        while(current_node.next.next != None):
            current_node = current_node.next
        current_node.next = None
        return self

    def removeVal(self, value):
        if(self.head == None):
            return self
        if(self.head.value == value):
            self.removeFromFront()
            return self
        prev_node = None
        current_node = self.head
        while(current_node.next != None):
            if(current_node.value == value):
                prev_node.next = current_node.next
                return self
            prev_node = current_node
            current_node = current_node.next
        if(current_node.value == value):
            self.removeFromBack()
        return self

    def insertAt(self, value, n):
        if(n == 0):
            self.addToFront(value)
            return self
        new_node = Node(value)
        prev_node = None
        current_node = self.head
        index = 0
        while(current_node.next != None):
            print("index: " + str(index))
            if(index == n):
                print(str(index) + " == " + str(n) + ", adding at index")
                prev_node.next = new_node
                new_node.next = current_node
                return self
            index += 1
            prev_node = current_node
            current_node = current_node.next
        if(n == index):
            print(str(index) + " == " + str(n) + ", adding to back")
            prev_node.next = new_node
            new_node.next = current_node
            return self
        if(n == index + 1):
            self.addToBack(value)
        else:
            print("specified index DNE")
        return self
        


    


# my_list = SList()
# my_list.addToFront("are").addToFront("Linked lists").addToBack("fun!").removeFromBack().print_values()
# my_list.addToFront("bye").addToBack("hello").addToBack("thomas").removeVal("hello").print_values()
# my_list.addToFront("bye").addToBack("hello").insertAt("hi", 0).print_values()

