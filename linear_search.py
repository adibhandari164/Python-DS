def linear_search(list, target):
    """
    Returns the position of the target if found, else returns None
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
            
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")

result = linear_search([1, 2, 3, 4, 5], 1)
verify(result)
