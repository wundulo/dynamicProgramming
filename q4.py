import itertools, operator, json

'''
CS673 Fall 2012 
Assignment 6
Question 4 - Problem 15-9 Breaking a string

Ian, Hei Wong
Section 1
'''

string_size = 25
L = [2,5,8,10]

# string_size = 20
# L = [2,8,10]

directions = ["left-to-right","right-to-left"]
memoized_subproblems = {}

def main():
    
    # build cost table for all permutations
    cost_table = generate_permutations(L, directions)
    
    # print memoized subproblems and their costs
    # print json.dumps(memoized_subproblems, indent=4)
    
    # print optimal solution found
    optimal_solution = find_min_cost(cost_table)
    print "Optimal solution = ",optimal_solution

class String():
    def __init__(self, size):
        self.size = size
        self.last_break = 0
        self.last_right_break = 0
        self.total_cost = 0
        self.path = []
        
    def __repr__(self):
        return str(self.size)+":"+str(self.path)
        
    def break_after(self, num_char, direction, isStart=False):
        
        mem_key = direction+"-"+str(num_char)
        self.path.append(mem_key)
        
        if str(self.path) in memoized_subproblems:
            
            # if the current subproblem is memoized, 
            # look up cost instead of recalculating it            
            
            cost = memoized_subproblems[str(self.path)]
            print str(self.path) + " is memoized = " + str(cost)
            
        else:
        
            # current subproblem is not found in memoization table
            # calculate new cost
            
            if self.size is string_size:
                cost = string_size
                self.last_right_break = num_char
            elif direction == "left-to-right":            
                cost = string_size - self.last_right_break
                self.last_right_break = num_char
            elif direction == "right-to-left":
                cost = self.last_break
                
            if isStart is False:
                memoized_subproblems[str(self.path)] = cost
                
        self.size -= num_char
        self.last_break = num_char
        self.total_cost += cost
        return cost

def generate_permutations(L, directions):
    
    sequences = [list(x) for x in itertools.permutations(L)]
    print "All possible permutations :"
    print sequences
    
    cost_table = {}
    for sequence in sequences:
        s = String(string_size)
        for i, elem in enumerate(sequence):

            # first element, look at the next elem for direction
            if i == 0:  
                next_elem = sequence[i+1]
                if elem < next_elem:
                    
                    cost = s.break_after(elem, "left-to-right", True) 
                    print elem,"=",cost
                    
                elif elem > next_elem:
                    
                    cost = s.break_after(elem, "right-to-left", True)
                    print elem,"=",cost
                    
            # 2nd to nth element, look at last elem for direction
            elif i+1 <= len(sequence): 
                last_elem = sequence[i-1]
                if last_elem < elem:
                    
                    cost = s.break_after(elem, "left-to-right")
                    print last_elem,"<", elem,"=",cost
                    
                elif last_elem > elem:
                    
                    cost = s.break_after(elem, "right-to-left")
                    print last_elem, ">", elem,"=",cost
                    
        print sequence, "total cost =", s.total_cost
        print 
        cost_table[str(sequence)] = s.total_cost
    return cost_table

def find_min_cost(cost_table):
    return sorted(cost_table.iteritems(), key=operator.itemgetter(1))[0]
    
if __name__ == "__main__":
    main()
    