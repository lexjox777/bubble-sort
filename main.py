# arr=(49,24,18,5,10,56,40,34,20,4,1)

# def bubble_sort(arr):
#   sorted = False 

#   while not sorted:
#     sorted = True
   
#     for i in range(len(arr)-1):
#      if arr[i] > arr[i+1]
#       sorted = False
#       arr[i], arr[i+1] = arr[i+1], arr[i]


#        #  0  1 2  3  4  5  6  7  8 9 10
#       x=[49,24,18,5,10,56,40,34,20,4,1]

#     #   # sort alist
#     #   bubble_sort(arr)

#     #   # print sorted list
#       print(i+1)

      # ===================================
      
        # x = (49,24,18,5,10,56,40,34,20,4,1):

      # def bubble_sort(x):
      #   sorted = False

      #   while not sorted:
      #     sorted = True

      #      #   0  1  2  3  4  5  6  7  8 9 10
      #     x = (49,24,18,5,10,56,40,34,20,4,1):

      #     for i in range(len(x)-1)
      #     print(x)

       # ===================================

# def bubbleSort(arr):
   
#         arr=(49,24,18,5,10,56,40,34,20,4,1)      
#          for [i] in range(0, len(arr) - 1):
#            for j in range(0, len(arr) - 1 - i):
#              if arr[j] > arr[j+1]:
#                arr[j], arr[j+1] = arr[j+1], arr[j]
#                return arr


#            print(bubbleSort(arr))


       # ===================================


def bubble_sort(arr):
    # begin by assuming list is unsorted
    sorted = False

    # This runs because sorted is False
    while not sorted:
        # assume sorted before iterating over the list
        sorted = True
        # go all the way from 0 - 10
        # len(arr) is 11 
        # range(len(arr) - 1) is basically range(10)
        # range(10) is basically [0,1,2,3,4,5,6,7,8,9] 
        # for i in [0,1,2,3,4,5,6,7,8,9]
        for i in range(len(arr) - 1):
            # i will change from 0,1,2,3,4,5,6,7,8,9
            # arr[i] will go from 49,24,18,5...
            if arr[i] > arr[i+1]:
                # by setting this to False
                # we know line 6 will run again
                # and the process will repeat
                sorted = False
                # here we are simply swapping positions around 
                arr[i], arr[i+1] = arr[i+1], arr[i]

# list to sort
      # 0  1  2 3  4  5  6  7  8 9 10
# x = [49,24,18,5,10,56,40,34,20,4,1]
# alist = [1,2,3,4,5]

# sort alist
bubble_sort(alist)

# print sorted list
print(alist)



