def selection_sort(L):
    """Selection sort from MIT OCW
    
    Parameters:
    L (list): Unsorted list.
        
    Returns:
    L (list): Sorted list.
    """
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L
