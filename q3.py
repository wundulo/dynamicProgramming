import random, json, copy, operator

'''
CS673 Fall 2012 
Assignment 6
Question 3 - Problem 15-8 Image compression by seam carving

Ian, Hei Wong
Section 1
'''

paths_costs = {}
final_paths = {}
memoized_subproblems = {}

def main():
    
    '''
    Picture matrix:
    [ A B C ]
    [ D E F ]
    [ G H I ]
    '''
        
    # row 3 pixels
    G = Pixel("G", random.randint(1,10), None, None, None)
    H = Pixel("H", random.randint(1,10), None, None, None)
    I = Pixel("I", random.randint(1,10), None, None, None)
    
    # row 2 pixels
    D = Pixel("D", random.randint(1,10), None, G, H)
    E = Pixel("E", random.randint(1,10), G, H, I)
    F = Pixel("F", random.randint(1,10), H, I, None)
    
    # row 1 pixels
    A = Pixel("A", 1, None, D, E)
    B = Pixel("B", 1, D, E, F)
    C = Pixel("C", 1, E, F, None)
    
    top_pixels = [A,B,C]
    all_pixels = [A,B,C,D,E,F,G,H,I]
    pic = Picture("picture", top_pixels, all_pixels, 3)

    # find all possible seams starting from each top pixel
    for top_pixel in top_pixels:
        path = []
        cost = 1
        find_paths(top_pixel, path, cost, pic)
    
    # print json.dumps(paths_costs, indent=4)
    # print json.dumps(final_paths, indent=4)
    
    print "Memoized sub_paths and their costs = "+json.dumps(memoized_subproblems, indent=4)
    
    print "Optimal seam = "+ str(find_least_cost_seam(final_paths))

class Pixel():
    def __init__(self, name, cost, left_child=None, center_child=None, right_child=None):
        self.name = name
        self.cost = cost
        self.left_child = left_child
        self.center_child = center_child
        self.right_child = right_child
        
    def __repr__(self):
        return "("+self.name+":"+str(self.cost)+")"
        
class Picture():
    def __init__(self, name, top_pixels, all_pixels, rows):
        self.name = name
        self.top_pixels = top_pixels
        self.all_pixels = all_pixels
        self.rows = rows

def find_least_cost_seam(final_paths):
    return sorted(final_paths.iteritems(), key=operator.itemgetter(1))[0]
            
def find_paths(pixel, path, cost, pic):
    
    # append to current path
    path.append(pixel)
    
    # update current path and cost
    if pixel not in pic.top_pixels:
        path_string = ''.join([pixel.name for pixel in path])[1:]
        if path_string in memoized_subproblems:
            print path_string, " is memoized already."
            cost = memoized_subproblems[path_string]
        else:
            # not memoized, now calcuate cost
            cost += pixel.cost
    
    # record path
    paths_costs[str(path)] = cost
    
    # memoize sub paths for dynamic programming
    if pixel not in pic.top_pixels:
        path_string = ''.join([pixel.name for pixel in path])[1:]
        if path_string not in memoized_subproblems:
            memoized_subproblems[path_string] = cost
    
    if len(path) == pic.rows:
        final_paths[str(path)] = cost
    
    if pixel is None: return
    
    if pixel.left_child is not None:
        path_left = copy.copy(path)
        find_paths(pixel.left_child, path_left, cost, pic)
        
    if pixel.center_child is not None:
        path_center = copy.copy(path)
        find_paths(pixel.center_child, path_center, cost, pic)
        
    if pixel.right_child is not None:
        path_right = copy.copy(path)
        find_paths(pixel.right_child, path_right, cost, pic)
                
if __name__ == "__main__":
    main()
    