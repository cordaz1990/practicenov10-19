def mergesort(L: list) -> None:
    """  Reorder the items in L from smallest to largets.
    L = [3,4,7,-1,2,5]
    mergesort(L)
    L
    [-1,2,3,4,5,7]
    """
    for i in range(len(L)):
      workspace.append([L[i]])
      
    i = 0
    while i < len(workspace) - 1
         L1 = workspace[i]
         L2 = workspace[i + 1]
         newL = merge(L1, L2)
         workspace.append(newL)
         i += 2
   if len(workspace) != 0
        L[:] = workspace[-1][:]
