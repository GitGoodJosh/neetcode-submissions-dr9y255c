class cNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def checkindexError(self,index):
        if index < 0 or index > self.size:
            return True
        else:
            return False


    def get(self, index):
        if self.checkindexError(index):
            return -1
        
        current = self.head
        for _ in range(0,index):
            current = current.next
        
        return current.val
        

    def addAtHead(self, val):
        self.addAtIndex(0,val)
        

    def addAtTail(self, val):
        self.addAtIndex((self.size) , val)
        

    def addAtIndex(self, index, val):
        if self.checkindexError(index):
            return -1
        
        current = self.head
        newnode = cNode(val)

        if index <=0:
            newnode.next = current
            self.head = newnode
        else:
            for _ in range(index - 1):
                current = current.next
            newnode.next = current.next
            current.next = newnode
        self.size += 1
        

    def deleteAtIndex(self, index):
        
        if self.checkindexError(index):
            return -1

        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
        
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
