from time import time

def insertion_sort(unsorted: list):
    ''' Simple insertion sort to sort numbers into ascending order.
    '''
    for n in range(1,len(unsorted)):
        to_sort = unsorted[n]
        index = n
        while index > 0 and unsorted[index] < unsorted[index-1]:
                unsorted[index] = unsorted[index-1]
                unsorted[index-1] = to_sort
                index -= 1

if __name__ == '__main__':
    sequence = list(range(50,10,-1))
    start = time()
    sorted = insertion_sort(sequence)
    end = time()
    
    print(f'{sorted}. \n{execution_time=} seconds')
