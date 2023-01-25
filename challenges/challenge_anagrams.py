def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)

    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]

    i, j = 0, 0

    for k in range(start, end):
        if i >= len(left):
            arr[k] = right[j]
            j += 1
        elif j >= len(right):
            arr[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def is_anagram(first_string, second_string):
    first_list = [*first_string.lower()]
    second_list = [*second_string.lower()]

    merge_sort(first_list)
    merge_sort(second_list)

    first_string = "".join(first_list)
    second_string = "".join(second_list)

    if not first_string or not second_string:
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)
