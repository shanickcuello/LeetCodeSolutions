def unique_occurrences(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    unique_counts = set(count_dict.values())

    return len(unique_counts) == len(count_dict)

arr1 = [1, 2, 2, 1, 1, 3]
arr2 = [1, 2]
arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

if __name__ == '__main__':
    print(unique_occurrences(arr1))
    print(unique_occurrences(arr2))
    print(unique_occurrences(arr3))