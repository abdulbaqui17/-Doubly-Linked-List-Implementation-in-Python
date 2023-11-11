class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class dll:
    def __init__(self):
        self.start=None
    
    def is_empty(self):
        return self.start is None
    
    def insert_first(self,data):
        n=node(data)
        if self.start is not None:
            self.start.prev=n
        n.next=self.start
        self.start=n
    
    def insert_last(self,data):
        n=node(data)
        if self.start is None:
            n.next=self.start
            self.start=n
        else:
            current=self.start
            while current.next is not None:
                current=current.next
            current.next=n
            n.prev=current
    
    def insert_after(self,target,data):
        n=node(data)
        if self.start.data==target:
            n.next=self.start.next
            n.prev=self.start
            self.start.next=n
        else:
            current=self.start
            while current is not None:
                if current.data==target:
                    n.next=current.next
                    n.prev=current
                    current.next=n
                current=current.next
    
    def delete_first(self):
        self.start=self.start.next
        self.start.prev=None
    
    def delete_last(self):
        if self.start.next is None:
            self.start=None
            
        current=self.start
        while current.next.next is not None:
            current=current.next
        current.next=None
        
    def delete_value(self,data):
        if self.start.data==data:
            self.start=self.start.next
        current=self.start
        while current.next is not None:
            if current.next.data==data:
                current.next=current.next.next
            current=current.next
        
    def display(self):
        current=self.start
        while current is not None:
            print(current.data)
            current=current.next
    
    def search(self,data):
        current=self.start
        while current is not None:
            if current.data==data:
                print(current)
            current=current.next
        
l=dll()
l.insert_last(10)
l.insert_first(5)
l.insert_after(5,6)
l.insert_after(10,20)
l.insert_after(10,15)
l.delete_first()
l.delete_last()
l.delete_value(10)
l.display()