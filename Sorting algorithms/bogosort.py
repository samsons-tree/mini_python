from random import shuffle
from time import time

def bogosort(seq:list):
    '''Randomly shuffle sequence and then check if it's in the correct order.
       Repeat until sequence is sorted from lowest to highest.
    '''
    shuffles = 0
    while True:
        count = 0
        for i in range(1,len(seq)):
            if seq[i-1] < seq[i]:
                count += 1
        if count == len(seq) -1:
            break
        shuffle(seq)
        shuffles += 1
    return seq, shuffles

if __name__ == '__main__':
  sequence = list(range(20,10,-1))
  
  start = time()
  bogo, iterations = bogosort(sequence)
  end = time()
  execution_time = end - start

  print(f'Done. {iterations=}. Time: {execution_time=}')
