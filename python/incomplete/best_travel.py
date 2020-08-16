#
# Best Travel
#
# Summary: 
#     - John and Mary want to travel between a few towns 
#         - A, B, C 
#     - Mary has a list of distances between these towns  
#         - ls = [50, 55, 57, 58, 60]
#     - John says he doesn't want to drive 
#         - more than t = 174 miles 
#         - he will visit only 3 towns
# Problem: 
#     - Which distances, (i.e. towns), will they choose 
#         - so that the sum of the distances is the biggest possible to please Mary and John
#
# Explanation:
#     - With list ls and 3 towns to visit they can make a choice between: 
#         - [50,55,57]
#         - [50,55,58]
#         - [50,55,60]
#         - [50,57,58]
#         - [50,57,60]
#         - [50,58,60]
#         - [55,57,58]
#         - [55,57,60]
#         - [55,58,60]
#         - [57,58,60]
#     - The sums of distances are then: 
#         - 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.
#     - The biggest possible sum taking a limit of 174 into account 
#         - is then 173 
#         - the distances of the 3 corresponding towns is [55, 58, 60].
#     - choose_best_sum  will take as parameters 
#         - t = maximum sum of distances, integer >= 0, 
#         - k = number of towns to visit, k >= 1 
#         - ls = list of distances, 
#             - all distances are positive or null integers 
#             - list has at least one element 
#     - The function returns 
#         - the biggest possible sum of k distances less than or equal to the given limit t if that sum exists, 
#         - otherwise returns (nil, null, None, Nothing)
# Examples:
#     - ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163
#     - xs = [50] choose_best_sum(163, 3, xs) -> nil 
#     - ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228

# Note: 
#     - don't modify the input list ls
# def choose_best_sum(t, k, ls):
import itertools
from operator import itemgetter
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
ls = [50, 55, 57, 58, 60]
def choose_best_sum(max_distance, num_of_towns, distances):
    dist = list(itertools.permutations(distances, (num_of_towns)))
    sorted_list = []
    sum_list = []
    closest_number_to_limit = 0
    for x in dist:
        sorted_list.append(sorted(x))
    unique_tuples = [t for t in (set(tuple(i) for i in sorted_list))] 
    unique_arrays = [list(ele) for ele in unique_tuples]
    for x in unique_arrays:
        sum_list.append(sum(x))
    for num in sum_list:
        if num > max_distance:
            index = sum_list.index(num)
            # sum_list.pop(index)
            del sum_list[index]


    # closest_number_to_limit = min(sum_list, key=lambda x:abs(x-max_distance))
    # if closest_number_to_limit > max_distance:
    #     return None
    # else:
    #     return closest_number_to_limit
    return max_distance
# Test.assert_equals(choose_best_sum(230, 4, xs), 230)
# Test.assert_equals(choose_best_sum(430, 5, xs), 430)
# Test.assert_equals(choose_best_sum(430, 8, xs), None)
print(choose_best_sum(230, 4, ls)) # 230
print(choose_best_sum(430, 5, xs)) # 430
print(choose_best_sum(430, 8, xs)) # None
