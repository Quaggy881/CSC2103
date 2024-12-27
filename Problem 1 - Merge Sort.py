# Test merge sort and quick sort algorithms

def merge_sort(arr, left, right, tracing=False):
    # Sort arr[left...right].
    if tracing:
        trace("\nInitially:      ", arr, left, right)
    if left < right:
        m = (left + right) // 2
        merge_sort(arr, left, m, tracing)
        if tracing:
            trace("Left sorted:    ", arr, left, right)
        merge_sort(arr, m + 1, right, tracing)
        if tracing:
            trace("Right sorted:   ", arr, left, right)

        # Create a temp array to merge
        temp_arr = [0] * (right - left + 1)
        merge(arr, left, m, arr, m + 1, right, temp_arr, 0)

        for k in range(left, right + 1):
            arr[k] = temp_arr[k - left]
        if tracing:
            trace("Merged:         ", arr, left, right)
    if tracing:
        trace("Merge-sort:     ", arr, left, right)


def merge(arr1, left1, right1, arr2, left2, right2, temp_arr, left):
    # Merge arr1[left1...right1] and arr2[left2...right2] into temp_arr[left...].
    i = left1
    j = left2
    k = left
    while i <= right1 and j <= right2:
        if custom_key(arr1[i]) <= custom_key(arr2[j]):
            temp_arr[k] = arr1[i]
            i += 1
        else:
            temp_arr[k] = arr2[j]
            j += 1
        k += 1
    while i <= right1:
        temp_arr[k] = arr1[i]
        i += 1
        k += 1
    while j <= right2:
        temp_arr[k] = arr2[j]
        j += 1
        k += 1

def custom_key(item):
    if isinstance(item, (int, float)):
        return (0, item)
    return (1, str(item).lower())


def trace(caption, arr, left, right):
    print(caption + " {", end="")
    for k in range(left, right + 1):
        print(" " + str(arr[k]), end="")
    print(" }")


def parse_item(item):  
    try:
        return float(item) if '.' in item else int(item)
    except ValueError:
        return item.strip()

if __name__ == "__main__":

    user_input = input("Enter elements to sort (separated by commas): ")

    #Converting elements to numbers
    data = [parse_item(x.strip()) for x in user_input.split(',')]

    left = 0
    right = len(data) - 1

    print("\nOriginal Data:", data)
    merge_sort(data, left, right, True)
    print("\nSorted Data:", data)



