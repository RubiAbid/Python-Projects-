'''Fill out the function get_last_element(lst) which takes in a list lst as a parameter
 and prints the last element in the list. The list is guaranteed to be non-empty, but 
 there are no guarantees on its length.'''

def get_last_element(lst):
    print(lst[-1])

if __name__=="__main__":
    get_last_element([0,0,0,0,0,3,303,403,50,460,450])