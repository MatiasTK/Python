#function that determines whether the array contains any duplicates.
def contains_duplicates(arr):
    #create a set
    s = set()
    #loop through the array
    for i in arr:
        #if the set contains the element
        if i in s:
            #return true
            return True
        #if not, add the element to the set
        else:
            s.add(i)
    #return false
    return False

