def partition(array, left, right):
    pivot = array[left]
    i = left + 1

    for j in range(i, right + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    i -= 1
    array[i], array[left] = array[left], array[i]

    return i


def count_quick_sort(array, left, right):
    if len(array) == 1:
        return array
    if left <= right:
        pivot = partition(array, left, right)

        count_quick_sort(array, left, pivot - 1)
        count_quick_sort(array, pivot + 1, right)


file = open("D:\\Algorithms-Specialization\\files\\quick_sort_integers.txt")
lines = file.readlines()
file.close()

num_array = []
for n in range(0, len(lines)):
    lines[n] = lines[n].strip()
    num_array.append(int(lines[n]))

count_quick_sort(num_array, 0, len(num_array) - 1)

print(num_array)
