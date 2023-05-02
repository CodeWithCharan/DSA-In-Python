# Time Complexity
# O(n) --> time = a*n+b
# def get_squared_numbers(numbers):
#     squared_numb = []
#     for n in numbers:
#         squared_numb.append(n*n)
#     return squared_numb

# numbers = [2, 5, 8, 9]  
# print(get_squared_numbers(numbers))


# O(1) --> time = a
# def find_first_pe(Prices, eps, index):
#     pe = Prices[index]/eps[index]
#     return pe


# O(n^2) --> time = a*n^2+b
# numbers = [3, 6, 2, 4, 3, 6, 8, 9]
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             print(str(numbers[i])+" is duplicate")
#             break


# O(log n) --> time = log^n 2 
def binary_search(arr, x):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            return mid
    return -1

numbers = [4, 9, 15, 21, 34, 57, 68, 91]
target = 68

result = binary_search(numbers, target)

if result == -1:
    print(f"{target} was not found in the array")
else:
    print(f"{target} was found at index {result} in the array")