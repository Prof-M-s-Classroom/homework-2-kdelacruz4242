from Spaceship import Spaceship

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def insertatindex(self, index, value):
        if index > self.length: #if index is greater than total list length
            return False

        if index < 0: #if index is less than 0
            return False

        if index == 0: #if index = 0, this will prepend the value at 0
            self.prepend(value)
            return True

        if index == self.length: #if index is at the end of the list, this will append the value last on list
            self.append(value)
            return True

        new_node = Node(value)
        temp = self.head
        for i in range (index - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def deleteatindex(self, index):
        if index > self.length: #if index is greater than total list length
            return None

        if index < 0: #if index is less than 0
            return None

        if index == 0: #if index = 0, this will prepend the value at 0
            return self.delfirst()

        temp = self.head
        for i in range (index - 1):
            temp = temp.next

        del_node = temp.next
        temp.next = del_node.next

        if index == self.length:  # if index is at the end of the list, this will append the value last on list
            self.tail = temp

        self.length -= 1
        return del_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.
# TODO : Write function deleteatindex to delete a newnode at any given index. Consider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.

s1 = Spaceship("Voyager", 300)
s2 = Spaceship("Enterprise", 300)
s3 = Spaceship("Atlantis", 300)
s4 = Spaceship("Challenger", 300)
s5 = Spaceship("Artemis", 300)

mylinkedlist = LinkedList(s1) #list is made containing s1 first
mylinkedlist.append(s2) #add to end of list
mylinkedlist.print_list()
print ("\t")

mylinkedlist.append(s3)
mylinkedlist.print_list()
print ("\t")

mylinkedlist.prepend(s4) #put in front of list
mylinkedlist.print_list()
print ("\t")

mylinkedlist.prepend(s5)
mylinkedlist.print_list()
print ("\t")

mylinkedlist.insertatindex(2, s3) #will insert Atlantis in [2] position
mylinkedlist.print_list()
print ("\t")

mylinkedlist.deleteatindex(2) #will delete Atlantis in [2] position
mylinkedlist.print_list()