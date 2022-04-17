import numpy
heap=numpy.zeros([10,2])
def makenewheap(numbers):
    global heap
    heap=numpy.zeros([numbers,2])

def insert(data):
    current=0
    while True:
        if heap[current][1]==0:
            heap[current][1]=data
            break
        else:
            current=current+1
    for i in range(len(heap)):
        while

makenewheap(10)




