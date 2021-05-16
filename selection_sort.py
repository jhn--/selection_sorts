def selection(L):
    """Selection sort
    
    Parameters:
    L (list): Unsorted list.
        
    Returns:
    L (list): Sorted list.
    """
    for p in range(len(L)):
        for s in range(p+1, len(L)):
            if L[s] < L[p]:
                (L[p], L[s]) = (L[s], L[p])
    return L
