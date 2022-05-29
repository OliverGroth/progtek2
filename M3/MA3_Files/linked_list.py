""" linked_list.py

Student: Oliver Groth
Mail: Oliver.Groth.7974@student.uu.se
Reviewed by: Kieran
Date reviewed: 16 May
"""

class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ      
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self):             # Optional
        l = 0
        f = self.first
        while f:
            f = f.succ
            l += 1
        return l
  
  
    def mean(self):               # Optional
        pass
    
    
    def remove_last(self):        # Optional
        pass
    
    
    def remove(self, x):          # Compulsory
        f = self.first
        if f.data == x:
            self.first = f.succ
            return True
        while f.succ:
            print(f.succ.data)
            if f.succ.data == x:
                f.succ = f.succ.succ
                return True
            f = f.succ
        return False




    
    
    def count(self, x):           # Optional
        pass
    
    
    def to_list(self):            # Compulsory
        return self._to_list(self.first)

    def _to_list(self,f):
        if f is None:
            return []
        else:
            return [f.data] + self._to_list(f.succ)

    
    
    def remove_all(self, x):      # Compulsory
        self._remove_all(x,self.first) # Kan inte ta bort den första
        if self.first.data == x: # Tar bort första om det krävs
            self.first = self.first.succ

    def _remove_all(self,x,f):
        if f.succ is None:
            return
        if f.succ.data == x:
            f.succ = f.succ.succ
            return self._remove_all(x,f)
        return self._remove_all(x,f.succ)
    
    
    def __str__(self):            # Compulsary
        if self.first is None:
            return "()"
        else:
            result = "("
            for data in self:
                result = result + str(data) + ", "
            result = result[:-2] # Tar bort kommatecken och space från sista
            result = result + ")"
            return result
    
    
    def merge(self, lst):         # Compulsory
        for data in lst:
            self.insert(data)
    
    
    def __getitem__(self, ind):   # Compulsory
        i = 0
        for data in self:
            result = data
            if i == ind:
                return data
            i += 1
        return "Error"


class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self,other):
        if self.pnr < other.pnr:
            return True
        else:
            return False

    def __le__(self,other):
        if self.pnr <= other.pnr:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.pnr > other.pnr:
            return True
        else:
            return False

    def __ge__(self,other):
        if self.pnr >= other.pnr:
            return True
        else:
            return False

    def __eq__(self,other):
        if self.pnr == other.pnr:
            return True
        else:
            return False


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    #lst.print()
    
    # Test code:
    #print(lst.length())
    #print(lst.remove(1))
    #print(lst.to_list())
    #lst.remove_all(7)
    #lst.print()

    test1 = Person("Anders",1999)
    test2 = Person("Anna", 1998)

    personer = [test1,test2]
    listan = LinkedList()
    for personen in personer:
        listan.insert(personen)

    listan.print()

if __name__ == '__main__':
    main()
    


    

