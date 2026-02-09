from unittest import result



#Recursive function always need a stopping condition for it to end. 
#Make sure all starting points coverge to that stopping conditions. 
def recursive_binary_search(list, target):
    list_length = len(list)
    mid_element = list[list_length//2]
    if target == mid_element:
        return list_length//2
    if list_length == 1:
        return None
    elif target<mid_element:
        val = recursive_binary_search(list[:list_length//2], target)
        if val == None:
            return None
        else:
            return val
    else:
        val = recursive_binary_search(list[list_length//2 + 1:], target)
        if val == None:
            return None
        else:
            return val + list_length//2 +1


def binary_search(list, target):

    #The first and last is inclusive here
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last)//2

        if list[mid] ==  target:
            return mid
        elif target < list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    
    return None


result = binary_search([1, 2, 3, 4, 5, 6, 7, 67, 100], 2)
print(result)
