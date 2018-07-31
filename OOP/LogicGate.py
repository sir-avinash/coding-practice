class LogicGate:
    def __init__(self, name):
        self.label = name
        self.output = None
        
    def getLabel(self):
        return self.label
        
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
        
class BinaryGate(LogicGate):
    def __init__(self, name):
        LogicGate.__init__(self, name)
        ### Another way to do it
        # super().__init__(name)
        self.inpA = None
        self.inpB = None

    def get_inpA(self):
        if self.inpA is None:
            return int(input("Enter input A for gate "+ self.getLabel()+"-->"))
        else:
            return self.inpA.getFrom().getOutput()
    
    def get_inpB(self):
        if self.inpB is None:
            return int(input("Enter input B for gate "+ self.getLabel()+"-->"))
        else:
            return self.inpB.getFrom().getOutput() 
            
    def setNextInp(self, new_conn):
        if self.inpA is None:
            self.inpA = new_conn
        elif self.inpB is None:
            self.inpB = new_conn
        else:
            raise ValueError("No Empty Pins!")
                
class UnaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)        
        self.inpA = None
        

    def get_inpA(self):
        if self.inpA is None:
            return int(input("Enter input A for gate "+ self.getLabel()+"-->"))
        else:
            return self.inpA.getFrom().getOutput()
                        
    def setNextInp(self, new_conn):
        if self.inpA is None:
            self.inpA = new_conn
        else:
            raise ValueError("No Empty Pins!")
    
class AndGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)
        
    def performGateLogic(self):
        inpA = self.get_inpA()
        inpB = self.get_inpB()
        
        if inpA == 1 and inpB == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)
        
    def performGateLogic(self):
        inpA = self.get_inpA()
        inpB = self.get_inpB()
        
        if inpA == 0 and inpB == 0:
            return 0
        else:
            return 1
            
class NotGate(UnaryGate):
    def __init__(self, name):
        super().__init__(name)
        
    def performGateLogic(self):
        inpA = self.get_inpA()
        
        if inpA == 1:
            return 0
        else:
            return 1
                
#############################                 
class Connector:

    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        
        to_gate.setNextInp(self)
        
    def getFrom(self):
        return self.from_gate
        
    def getTo(self):
        return self.to_gate


  
def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()          