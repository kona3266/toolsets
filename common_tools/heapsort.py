#!/usr/bin/env python
# coding: utf-8
import sys
from optparse import OptionParser

def heapfy(arr, start, end):
    # start stands for root node, find left child, then right child
    root = start
    while True:
        left_c = 2*root + 1
        child = left_c
        if left_c > end:
            break

        right_c = left_c + 1
        if right_c <= end and arr[left_c] < arr[right_c]:
            child = right_c
        
        if arr[child] > arr[root]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break

def runner():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-s", action="store", dest="array", default=None, type="string", help="input arr")
    (options, args) = parser.parse_args()
    array = options.array
    if array is None or not array:
        parser.error("need specify the unsorted array")
    arr = [int(i) for i in array.split(",")]
    length = len(arr)
    # create a max heap
    for i in range((length-2)//2, -1, -1):
        heapfy(arr, i, length-1)
    
    # heap sort
    for i in range(length-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapfy(arr, 0, i-1)
    print(arr)

