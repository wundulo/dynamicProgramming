import operator, copy

'''
CS673 Fall 2012 
Assignment 6
Question 1

Ian, Hei Wong
Section 1
'''

def main():
    
    # 1a) common dimension is smallest
    print "1a) common dimension is smallest"
    
    solution = numScalarMult([Matrix("A3",50,5), Matrix("A2",5,100),Matrix("A1",100,10)])
    print "(A1 (A2 A3)) =",solution
    solution = numScalarMult([Matrix("A1",10,100), Matrix("A2",100,5), Matrix("A3",5,50)])
    print "which is greater than multiplying the largest common dimension first ((A1 A2) A3) =",solution
    print "therefore multiplying smallest common dimension matrices first does not give optimal solution\n"

    # 1b) common dimension is largest
    print "1b) common dimension is largest"
    A = Matrix("A",10,1000)
    B = Matrix("B",1000,100)
    C = Matrix("C",100,10)
    D = Matrix("D",10,1)
    
    solution = numScalarMult([A,B,C,D])
    print "((A B) C) D) =",solution
    solution = numScalarMult([D.rotate(),C.rotate(),B.rotate(),A.rotate()])
    print "which is greater than multiplying the smallest common dimension first: (A (B (C D))) =",solution
    print "therefore multiplying largest common dimension matrices first does not give optimal solution\n"

    # 1c) minimize pi-1*pk*pj
    print "1c) minimize pi-1*pk*pj"
    A = Matrix("A",10,2)
    B = Matrix("B",2,100)
    C = Matrix("C",100,10)
    D = Matrix("D",10,1)
    
    solution = numScalarMult([A,B,C,D])
    print "((A B) C) D) =",solution
    solution = numScalarMult([D.rotate(),C.rotate(),B.rotate(),A.rotate()])
    print "which is greater than multiplying the another solution: (A (B (C D))) =",solution
    print "therefore multiplying 2 matrices with minimized pi-1*pk*pj first does not give optimal solution\n"  
    
class Matrix():
    """A matrix instance"""
    def __init__(self, name, rows, columns):
        self.name = name
        self.rows = rows
        self.columns = columns
        
    def __repr__(self):
        return self.name +":"+str(self.rows)+"x"+str(self.columns)
        
    def rotate(self):
        temp = self.rows
        self.rows = self.columns
        self.columns = temp
        return self
        
def numScalarMult(matrices):
    
    for i,matrix in enumerate(matrices):

        if i+1 is len(matrices): break
        
        A = matrix
        B = matrices[i+1]
        
        if A.columns is not B.rows:
            print "Incompatible dimensions"
            return
            
    numOps = reduce(operator.mul, [m.rows for m in matrices])
    numOps += matrices[0].rows* reduce(operator.mul, [m.columns for m in matrices[1:]])
    return numOps

if __name__ == '__main__':
    main()
    