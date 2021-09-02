# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def removeKFromList(l, k):
    x = 0
    new_list = set()
    for x in range(len(l)):
        if l[x] != k:
            new_list.add(l[x])
    new_list = list(new_list)
    return new_list

l = [3, 1, 2, 3, 4, 5]
k = 3

print(removeKFromList(l,k))
    
        

