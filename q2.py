import sets

'''
CS673 Fall 2012 
Assignment 6
Question 2

Ian, Hei Wong
Section 1
'''

m = {
    "a" : {"a": "b", "b": "b", "c": "a"},
    "b" : {"a": "c", "b": "b", "c": "a"},
    "c" : {"a": "a", "b": "c", "c": "c"}
}

x = "bbbba"
# x = "bac"
result = "a"
memoized_subproblems = {}

def main():
    
    # find all possible permutations of each length of substring and
    # take the union of all possible products when split at i
    
    all_result_sets = []
    for index, value in enumerate(x):
        if index is not 0:
            
            # split string into left and right substrings
            left = x[:index]
            right = x[index:]
            
            # find all possible values given each substring
            a = ''.join(find_possible_value(left))
            b = ''.join(find_possible_value(right))
            
            # get the product of all possible values from each substring
            substring_possible_value_set = [m[char_a][char_b] for char_b in list(b) for char_a in list(a)]
            all_result_sets.append(sets.Set(substring_possible_value_set))
            
    # take the union of all possible values from substrings
    final_sets = sets.Set()
    num_expressions = 0
    for o in all_result_sets:
        if result in o:
            num_expressions += 1
        final_sets = final_sets | sets.Set(o)
    
    # print results
    print
    print "x = ",x+", Result expression = ", result
    if result in list(final_sets):
        print "2a) Yes"
        print "2b) Number of expression can be parethesized to get ",result," = ",num_expressions
    else:
        print "2a&b) No"

def find_possible_value(string):
    
    possible_values = []
    
    temp = [char for char in string]
    print "traverse substring:",temp
    while len(temp) > 1:
        i = temp.pop(0)
        j = temp.pop(0)
        pair = i+j
        if pair in memoized_subproblems:
            print pair," is memoized"
        else:
            memoized_subproblems[pair] = m[i][j]
        temp.insert(0, memoized_subproblems[pair])
    possible_values.append(temp[0])
    return set(possible_values)
    
if __name__ == '__main__':
    main()
    