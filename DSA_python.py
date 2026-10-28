# List is a built-in dynamic array which can store elements of different data types.
# It is an ordered collection of item, that is elements are stored in the same order as they were inserted into the list.
# List stores references to the objects (elements) rather than storing the actual data itself.

# a = [10, 20, "GfG", 40, True]
# print(a[2])



#  Searching Algorithms
# Searching algorithms are used to locate a specific element within a data structure, such as an array, list, or tree. 
# They are used for efficiently retrieving information in large datasets.





# import bisect  
# a = [2, 4, 6, 8, 10]
# print(6 in a)       
# print(a.count(8) > 0)   
# pos = bisect.bisect_left(a, 8)
# print("Found at index:", pos)

# True
# False
# Found at index: 3


# Sorting Algorithms
# Sorting algorithms are used to arrange the elements of a data structure, such as an array, list, or tree, in a particular order, 
# typically in ascending or descending order.
# These algorithms are used for organizing data, which enables more efficient searching, merging, and other operations.





# nums = [5, 3, 8, 1]
# nums.sort()
# print(nums)     
# print(sorted(nums, reverse=True))

How to initialise a list?

# n = int(input(" "))

# my_list = []

# print(f"Ab ek-ek karke {n} numbers enter karo:")
# for i in range(n):
#     number = int(input(f"Element {i+1}: "))
#     my_list.append(number)  # list mein number jodte jao

# # 4. Final list ko print kar do
# print("\nAapki final list yeh hai:", my_list)

my_list = list()