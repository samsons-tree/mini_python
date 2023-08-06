def selection_sort(unsorted: list, order = 'asc') -> list:
    ''' Sort in ascending order.
    '''
    for n in range(len(unsorted)):
        smallest = n
        for m in range(n+1,len(unsorted)):
            if unsorted[m] < unsorted[smallest]:
                smallest = m
        unsorted_item = unsorted[n]
        unsorted[n] = unsorted[smallest]
        unsorted[smallest] = unsorted_item
    return unsorted

if __name__ == '__main__':
    sequence = list(range(5000,10,-1))
    start = time()
    sorted = selection_sort(sequence)
    end = time()
    execution_time = end - start
    
    print(f'{sorted}. \n{execution_time = } seconds')
