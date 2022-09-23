#!/usr/bin/env python3
def find_peak(list_of_integers):
    low = 0
    high = len(list_of_integers)-1
    while low<high:
        mid = low + (high - low+1)//2
        if (mid-1>=0 and list_of_integers[mid-1]<=list_of_integers[mid]):
            low = mid
        else:
            high = mid-1
    return list_of_integers[low+1]

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([15,35,85,96,5,6,8,12]))
# cars = ['Ford', 'BMW', 'Volvo']

# cars.sort(reverse=True)
# print(cars)
# from scipy.signal import find_peaks
# lst = [5, 3, 2, 19, 17, 8, 13, 5, 0, 6, 1, -5, -10, -3, 6, 9, 8, 14, 8, 11, 3,
#     2, 22, 8, 2, 1 ]
# peaks, _ = find_peaks(lst, height=0)
# print(peaks)