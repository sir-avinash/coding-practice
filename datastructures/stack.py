class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        # return TRUE if the stack is empty
        return self.items == []
        
    def push(self, item):
        # adds an element to the top
        return self.items.append(item)
        
    def pop(self):
        # removes the top most element
        return self.items.pop()
        
    def peek(self):
        # returns the top most element
        return self.items[len(self.items)-1]
        
    def size(self):
        # return the length of the stack
        return len(self.items)
        
        
if __name__ == "__main__":
#def main():
    s = Stack()
    print(s.isEmpty())
    s.push('horn')
    s.push('ok')
    s.push('please')
    print(s.peek())
    s.pop()
    print(s.size())   

#main()     